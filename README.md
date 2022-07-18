# latin2nqo

![Build](https://github.com/mdoumbouya/latin2nqo/actions/workflows/ci.yaml/badge.svg) [![PyPI - Version](https://img.shields.io/pypi/v/latin2nqo.svg)](https://pypi.org/project/latin2nqo)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/latin2nqo.svg)](https://pypi.org/project/latin2nqo)




-----

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

```console
pip install latin2nqo
```

## Usage

**as a software library**
```python
from latin2nqo import Detransliterator

detransliterator = Detransliterator('001.35')
latin = "musa dunbuya"
nqo = detransliterator.detransliterate(latin, beam_size=5)
assert reference_nqo == "ߡߎߛߊ߫ ߘߎ߲ߓߎߦߊ"
```

**as a console tool**
```console
python -m latin2nqo.tool --help
```

**example: detransliterate a stream**
```console
echo "musa dunbuya" | python -m latin2nqo.tool
```

**example: detransliterate a csv file**
```console
cat file.latin                     \
    | python -m latin2nqo.tool    \
        --csv-separator \t        \
        --csv-column 1            \
        --csv-target-column-name  \
    > file.nqo
```
**example: use a particular GPU**
```console
CUDA_VISIBLE_DEVICES="1" echo "musa dunbuya" | python -m latin2nqo.tool
```
## License

`latin2nqo` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
