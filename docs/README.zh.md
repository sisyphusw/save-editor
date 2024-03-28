
<!-- language: zh -->
[![中文](https://img.shields.io/badge/lang-zh-red.svg)](https://github.com/sisyphusw/save-editor/blob/main/docs/README.zh.md)
[![en](https://img.shields.io/badge/lang-en-green.svg)](https://github.com/sisyphusw/save-editor/blob/main/README.md)

**游戏存档编辑器** by python

提供一种通用的解析、修改和转换 二进制存档文件的思路

## 如何实现

通过[Kaitai Struct](https://github.com/kaitai-io/kaitai_struct), 一种声明性语言，用于描述文件或内存中的各种二进制数据结构。

### 定义
定义二进制存档文件的数据格式，用yaml文件[unicorn_overlord_dat.ksy](./unicorn_overlord/switch/v1_00/unicorn_overlord_dat.ksy)

- 魔数
- 文件大小
- 存档槽位

```yaml
seq:
  - id: magic
    size: 8
    contents: [0x00,0x00,0x00,0x00,UCSD]
  - id: unknow
    size: 4
    contents: [0xd5,0x50,0x1c,0x00]
  - id: file_size
    type: u4
  - id: slot
    type: u4
```

### 编译
使用`kaitai_struct_compiler`，将`unicorn_overlord_dat.ksy`编译为

python文件[unicorn_overlord_dat.py](./unicorn_overlord/switch/v1_00/unicorn_overlord_dat.py)。如何就可以将二进制数据被解析为python中的数据对象
```python
class UnicornOverlordDat(ReadWriteKaitaiStruct):
    def _read(self):
        self.magic = self._io.read_bytes(8)
        self.file_size = self._io.read_u4le()
        self.slot = self._io.read_u4le()
```


## 如何使用
如果要使用命令行工具的话，需要安装`typer`

    pip3 install typer

### 命令行
目前使用[typer](https://github.com/tiangolo/typer)写了一个简陋的命令行工具，提供解析和修改功能
```shell
# parse
python main.py parse "Unicorn Overlord" "switch" "v1.00" example/UCSAVEFILE03.DAT --output UCSAVEFILE03.DAT.json

# edit
python main.py edit "Unicorn Overlord" "switch" "v1.00" example/UCSAVEFILE03.DAT UCSAVEFILE03.DAT.edited.json --output UCSAVEFILE03.DAT.edited
```
### python 
调用`save_editor.py`文件中的`SaveEditor`对象
```python
from save_editor import SaveEditor

se = SaveEditor(game, platform, version)
# parse
parsed_dict = se.parse(bytes)
# edit
edited_bytes = se.edit(dict, bytes)
```
实际代码很简单，只是为了模块版本管理。考虑到一个游戏在多个平台上

存档文件格式可能会有所区别，另外版本差距太大也可能变化

## 比较
#### 传统方式 
二进制数据结构定义和解析逻辑在代码逻辑中
* 简单直接
* 维护和扩展相对麻烦，试想一下重复写类似的逻辑的心情
#### 声明式
用特定语言定义在yaml文件中
* 通用易扩展
* 学习曲线陡峭

## 扩展
kaitai的可视化[Web IDE](https://ide.kaitai.io)

这个思路也可以用于其他场景，

IDE里有很多已经定义好的文件格式，比如压缩，图片和网络相关的

## Credit
[pj1980](https://gbatemp.net/members/pj1980.378437) from [GBATEMP](https://gbatemp.net/threads/unicorn-overlord-save-editing.650584) —— 圣兽之王存档格式解析 