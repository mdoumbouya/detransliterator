from datetime import datetime
from pathlib import Path

def get_log_filename(prefix):
    logdir = Path('logs')
    logdir.mkdir(parents=True, exist_ok=True)
    date = datetime.utcnow().isoformat()
    date = date.replace(":", "-")
    return str(logdir / f"{prefix}_{date}.log")

    