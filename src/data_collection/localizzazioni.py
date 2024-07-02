import pandas as pd

from logging import getLogger

from src.sources import LOC_URL, LOC_FILENAME
from src.utils import fetch_csv_from_zip


logger = getLogger(__name__)


def get_localizzazioni() -> pd.DataFrame:

    """
    Fetches the Localizations Dataset
    """
    logger.info("Fetching P02..")

    try:
        localizzazioni_cap = fetch_csv_from_zip(
            url=LOC_URL,
            csv_filename=LOC_FILENAME,
            separator=";",
            na_values=["NA", "ND"]
        )

        logger.info("Done fetching Localizzazioni Dataset")
        return localizzazioni_cap
    
    except Exception as e:
        logger.error(f"Error fetching P02 Dataset: {e}")