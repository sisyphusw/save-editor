<!-- language: en -->
[![中文](https://img.shields.io/badge/lang-zh-red.svg)](https://github.com/sisyphusw/save-editor/blob/main/docs/README.zh.md)
[![en](https://img.shields.io/badge/lang-en-green.svg)](https://github.com/sisyphusw/save-editor/README.md)


**Game Save Editor** write in Python

Provide a generic approach to parsing, editing, and converting binary save files.

## How it Works

Base on [Kaitai Struct](https://github.com/kaitai-io/kaitai_struct), a declarative language for describing various binary data structures found in files or memory.

### Define
Defines the data format of the binary save file using a YAML file [unicorn_overlord_dat.ksy](./unicorn_overlord/switch/v1_00/unicorn_overlord_dat.ksy).

- Magic Number
- File Size
- Slot

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
### Compile
Using `kaitai_struct_compiler`, compiles `unicorn_overlord_dat.ksy` into a
python file [unicorn_overlord_dat.py](./unicorn_overlord/switch/v1_00/unicorn_overlord_dat.py), which allows binary data to be parsed into Python data objects.
```python
class UnicornOverlordDat(ReadWriteKaitaiStruct):
    def _read(self):
        self.magic = self._io.read_bytes(8)
        self.file_size = self._io.read_u4le()
        self.slot = self._io.read_u4le()
```

## How to Use

If you want to use command-line tool, you need to install `typer`.

    pip3 install typer

### CLI
a command-line tool is written using typer, which can parse and edit save file. 

game support

* Unicron Overlord

```shell
# parse
python main.py parse "Unicorn Overlord" "switch" "v1.00" example/UCSAVEFILE03.DAT --output UCSAVEFILE03.DAT.json

# edit
python main.py edit "Unicorn Overlord" "switch" "v1.00" example/UCSAVEFILE03.DAT UCSAVEFILE03.DAT.edited.json --output UCSAVEFILE03.DAT.edited
```

### python 
`SaveEditor` object from the `save_editor.py` file.
```python
from save_editor import SaveEditor

se = SaveEditor(game, platform, version)
# parse
parsed_dict = se.parse(bytes)
# edit
edited_bytes = se.edit(dict, bytes)
```

Actual, the code is very simple. But for module version management, considering that a game may be on multiple platforms, the save file format may differ, and also version masters.

## Pros && Cons
#### Traditional 
Binary data structure definitions and parsing logic are in the code logic.
* Simple and straight
* Maintain and extension are relatively difficult, repeatedly writing similar code.
#### Declarative
Defined in YAML or other file format using a specific language
* Universal and easy to extend
* Steep learning curve

## What more
Kaitai's visual Web IDE

This approach can also be used in other scenarios.

The IDE has many predefined file formats, such as compression, images, and network-related.

## Credit
[pj1980](https://gbatemp.net/members/pj1980.378437) from [GBATEMP](https://gbatemp.net/threads/unicorn-overlord-save-editing.650584) —— Unicorn Overlord save file format parsing