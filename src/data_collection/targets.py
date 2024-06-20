import pandas as pd

from logging import getLogger

from src.sources import ITALIA_DOMANI_BASE_URL, TARGETS_URL, TARGETS_FILE_NAME
from src.utils import fetch_csv_from_html

logger = getLogger(__name__)


def get_targets() -> pd.DataFrame:
    """
    Fetches the Dataset Target Indicators

    The dataset associates a target indicator with 
    each CUP/CLP code related to the reference sub-measure of the PNRR, 
    including information on the indicator description, unit of measure, 
    programmed value, and achieved value. 
    
    The Target Indicators concern the contribution of each project, 
    in terms of physical and procedural progress, to the national and European 
    level targets of the measure that finances it, as identified in the 
    Annex to the Council Decision of December 8, 2023, which revises the 
    Decision of July 13, 2021. 

    Validation is the periodic consolidation of information related to the physical, 
    procedural, and financial progress of the projects present on the ReGiS platform, 
    based on the results of automatic consistency checks of the data entered 
    into the system by the Implementing Bodies and the appropriate administrative 
    checks carried out by the Administrations.
    
    CUP: Codice Unico di progetto
    CLP: Codice Locale di progetto 
    """

    targets = fetch_csv_from_html(
        TARGETS_URL, 
        ITALIA_DOMANI_BASE_URL, 
        TARGETS_FILE_NAME
    )

    return targets