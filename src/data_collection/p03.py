import pandas as pd

from logging import getLogger

from src.sources import P03_URL, P03_FILENAME
from src.utils import fetch_csv_from_zip


logger = getLogger(__name__)


def get_p03() -> pd.DataFrame:
    """
    Fetches P03 Dataset: Incentive Measures

    The dataset provides, for calls for tenders that use PNRR/PNC funds, 
    inclusion quotas and any exemptions to the equal opportunity regulations.
    """

    p03 = fetch_csv_from_zip(P03_URL, P03_FILENAME)

    return p03