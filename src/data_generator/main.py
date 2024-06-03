import random

import pandas as pd

from common.cleanup import cleanup_csv
from common.const import DATA_DIR, LOTS_CSV_PATH, SEED, YARD_CSV_PATH, H, N, W
from common.seed import seed_everything


def generate_lots() -> None:
    lots = []
    for _ in range(N):
        lot_height = random.randint(1, H // 3)
        lot_width = random.randint(1, W // 3)
        lots.append(
            {
                "height": lot_height,
                "width": lot_width,
            }
        )

    lots_df = pd.DataFrame(lots)
    lots_df.to_csv(LOTS_CSV_PATH, index=False)
    print(f"Generated lots.csv with {N} lots in {LOTS_CSV_PATH.resolve()}.")


def generate_yard() -> None:
    yards_df = pd.DataFrame([{"height": H, "width": W}])
    yards_df.to_csv(YARD_CSV_PATH, index=False)
    print(f"Generated yard.csv with in {YARD_CSV_PATH.resolve()}.")


if __name__ == "__main__":
    seed_everything(SEED)

    cleanup_csv(DATA_DIR)

    generate_lots()
    generate_yard()
