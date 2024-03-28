import os
import io
import re
from enum import Enum

from .kaitaistruct import KaitaiStream, ReadWriteKaitaiStruct
from .unicorn_overlord_dat import UnicornOverlordDat as svd





GAME_VERSION = 'v1.00'
KSDUMP_VERSION = '0.7'
KSDUMP_PATH = 'ksdump'
KSY_PATH = os.path.join(os.path.dirname(__file__), 'unicorn_overlord_dat.ksy')



# 通过__all__指定暴露的内容
__all__ = ['parse', 'edit', 'convert', 'KSDUMP_VERSION', 'KSDUMP_PATH', 'KSY_PATH', 'GAME_VERSION']


def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

# help function
def recur_parse(save_object):
    ignore_list = ['_io', '_parent', '_root', '_seq', '_read', '_check', '_fetch_instances', '__write', '_unname', '_m_']
    save_data = {}
    a = dir(save_object)
    for k in dir(save_object):
        v = save_object.__getattribute__(k)
        if k.isupper() or k.startswith('_') or k.endswith('_write'):
            continue 

        if isinstance(v, ReadWriteKaitaiStruct):
            save_data[k] = recur_parse(v)
        elif issubclass(v.__class__, Enum):
            save_data[k] = camel_to_snake(v.__class__.__name__) + '_'+ v.name
        elif isinstance(v, int):
            save_data[k] = v
        elif isinstance(v, str):
            save_data[k] = v
        elif isinstance(v, bytes):
            save_data[k] = v.hex(" ", 1).upper()
        elif isinstance(v, list):
            save_data[k] = [recur_parse(i) for i in v]

    return save_data

# 解析
def parse(save_bytes) -> dict:
    save_object = svd.from_bytes(save_bytes)
    save_object._read()
    save_object._fetch_instances()
    
    save_data = recur_parse(save_object)
    
    return save_data


# help function
def recur_edit(save_data, save_object):
    for k, v in save_data.items():
        ov = getattr(save_object, k)
        if isinstance(ov, ReadWriteKaitaiStruct):
            recur_edit(v, ov)
        elif isinstance(ov, Enum):
            for member_name in type(ov).__members__.keys():
                if v.endswith(member_name):
                    setattr(save_object, k, type(ov)[member_name])
        elif isinstance(ov, bytes):
            setattr(save_object, k, bytes.fromhex(v.replace(' ', '')))
        elif isinstance(ov, list):
            for lov, lv in zip(ov, v):
                recur_edit(lv, lov)
        else:
            setattr(save_object, k, v)

# 修改
def edit(save_data, save_bytes) -> bytes:
    save_object = svd.from_bytes(save_bytes)
    save_object._read()
    save_object._fetch_instances()
    _io = KaitaiStream(io.BytesIO(save_bytes))
    recur_edit(save_data, save_object) 

    save_object._check()
    save_object._write(_io)

    return _io.to_byte_array()


# 转换
def convert(save_bytes) -> bytes:
    return save_bytes







# 测试
if __name__ == '__main__':
    filepath = r'C:\Users\zengq\AppData\Roaming\Ryujinx\bis\user\save\0000000000000014\0\UCSAVEFILE01.DAT'

    with open(filepath, 'rb') as f:
        bytes_data = f.read()
    save_data = parse(bytes_data)
    save_data['gold'] =100
    save_data['renown'] =100
    edit_bytes = edit(save_data, bytes_data)

    with open(filepath, 'wb') as f:
        f.write(edit_bytes)
        f.close()
    pass