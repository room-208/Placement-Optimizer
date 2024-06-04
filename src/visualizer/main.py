from math import ceil
from pathlib import Path

import matplotlib.animation as animation
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from common.cleanup import cleanup_gif
from common.const import ANIMATION_GIT_PATH, DIVIDE_MIN, OUTPUTS_DIR, H, W
from visualizer.reader import merge_all_placements_df


def vizualize_gif() -> None:
    all_placements_df = merge_all_placements_df()

    fig, ax = plt.subplots()

    rest_num = 0

    def update(stage: int) -> None:
        global rest_num

        if pd.isna(all_placements_df.at[stage, "width"]):
            ax.clear()
            rest_num = 0

            ax.set_title(
                f"Loss Area = {int(all_placements_df.at[stage, 'loss_area'])}, Stage = {int(all_placements_df.at[stage, 'stage'])}"
            )
            ax.set_xlim(0, 2 * W)
            ax.set_ylim(0, H)
            ax.set_aspect("equal")

            box = patches.Rectangle(
                (0, 0), W, H, edgecolor="black", facecolor="red", alpha=0.1
            )
            ax.add_patch(box)
        else:
            if pd.isna(all_placements_df.at[stage, "x"]):
                if (
                    all_placements_df.at[stage, "width"]
                    > all_placements_df.at[stage, "height"]
                ):
                    (
                        all_placements_df.at[stage, "width"],
                        all_placements_df.at[stage, "height"],
                    ) = (
                        all_placements_df.at[stage, "height"],
                        all_placements_df.at[stage, "width"],
                    )
                center_x = (rest_num % DIVIDE_MIN + 0.5) * (W / DIVIDE_MIN)
                center_y = (rest_num // DIVIDE_MIN + 0.5) * (H / DIVIDE_MIN)
                all_placements_df.at[stage, "x"] = (
                    center_x - (all_placements_df.at[stage, "width"] / 2) + W
                )
                all_placements_df.at[stage, "y"] = center_y - (
                    all_placements_df.at[stage, "height"] / 2
                )
                rest_num += 1

            rect = patches.Rectangle(
                (
                    all_placements_df.at[stage, "x"],
                    all_placements_df.at[stage, "y"],
                ),
                all_placements_df.at[stage, "width"],
                all_placements_df.at[stage, "height"],
                edgecolor="black",
                facecolor="blue",
            )
            ax.add_patch(rect)

            ax.text(
                int(all_placements_df.at[stage, "x"])
                + int(all_placements_df.at[stage, "width"]) / 2,
                int(all_placements_df.at[stage, "y"])
                + int(all_placements_df.at[stage, "height"]) / 2,
                str(int(all_placements_df.at[stage, "order"])),
                ha="center",
                va="center",
                fontsize=10,
                color="white",
            )

    ani = animation.FuncAnimation(fig, update, frames=len(all_placements_df))

    ani.save(ANIMATION_GIT_PATH)

    plt.tight_layout()
    plt.show()

    print(f"Generated animation.gif in {ANIMATION_GIT_PATH.resolve()}.")


if __name__ == "__main__":
    cleanup_gif(OUTPUTS_DIR)

    vizualize_gif()
