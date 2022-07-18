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

### as a software library
```python
from detransliterator import Detransliterator

detransliterator = Detransliterator('latin2nqo_001.35')
latin = "musa dunbuya"
nqo = detransliterator.detransliterate(latin, beam_size=5)
assert nqo == "ߡߎߛߊ߫ ߘߎ߲ߓߎߦߊ"
```

### as a console tool
```console
# detransliteration tool
python -m detransliterator.tool --help

# csv/tsv extraction tool
python -m detransliterator.csv_tool --help
```

**example: detransliterate a stream**
```console
echo "musa dunbuya" | python -m detransliterator.tool --model-name latin2nqo_001.35
```

**example: extract a column from a csv file**
```console
cat test_csv_no_header.csv \
| python -m detransliterator.csv_tool \
    extract-column --column-ix 1 \
> tmp_col1.txt
```

**example: extract a column from  a tsv file**
```console
cat test_tsv_with_header.tsv \
| python -m detransliterator.csv_tool \
    extract-column --column-ix 1 --skip-lines 1 --csv-formatting-params delimiter tab \
> tmp_col2.txt
```

**example: detransliterate a column from a csv file**
```console
cat test_tsv_no_header.tsv \
| python -m detransliterator.csv_tool extract-column --column-ix 1 \
    --csv-formatting-params delimiter tab \
| python -m detransliterator.tool --model-name latin2nqo_001.35 \
> tmp_detransliterated_1.nqo
```

**example: detransliterate a column from a tsv file**
```console
cat test_csv_with_header.csv \
| python -m detransliterator.csv_tool extract-column --column-ix 1 --skip-lines 1 \
| python -m detransliterator.tool --model-name latin2nqo_001.35 \
> tmp_detransliterated_2.nqo
```

**example: use a particular GPU**
```console
CUDA_VISIBLE_DEVICES="1" echo "musa dunbuya" | python -m detransliterator.tool
```

## Detransliteration Models
|Model|Source Script|Target Script|#Parameters|Validation BLEU|Test BLEU|
|:--:|:--:|:--:|--:|--:|--:|
|latin2nqo_001.35|latin|nqo|2 520 576|75.56|74.14|
|latin2nqo_001.38|latin|nqo|3 909 120|78.51|77.06|


## License

`detransliterator` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
