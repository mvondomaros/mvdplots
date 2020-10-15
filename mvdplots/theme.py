import matplotlib as mpl


class State:
    journal = None
    rc_params = None

    __init__ = None


FIGSIZES = {"jpc": (3.25, 0.8 * 3.25)}


def set_gridsize(rows=1, cols=1):
    if State.journal is None:
        figsize = mpl.rcParams["figure.figsize"]
    else:
        figsize = FIGSIZES[State.journal]
    mpl.rcParams["figure.figsize"] = (rows * figsize[0], cols * figsize[1])


def set_theme(journal="jpc"):
    if State.rc_params is None:
        State.rc_params = mpl.rcParams

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
            "figure.figsize": FIGSIZES[journal],
            "figure.constrained_layout.use": True,
            "image.cmap": "cividis",
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
            "patch.linewidth": 0.3,
            "patch.facecolor": "4e79a7",
        }
    )


def unset_theme():
    if State.original_rc_params is not None:
        mpl.rcParams = State.rc_params
        State.rc_params = None