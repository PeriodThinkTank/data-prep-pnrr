import pandas as pd

from logging import getLogger

from src.sources import P04_URL, P04_FILENAME
from src.utils import fetch_csv_from_zip


logger = getLogger(__name__)


def get_p04() -> pd.DataFrame:
    """
    Fetches P04 Dataset: Quotas and Exemptions

    The dataset provides, for calls for tenders that use PNRR/PNC funds, 
    inclusion quotas and any exemptions to the equal opportunity regulations.
    """

    p04 = fetch_csv_from_zip(P04_URL, P04_FILENAME)

    return p04