import random

from optimizer.data_structure.state import State


def insert(state: State) -> State:
    i = random.randint(0, len(state.lots) - 2)
    j = random.randint(i + 1, len(state.lots) - 1)
    lot = state.lots.pop(i)
    state.lots.insert(j, lot)
    return state
