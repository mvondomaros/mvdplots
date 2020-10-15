import matplotlib as mpl


class State:
    journal = None
    rc_params = None

    __init__ = None


ASPECT_RATIO = 5/4
FIGURE_WIDTHS = {"jpcb": {"single": 3.33, "double": 7}}


def figsize(width="single", height=1.0):
    width = FIGURE_WIDTHS[State.journal][width]
    height *= FIGURE_WIDTHS[State.journal]["single"] / ASPECT_RATIO
    return (width, height)


def set_journal(journal="jpcb"):
    State.journal = journal
    mpl.rcParams["figure.figsize"] = figsize()


def set_theme():
    if State.rc_params is None:
        State.rc_params = mpl.rcParams.copy()

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
            "figure.dpi": 126,
            "figure.constrained_layout.use": True,
            "image.cmap": "cividis",
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
            "patch.linewidth": 0.3,
            "patch.facecolor": "4e79a7",
        }
    )

    set_journal()


def unset_theme():
    if State.original_rc_params is not None:
        mpl.rcParams = State.rc_params
        State.rc_params = None