from pathlib import Path

import numpy as np
import pandas as pd

from common.const import OUTPUTS_DIR


def merge_all_placements_df() -> pd.DataFrame:
    all_placements_df = []

    paths = list(OUTPUTS_DIR.glob("placements_stage_*.csv"))
    paths.sort()

    for i, path in enumerate(paths):
        placements_df = pd.read_csv(path)

        nan_row = pd.DataFrame(
            [[np.nan] * len(placements_df.columns)],
            columns=placements_df.columns,
        )
        placements_df = pd.concat([nan_row, placements_df], ignore_index=True)

        placements_df["area"] = placements_df["width"] * placements_df["height"]
        placements_df["sum_area"] = np.sum(placements_df["area"])
        placements_df["loss_area"] = np.sum(placements_df["area"]) - np.sum(
            placements_df[~placements_df["x"].isnull()]["area"]
        )

        placements_df["stage"] = i

        all_placements_df.append(placements_df)

    all_placements_df = pd.concat(all_placements_df).reset_index(drop=True)

    return all_placements_df
