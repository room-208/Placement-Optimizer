import pandas as pd

from common.const import LOTS_CSV_PATH, PLACEMENTS_CSV_PATH, YARD_CSV_PATH
from optimizer.data_structure.lot import Lot
from optimizer.data_structure.yard import Yard


class State:
    def __init__(self) -> None:
        self.lots: list[Lot]
        self.readLots()

        self.yard: Yard
        self.readYards()

        self.stage = 0

    def readLots(self) -> None:
        df = pd.read_csv(LOTS_CSV_PATH)
        self.lots = [Lot(row["height"], row["width"], M) for _, row in df.iterrows()]

    def readYards(self) -> None:
        df = pd.read_csv(YARD_CSV_PATH)
        self.yards = [Yard(row["height"], row["width"]) for _, row in df.iterrows()]

    def writePlacements(self) -> None:
        placements = []
        for lot in self.lots:
            if (lot.x is not None) and (lot.y is not None):
                placement = {"x": lot.x, "y": lot.y}
                placements.append(placement)

        placements_df = pd.DataFrame(placements)
        placements_df.to_csv(PLACEMENTS_CSV_PATH(self.stage), index=False)
        print(
            f"Generated placements_stage_{self.stage}.csv in {PLACEMENTS_CSV_PATH(self.stage).resolve()}."
        )

        self.stage += 1
