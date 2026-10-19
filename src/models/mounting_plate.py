
from pathlib import Path

from build123d import (
    Align,
    Axis,
    Box,
    BuildPart,
    CounterSinkHole,
    Locations,
    export_step,
    export_stl,
    fillet,
)
from ocp_vscode import show

# Design parameters: millimeters
LENGTH = 100.0
WIDTH = 60.0
THICKNESS = 8.0

CORNER_RADIUS = 3.0
EDGE_OFFSET = 10.0
HOLE_DIAMETER = 5.0
SINK_DIAMETER = 9.0
SINK_ANGLE = 90.0

ROOT = Path(__file__).resolve().parents[0]
OUTPUT = ROOT / "build"


def make_part():
    """Create a rounded mounting plate with four countersunk holes."""
    if min(LENGTH, WIDTH, THICKNESS) <= 0:
        raise ValueError("Dimensions must be positive.")

    if not 0 < EDGE_OFFSET < min(LENGTH, WIDTH) / 2:
        raise ValueError("Invalid hole edge offset.")

    if not 0 < CORNER_RADIUS < min(LENGTH, WIDTH) / 2:
        raise ValueError("Invalid corner radius.")

    if not 0 < HOLE_DIAMETER < SINK_DIAMETER:
        raise ValueError("Invalid hole/countersink diameters.")

    x = LENGTH / 2 - EDGE_OFFSET
    y = WIDTH / 2 - EDGE_OFFSET

    positions = [
        (-x, -y, THICKNESS),
        (-x, y, THICKNESS),
        (x, -y, THICKNESS),
        (x, y, THICKNESS),
    ]

    with BuildPart() as plate:
        Box(
            LENGTH,
            WIDTH,
            THICKNESS,
            align=(Align.CENTER, Align.CENTER, Align.MIN),
        )

        fillet(plate.edges().filter_by(Axis.Z), radius=CORNER_RADIUS)

        with Locations(*positions):
            CounterSinkHole(
                radius=HOLE_DIAMETER / 2,
                counter_sink_radius=SINK_DIAMETER / 2,
                counter_sink_angle=SINK_ANGLE,
            )

    return plate.part


def main():
    part = make_part()
    OUTPUT.mkdir(parents=True, exist_ok=True)

    export_step(part, str(OUTPUT / "mounting_plate.step"))
    export_stl(
        part,
        str(OUTPUT / "mounting_plate.stl"),
        tolerance=0.05,
        angular_tolerance=0.1,
    )

    show(part)
    print(f"Exports written to {OUTPUT}")


if __name__ == "__main__":
    main()
