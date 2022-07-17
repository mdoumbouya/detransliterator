from latin2nqo import latin2nqo

def test_01():
    model = latin2nqo.get_model_by_name('001.35')
    latin = "musa dunbuya"
    reference_nqo = "ߡߎߛߊ߫ ߘߎ߲ߓߎߦߊ"
    nqo = model.translate(latin, beam=5)
    assert reference_nqo == nqo