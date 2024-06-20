""" Used to collect and wrangle data for Period's PNRR Web App"""
import pandas as pd
from logging import getLogger

from src.data_collection.comuni import fetch_dataset_comuni
from src.data_collection.indicators import get_indicators
from src.data_collection.indicators_sdg import get_indicators_and_sdg 
from src.data_collection.missioni import fetch_pnrr_missions
from src.data_collection.p01 import get_p01
from src.data_collection.p02 import get_p02
from src.data_collection.p05 import get_p05
from src.data_collection.targets import get_targets

logger = getLogger(__name__)

if __name__ == "__main__":

    logger.info("Starting getting datasets; this may take a while..")

    p01 = get_p01()

    p02 = get_p02()

    p05 = get_p05()

    comuni = fetch_dataset_comuni()

    missions = fetch_pnrr_missions()

    indicators = get_indicators()

    indicators_sdg = get_indicators_and_sdg()

    targets = get_targets()

    logger.info("Done fetching datasets, now we'll merge them..")

    # code to merge, join etc to create the master table

    data_final = pd.DataFrame()
    data_final.to_parquet("base_dati.parquet")
    
    logger.info("Master Table saved.")

