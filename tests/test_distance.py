import polars as pl
from polars_geodesic_distance import distance


def test_piglatinnify():
    df = pl.DataFrame(
        {
            "lat_a": [52.518992275104445, 52.518992275104445, 52.518992275104445, 52.518992275104445, 52.518992275104445, 52.518992275104445, 52.518992275104445, 52.518992275104445, 52.518992275104445, 52.518992275104445],
            "lng_a": [13.404800164623978, 13.404800164623978, 13.404800164623978, 13.404800164623978, 13.404800164623978, 13.404800164623978, 13.404800164623978, 13.404800164623978, 13.404800164623978, 13.404800164623978],
            "lat_b": [48.140313048369265, 48.140313048369265, 48.140313048369265, 48.140313048369265, 48.140313048369265, 48.140313048369265, 48.140313048369265, 48.140313048369265, 48.140313048369265, 48.140313048369265],
            "lng_b": [11.563939007231188, 11.563939007231188, 11.563939007231188, 11.563939007231188, 11.563939007231188, 11.563939007231188, 11.563939007231188, 11.563939007231188, 11.563939007231188, 11.563939007231188],
        }
    )
    df = df.with_columns(distance=distance("lat_a", "lng_a", "lat_b", "lng_b"))

    assert round(df["distance"][0]) == round(504347.6524)