import random
from copy import deepcopy

from common.cleanup import cleanup_csv
from common.const import OUTPUTS_DIR, SEED
from common.seed import seed_everything
from optimizer.data_structure.state import State
from optimizer.neighborhood.insert import insert
from optimizer.neighborhood.rotate import rotate
from optimizer.neighborhood.swap import swap
from optimizer.packing.bottom_left import bottom_left

if __name__ == "__main__":
    seed_everything(SEED)

    cleanup_csv(OUTPUTS_DIR)

    state = State()
    state = bottom_left(state)
    state.computeScore()
    state.writePlacements()

    for _ in range(1000):
        r = random.randint(0, 2)
        new_state = deepcopy(state)
        if r == 0:
            new_state = insert(new_state)
        elif r == 1:
            new_state = rotate(new_state)
        elif r == 2:
            new_state = swap(new_state)

        new_state.computeScore()

        if new_state.score > state.score:
            state = deepcopy(new_state)
            state.writePlacements()
