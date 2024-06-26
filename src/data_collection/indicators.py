import pandas as pd

from logging import getLogger

from src.sources import ITALIA_DOMANI_BASE_URL, INDICATORI_URL, INDICATORI_FILENAME
from src.utils import fetch_csv_from_html

logger = getLogger(__name__)


def get_indicators() -> pd.DataFrame:
    """
    Fetches the Indicators Dataset: 

    Contains the measures and sub-measures (reference units), along with their detailed registry.  

    For each measure/sub-measure, the description and identification codes 
    are provided, which allow identification across different reference systems, 
    along with the description and identification code of the mission and the component.  

    Each measure and sub-measure is associated with its own common indicators, 
    broken down into various sub-categories, as described in the Circular 
    34/2022 RGS ("Linee guida metodologiche per la rendicontazione degli Indicatori Comuni del Pnrr”)
    """

    indicators = fetch_csv_from_html(
        INDICATORI_URL, 
        ITALIA_DOMANI_BASE_URL, 
        INDICATORI_FILENAME
    )
    
    return indicators