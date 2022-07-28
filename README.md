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

detransliterator = Detransliterator('latin2nqo_001.38')
for latin in ["maari", "mààri", "magari", "màgàri", "makari", "màkàri"]:
    nqo = detransliterator.detransliterate(latin, beam_size=5)
    assert nqo == "ߡߊ߰ߙߌ"
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
> tmp_col1_1.txt
```

**example: extract a column from  a tsv file**
```console
cat test_tsv_with_header.tsv \
| python -m detransliterator.csv_tool \
    extract-column --column-ix 1 --skip-lines 1 --csv-formatting-params delimiter tab \
> tmp_col1_2.txt
```


**example: detransliterate a column from a csv file**
```console
cat test_csv_with_header.csv \
| python -m detransliterator.csv_tool extract-column --column-ix 1 --skip-lines 1 \
| python -m detransliterator.tool --model-name latin2nqo_001.35 \
> tmp_col_1_detransliterated_1.nqo
```

**example: detransliterate a column from a tsv file**
```console
cat test_tsv_no_header.tsv \
| python -m detransliterator.csv_tool extract-column --column-ix 1 \
    --csv-formatting-params delimiter tab \
| python -m detransliterator.tool --model-name latin2nqo_001.35 \
> tmp_col_1_detransliterated_2.nqo
```

**example: use a particular GPU**
```console
CUDA_VISIBLE_DEVICES="1" echo "musa dunbuya" | python -m detransliterator.tool
```

## latin2nqo Detransliteration Models
|Model|Source Script|Target Script|#Parameters|Validation BLEU|Test BLEU|
|:--:|:--:|:--:|--:|--:|--:|
|latin2nqo_001.35|latin|nqo|2 520 576|75.56|74.14|
|latin2nqo_001.38|latin|nqo|3 909 120|78.51|77.06|

### Supported variants of latin transliterations
|variant|example latin|detransliterated nqo|
|:--|:--:|:--:|
|maninka | maari | ߡߊ߰ߙߌ |
|maninka tonal | mààri| ߡߊ߰ߙߌ |
|bambara-ga | magari| ߡߊ߰ߙߌ |
|bambara-ga tonal | màgàri| ߡߊ߰ߙߌ |
|bambara-ka | makari| ߡߊ߰ߙߌ |
|bambara-ka tonal | màkàri| ߡߊ߰ߙߌ |


## License

`detransliterator` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

If you use this software in your work, please cite it using the following metadata:
```
@software{Doumbouya_Detransliterator_2022,
    author = {Doumbouya, Moussa},
    month = {7},
    title = {{Detransliterator}},
    url = {https://github.com/mdoumbouya/detransliterator},
    version = {0.0.2},
    year = {2022}
}
```
