from common.const import N
from optimizer.data_structure.state import State


def bottom_left(state: State) -> State:
    for i in range(N):
        bottom_left_points = []
        candidates = make_bottom_left_candidates(i, state)

        for point in candidates:
            if is_feasible_point(i, point, state):
                bottom_left_points.append(point)

        if len(bottom_left_points) == 0:
            state.lots[i].x, state.lots[i].y = None, None
        else:
            bottom_left_point = min(bottom_left_points, key=lambda v: (v[1], v[0]))
            state.lots[i].x, state.lots[i].y = bottom_left_point

    return state


def make_bottom_left_candidates(i: int, state: State) -> list[tuple[int, int]]:
    candidates = [(0, 0)]
    for j in range(i):
        for k in range(j):
            if state.lots[j].isPlaced() and state.lots[k].isPlaced():
                candidates.append(
                    (
                        state.lots[k].x + state.lots[k].width,
                        state.lots[j].y + state.lots[j].height,
                    )
                )
                candidates.append(
                    (
                        state.lots[j].x + state.lots[j].width,
                        state.lots[k].y + state.lots[k].height,
                    )
                )
    for j in range(i):
        if state.lots[j].isPlaced():
            candidates.append((0, state.lots[j].y + state.lots[j].height))
            candidates.append((state.lots[j].x + state.lots[j].width, 0))

    return candidates


def is_feasible_point(i: int, point: tuple[int, int], state: State) -> bool:
    if (
        point[0] + state.lots[i].width > state.yard.width
        or point[1] + state.lots[i].height > state.yard.height
    ):
        return False
    for j in range(i):
        if state.lots[j].isPlaced():
            continue
        if not (
            point[0] + state.lots[i].width <= state.lots[j].x
            or point[0] >= state.lots[j].x + state.lots[j].width
            or point[1] + state.lots[i].height <= state.lots[j].y
            or point[1] >= state.lots[j].y + state.lots[j].height
        ):
            return False
    return True
