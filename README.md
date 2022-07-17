# latin2nqo

[![PyPI - Version](https://img.shields.io/pypi/v/latin2nqo.svg)](https://pypi.org/project/latin2nqo)
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
```
python -m latin2nqo.tool --help
```

**Example: detransliterate a stream**
```
cat file.latin | python -m latin2nqo.tool > file.nqo
```

**TODO: Example: detransliterate a csv file**
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
