from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"

DEFAULT_KNOWLEDGE_BASE = (
    DATA_DIR / "knowledge_base.json"
)

DEFAULT_TOP_K = 3

ESCALATION_THRESHOLD = 0.18
