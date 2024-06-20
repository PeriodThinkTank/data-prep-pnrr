import pandas as pd

from logging import getLogger

from src.sources import ITALIA_DOMANI_BASE_URL, INDICATORI_SDG_URL, INDICATORI_SDG_FILENAME
from src.utils import fetch_csv_from_html

logger = getLogger(__name__)


def get_indicators_and_sdg() -> pd.DataFrame:
    """
    Fetches the Indicators&SDG Dataset.  

    The dataset provides details of the monitoring framework prepared along with 
    the values of the identified Well-being/Sustainability (BES) statistical indicators. 
    
    The dataset presents the entire overview of the connections between 
    the measures and sub-measures of the PNRR with the well-being and sustainability 
    indicators and their placement within the SDG framework of the 2030 agenda, 
    as a result of the collaboration between ISTAT and MEF RGS.
    """

    indicators_sdg = fetch_csv_from_html(
        INDICATORI_SDG_URL, 
        ITALIA_DOMANI_BASE_URL, 
        INDICATORI_SDG_FILENAME
    )

    return indicators_sdg