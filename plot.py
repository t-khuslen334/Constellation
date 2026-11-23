import matplotlib.pyplot as plt
import pandas as pd


def wrap_ra(ra: pd.Series) -> pd.Series:
    """Shift RA > 180° to negative so constellations crossing 0°/360° stay together."""
    # e.g. 350° -> -10°: same direction on the sky, but now next to 0°
    return ra.mask(ra > 180, ra - 360)


def plot_constellation(stars: pd.DataFrame, lines: dict, con: str) -> None:
    """Plot one constellation: lines, stars sized by brightness, and star names."""
    # Stars inside this constellation's border
    con_stars = stars[stars["con"] == con]

    # Lookup table by Hipparcos number (the line data uses HIP numbers)
    by_hip = stars.set_index("hip")

    # RA is a circle: a constellation spanning > 180° must cross the 0°/360° seam
    ra = con_stars["ra_deg"]
    if ra.max() - ra.min() > 180:
        con_stars = con_stars.assign(ra_deg=wrap_ra(con_stars["ra_deg"]))
        by_hip = by_hip.assign(ra_deg=wrap_ra(by_hip["ra_deg"]))

    # Built after the RA fix so labels move with their stars
    named = con_stars[con_stars["proper"].notna()]

    # Lines first, so the dots are drawn on top of them
    for path in lines[con]:
        coords = by_hip.loc[path, ["ra_deg", "dec"]]  # stars in drawing order
        plt.plot(coords["ra_deg"], coords["dec"], color="gray", linewidth=1)

    plt.scatter(
        con_stars["ra_deg"],
        con_stars["dec"],
        s=(6 - con_stars["mag"]) * 7,  # smaller mag = brighter -> bigger dot
        c="white",
    )

    # Name label slightly above each named star
    for name, x, y in zip(named["proper"], named["ra_deg"], named["dec"]):
        plt.text(x, y + 0.5, name, fontsize=8)

    plt.gca().invert_xaxis()  # looking up at the sky, east (larger RA) is on the left
    plt.xlabel("Right ascension (deg)")
    plt.ylabel("Declination (deg)")
    plt.title(f"{con}: naked-eye stars (mag ≤ 6)")