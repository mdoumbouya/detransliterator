build:
	flake8 detransliterator --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
	flake8 tests --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
	rm -rf dist
	hatch build

test:
	pytest -s

publish:
	hatch publish

test-csv-tools:
	cat detransliterator/assets/test_data/test_csv_with_header.csv \
	| python -m detransliterator.csv_tool \
		extract-column --column-ix 1 --skip-lines 1 \
	> tmp_col1.txt

	cat detransliterator/assets/test_data/test_csv_no_header.csv \
	| python -m detransliterator.csv_tool \
		extract-column --column-ix 1 \
	> tmp_col2.txt

	cat detransliterator/assets/test_data/test_tsv_with_header.tsv \
	| python -m detransliterator.csv_tool \
		extract-column --column-ix 1 --skip-lines 1 --csv-formatting-params delimiter tab \
	> tmp_col3.txt

	cat detransliterator/assets/test_data/test_tsv_no_header.tsv \
	| python -m detransliterator.csv_tool \
		extract-column --column-ix 1 --csv-formatting-params delimiter tab \
	> tmp_col4.txt

	# raise error if files are not the same
	diff tmp_col1.txt tmp_col2.txt
	diff tmp_col1.txt tmp_col3.txt
	diff tmp_col1.txt tmp_col4.txt

	rm tmp_col1.txt tmp_col2.txt tmp_col3.txt tmp_col4.txt

test-extract-and-detransliterate_latin2nqo_001.35:
	cat detransliterator/assets/test_data/test_tsv_no_header.tsv \
	| python -m detransliterator.csv_tool extract-column --column-ix 1 \
		--csv-formatting-params delimiter tab \
	| python -m detransliterator.tool --model-name latin2nqo_001.35 \
	> tmp_detransliterated_1.nqo

	cat detransliterator/assets/test_data/test_csv_with_header.csv \
	| python -m detransliterator.csv_tool extract-column --column-ix 1 --skip-lines 1 \
	| python -m detransliterator.tool --model-name latin2nqo_001.35 \
	> tmp_detransliterated_2.nqo

	diff tmp_detransliterated_1.nqo tmp_detransliterated_2.nqo
	rm tmp_detransliterated_1.nqo tmp_detransliterated_2.nqo

test-extract-and-detransliterate_latin2nqo_001.38:
	cat detransliterator/assets/test_data/test_tsv_no_header.tsv \
	| python -m detransliterator.csv_tool extract-column --column-ix 1 \
		--csv-formatting-params delimiter tab \
	| python -m detransliterator.tool --model-name latin2nqo_001.38 \
	> tmp_detransliterated_1.nqo

	cat detransliterator/assets/test_data/test_csv_with_header.csv \
	| python -m detransliterator.csv_tool extract-column --column-ix 1 --skip-lines 1 \
	| python -m detransliterator.tool --model-name latin2nqo_001.38 \
	> tmp_detransliterated_2.nqo

	diff tmp_detransliterated_1.nqo tmp_detransliterated_2.nqo
	rm tmp_detransliterated_1.nqo tmp_detransliterated_2.nqo