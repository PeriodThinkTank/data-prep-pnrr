import pandas as pd

from logging import getLogger

from src.sources import P01_URL, P01_FILENAME
from src.utils import fetch_csv_from_zip


logger = getLogger(__name__)


def get_p01() -> pd.DataFrame:

    """
    Fetches P01 Dataset: Linking CIGs and CUPs
    """
    logger.info("Fetching P01..")

    try:
        p01 = fetch_csv_from_zip(
            url=P01_URL,
            csv_filename=P01_FILENAME,
            separator=";",
            na_values=["NA", "ND"]
        )

        logger.info("Done fetching P01 Dataset")
        return p01
    
    except Exception as e:
        logger.error(f"Error fetching P01 Dataset: {e}")

    
