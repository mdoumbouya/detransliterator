# detransliterator

![Build](https://github.com/mdoumbouya/detransliterator/actions/workflows/ci.yaml/badge.svg) [![PyPI - Version](https://img.shields.io/pypi/v/detransliterator.svg)](https://pypi.org/project/detransliterator)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/detransliterator.svg)](https://pypi.org/project/detransliterator)




-----

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

```console
pip install detransliterator
```

## Usage

**as a software library**
```python
from detransliterator import Detransliterator

detransliterator = Detransliterator('latin2nqo_001.35')
latin = "musa dunbuya"
nqo = detransliterator.detransliterate(latin, beam_size=5)
assert nqo == "ߡߎߛߊ߫ ߘߎ߲ߓߎߦߊ"
```

**as a console tool**
```console
python -m detransliterator.tool --help
```

**example: detransliterate a stream**
```console
echo "musa dunbuya" | python -m detransliterator.tool
```

**example: detransliterate a csv file**
```console
cat file.latin                     \
    | python -m detransliterator.tool    \
        --csv-separator \t        \
        --csv-column 1            \
        --csv-target-column-name  \
    > file.nqo
```
**example: use a particular GPU**
```console
CUDA_VISIBLE_DEVICES="1" echo "musa dunbuya" | python -m detransliterator.tool
```
## License

`detransliterator` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
