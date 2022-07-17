from pathlib import Path
from fairseq.models.transformer import TransformerModel



def get_model_by_name(model_name):
    base_dir = Path(__file__).parent / "assets" / model_name
    model = TransformerModel.from_pretrained(
        str(base_dir / "checkpoints/"),
        checkpoint_file='checkpoint_best.pt',
        data_name_or_path=str(base_dir / "data" ),
        bpe='subword_nmt',
        bpe_codes=str(base_dir / "data" / "bpe.code"),
        source_lang="roman",
        target_lang="nqo"
    )
    return model
