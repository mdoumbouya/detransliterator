from detransliterator import Detransliterator
import pytest


@pytest.fixture
def detransliterators():
    return [
        Detransliterator('latin2nqo_001.35'),
        Detransliterator('latin2nqo_001.38')
    ]


def test_01(detransliterators):
    for detransliterator in detransliterators:
        latin = "musa dunbuya"
        reference_nqo = "ߡߎߛߊ߫ ߘߎ߲ߓߎߦߊ"
        nqo = detransliterator.detransliterate(latin, beam_size=5)
        assert reference_nqo == nqo


def test_02(detransliterators):
    for detransliterator in detransliterators:
        latins = ["musa dunbuya", "Musa Dunbuya"]
        reference_nqo = "ߡߎߛߊ߫ ߘߎ߲ߓߎߦߊ"
        nqos = [
            detransliterator.detransliterate(latin, beam_size=5)
            for latin in latins
        ]
        assert len(set(nqos)) == 1, "incorrect upper case handling"
        assert reference_nqo == nqos[0]
