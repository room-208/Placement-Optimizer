import pandas as pd

from common.const import PLACEMENTS_CSV_PATH


def make_placements_df(stage: int) -> tuple[pd.DataFrame, pd.DataFrame]:
    placements_df = pd.read_csv(PLACEMENTS_CSV_PATH(stage))
    can_placements_df = placements_df[~placements_df["x"].isnull()].reset_index(
        drop=True
    )
    cannot_placements_df = placements_df[placements_df["x"].isnull()].reset_index(
        drop=True
    )
    return can_placements_df, cannot_placements_df
