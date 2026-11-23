import matplotlib.pyplot as plt
import pandas as pd


def plot_constellation(stars: pd.DataFrame, con: str) -> None:
    """Plot one constellation's stars, sized by brightness and labeled by name."""
    con_stars = stars[stars["con"] == con]  # Boolean mask: True where the star belongs to this constellation, then keep only those rows.
    named = con_stars[con_stars["proper"].notna()]     # Of those, keep only stars that have a proper name (proper is NaN otherwise).

    plt.scatter(
        con_stars["ra_deg"],
        con_stars["dec"],
        s=(6 - con_stars["mag"]) * 7,  # brighter (smaller mag) -> bigger dot
        c="white",
    )

    for name, x, y in zip(named["proper"], named["ra_deg"], named["dec"]):
        plt.text(x, y + 0.5, name, fontsize=8)

    plt.gca().invert_xaxis()  # sky maps show east (increasing RA) on the left
    plt.xlabel("Right ascension (deg)")
    plt.ylabel("Declination (deg)")
    plt.title(f"{con}: naked-eye stars (mag ≤ 6)")