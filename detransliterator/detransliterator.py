from pathlib import Path

class Detransliterator():
    def __init__(self, model_name) -> None:
        self.model_name = model_name
        self._load_model()

    def _load_model(self):
        from fairseq.models.transformer import TransformerModel
        base_dir = Path(__file__).parent / "assets" / self.model_name
        self.model = TransformerModel.from_pretrained(
            str(base_dir / "checkpoints/"),
            checkpoint_file='checkpoint_best.pt',
            data_name_or_path=str(base_dir / "data"),
            bpe='subword_nmt',
            bpe_codes=str(base_dir / "data" / "bpe.code"),
            source_lang="roman",
            target_lang="nqo"
        )

    def detransliterate(self, latin, beam_size=5):
        latin = latin.lower()
        return self.model.translate(latin, beam=beam_size)
