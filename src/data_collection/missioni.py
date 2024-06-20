import pandas as pd
from logging import getLogger
from typing import Tuple

from src.sources import PATH_MISSIONI, PATH_COMPONENTI

logger = getLogger(__name__)


def fetch_pnrr_missions() -> Tuple[pd.DataFrame, pd.DataFrame]: 
    """
    Gets PNRR missions and subcomponents out of standardized files
    """
    missioni_map = pd.read_json(PATH_MISSIONI, orient="index")
    missioni_map.columns = ["MISSIONE"]

    componenti_map = pd.read_json(PATH_COMPONENTI, orient="index") 
    componenti_map.columns = ["COMPONENTE"]

    return missioni_map, componenti_map