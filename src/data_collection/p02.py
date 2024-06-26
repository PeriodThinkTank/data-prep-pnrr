import pandas as pd

from logging import getLogger

from src.sources import P02_URL, P02_FILENAME, P02_SHEET_NAME
from src.utils import fetch_excel_from_zip


logger = getLogger(__name__)


def get_p02() -> pd.DataFrame:

    """
    Fetches the P02 Dataset.
    """
    logger.info("Fetching P02..")

    try:
        # TODO this is an excel, not a csv
        p02 = fetch_excel_from_zip(
            url=P02_URL,
            xlsx_filename=P02_FILENAME,
            sheet_name=P02_SHEET_NAME,
            na_values=["NA", "ND"]
        )

        logger.info("Done fetching P02 Dataset")
        return p02
    
    except Exception as e:
        logger.error(f"Error fetching P02 Dataset: {e}")