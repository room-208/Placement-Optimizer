import random

from optimizer.data_structure.state import State


def swap(state: State) -> State:
    i = random.randint(0, len(state.lots) - 2)
    j = random.randint(i + 1, len(state.lots) - 1)
    state.lots[i], state.lots[j] = state.lots[j], state.lots[i]
    return state
