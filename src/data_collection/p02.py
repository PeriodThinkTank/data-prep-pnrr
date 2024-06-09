import pandas as pd

from logging import getLogger

from src.sources import P02_URL, P02_FILENAME
from src.utils import fetch_csv_from_zip


logger = getLogger(__name__)


def get_p02() -> pd.DataFrame:

    """
    Fetches P02 Dataset: CUPs Registry
    """
    logger.info("Fetching P02..")

    try:
        p01 = fetch_csv_from_zip(
            url=P02_URL,
            csv_filename=P02_FILENAME,
            separator=";",
            na_values=["NA", "ND"]
        )

        logger.info("Done fetching P02 Dataset")
        return p01
    
    except Exception as e:
        logger.error(f"Error fetching P02 Dataset: {e}")