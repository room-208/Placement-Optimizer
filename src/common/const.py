from pathlib import Path

COMMON_DIR = Path(__file__).resolve().parent

ROOT_DIR = COMMON_DIR.parents[1]

DATA_DIR = ROOT_DIR / "data"
SRC_DIR = ROOT_DIR / "src"
OUTPUTS_DIR = ROOT_DIR / "outputs"

LOTS_CSV_PATH = DATA_DIR / "lots.csv"
YARD_CSV_PATH = DATA_DIR / "yard.csv"

PLACEMENTS_CSV_PATH = (
    lambda stage: OUTPUTS_DIR / f"placements_stage_{str(stage).zfill(4)}.csv"
)
ANIMATION_GIT_PATH = OUTPUTS_DIR / "animation.gif"

SEED = 0
N = 50
H = 50
W = 30
