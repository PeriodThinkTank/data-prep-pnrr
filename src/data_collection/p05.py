import pandas as pd

from logging import getLogger

from src.sources import P05_URLs
from src.utils import fetch_csvs_from_url


logger = getLogger(__name__)


def get_p05() -> pd.DataFrame:
    """
    Fetches P05 Dataset: CIGs Registry. 
    The Dataset contains all procurement information published 
    in the year 2023 and 2024.

    CIG: Codice Identificativo Gara
    """

    logger.info("Fetching P05..")

    p05 = pd.DataFrame()

    for year, url in P05_URLs.items():
        try:
            year_df = fetch_csvs_from_url(
                url=url,
                files_title="cig_csv",
                separator=";",
            )

            year_df = year_df[year_df['FLAG_PNRR_PNC']=='1']
            
            p05 = pd.concat([p05, year_df], ignore_index=True, sort=False)

            logger.info(f"Done fetching {year} data")

        except Exception as e:
            logger.error(f"Error fetching data for year {year}: {e}")
   
    p05.drop_duplicates()
    for year in P05_URLs.keys():
        logger.info(
            f"Number of published CIG in {year}: {p05[p05['data_pubblicazione'].str.match(str(year))]['data_pubblicazione'].shape[0]}"
        )
    
    return p05

