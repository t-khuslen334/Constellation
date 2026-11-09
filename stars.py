import pandas as pd

COLUMNS = ["id", "hip", "proper", "ra_deg", "dec", "mag", "con"]


def load_stars(path: str, max_mag: float = 6.0) -> pd.DataFrame:
    
    """Load the HYG catalog and return stars brighter than max_mag, with RA in degrees."""
    df = pd.read_csv(path)
    df["ra_deg"] = df["ra"] * 15          # RA: hours -> degrees (1 h = 15°)

    is_star = df["id"] != 0                # exclude the Sun
    is_visible = df["mag"] <= max_mag      # exclude stars too faint to see

    return df.loc[is_star & is_visible, COLUMNS]
