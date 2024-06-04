import random

import pandas as pd

from common.cleanup import cleanup_csv
from common.const import (
    DATA_DIR,
    DIVIDE_MAX,
    DIVIDE_MIN,
    LOTS_CSV_PATH,
    PERCENT,
    SEED,
    YARD_CSV_PATH,
    H,
    W,
)
from common.seed import seed_everything


def generate_lots() -> None:
    lots = []
    area_sum = 0
    while True:
        lot_height = random.randint(H // DIVIDE_MAX, H // DIVIDE_MIN)
        lot_width = random.randint(W // DIVIDE_MAX, W // DIVIDE_MIN)

        if area_sum + lot_height * lot_width > PERCENT * H * W:
            break

        lots.append(
            {
                "height": lot_height,
                "width": lot_width,
            }
        )
        area_sum += lot_height * lot_width

    lots_df = pd.DataFrame(lots)
    lots_df.to_csv(LOTS_CSV_PATH, index=False)
    print(f"Generated lots.csv with {len(lots_df)} lots in {LOTS_CSV_PATH.resolve()}.")


def generate_yard() -> None:
    yards_df = pd.DataFrame([{"height": H, "width": W}])
    yards_df.to_csv(YARD_CSV_PATH, index=False)
    print(f"Generated yard.csv with in {YARD_CSV_PATH.resolve()}.")


if __name__ == "__main__":
    seed_everything(SEED)

    cleanup_csv(DATA_DIR)

    generate_lots()
    generate_yard()
