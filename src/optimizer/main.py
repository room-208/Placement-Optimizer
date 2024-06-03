import random

from common.cleanup import cleanup_csv
from common.const import OUTPUTS_DIR, SEED
from common.seed import seed_everything
from optimizer.data_structure.state import State
from optimizer.packing.bottom_left import bottom_left

if __name__ == "__main__":
    seed_everything(SEED)

    cleanup_csv(OUTPUTS_DIR)

    state = State()
    state = bottom_left(state)
    state.writePlacements()
