import pandas as pd

from common.const import LOTS_CSV_PATH, PLACEMENTS_CSV_PATH


def make_merged_placements_df(stage: int) -> tuple[pd.DataFrame, pd.DataFrame]:
    lots_df = pd.read_csv(LOTS_CSV_PATH)
    placements_df = pd.read_csv(PLACEMENTS_CSV_PATH(stage))
    merged_df = pd.merge(lots_df, placements_df, left_index=True, right_index=True)
    can_placements_df = merged_df[~merged_df["x"].isnull()].reset_index(drop=True)
    cannot_placements_df = merged_df[merged_df["x"].isnull()].reset_index(drop=True)
    return can_placements_df, cannot_placements_df