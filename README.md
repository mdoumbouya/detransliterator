# latin2nqo

[![PyPI - Version](https://img.shields.io/pypi/v/latin2nqo.svg)](https://pypi.org/project/latin2nqo)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/latin2nqo.svg)](https://pypi.org/project/latin2nqo)

![build](https://github.com/mdoumbouya/latin2nqo/actions/workflows/ci.yaml/badge.svg)


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
from latin2nqo import latin2nqo

model = latin2nqo.get_model_by_name('001.35')
latin = "musa dunbuya"
reference_nqo = "ߡߎߛߊ߫ ߘߎ߲ߓߎߦߊ"
nqo = model.translate(latin, beam=5)
assert reference_nqo == nqo
```

**as a console tool**
```console
python -m latin2nqo.tool --help
```

**Example: detransliterate a stream**
```
cat file.latin | python -m latin2nqo.tool > file.nqo
```

**Example: detransliterate a csv file**
```
cat file.latin                     \
    | python -m latin2nqo.tool    \
        --csv-separator \t        \
        --csv-column 1            \
        --csv-target-column-name  \
    > file.nqo
```

## License

`latin2nqo` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
