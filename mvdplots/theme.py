import matplotlib as mpl

from .figsize import figsize


def set_theme():
    mpl.rcParams.update(
        {
            "font.size": 8,
            "axes.facecolor": "0.95",
            "axes.linewidth": 0,
            "axes.grid": True,
            "axes.axisbelow": True,
            "axes.titlesize": "medium",
            "axes.prop_cycle": mpl.cycler(
                "color",
                [
                    "4e79a7",
                    "f28e2b",
                    "e15759",
                    "76b7b2",
                    "59a14f",
                    "edc948",
                    "b07aa1",
                    "ff9da7",
                    "9c755f",
                    "bab0ac",
                ],
            ),
            "xtick.major.size": 0,
            "xtick.minor.size": 0,
            "ytick.major.size": 0,
            "ytick.minor.size": 0,
            "grid.color": "white",
            "grid.linewidth": 0.8,
            "legend.frameon": False,
            "legend.handlelength": 0.8 * 2.0,
            "legend.numpoints": 1,
            "legend.scatterpoints": 1,
            "lines.linewidth": 1.4,
            "figure.dpi": 150,
            "figure.figsize": figsize(),
            "figure.constrained_layout.use": True,
            "image.cmap": "cividis",
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
            "patch.linewidth": 0.3,
            "patch.facecolor": "4e79a7",
            "scatter.edgecolors": "white",
        }
    )

