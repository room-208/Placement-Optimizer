import random

from optimizer.data_structure.state import State


def rotate(state: State) -> State:
    i = random.randint(0, len(state.lots) - 1)
    state.lots[i].height, state.lots[i].width = (
        state.lots[i].width,
        state.lots[i].height,
    )
    return state
