import pandas as pd

from logging import getLogger

from src.sources import ITALIA_DOMANI_BASE_URL, INDICATORI_UNIVERSO_REGIS_URL, INDICATORI_UNIVERSO_REGIS_FILENAME
from src.utils import fetch_csv_from_html
from src.data_processing.wrangling import conditions_gender, conditions_individuals

logger = getLogger(__name__)


def get_regis_indicators() -> pd.DataFrame:
    """
    Fetches the Common European PNRR Indicators (Regis Universe) Dataset: 

    Associates one or more common indicators with the PNRR measures (investments and reforms) 
    and with each CUP-CLP linked to the reference sub-measure, indicator description, 
    unit of measure, programmed value, and value achieved by the implementing entity. 
    
    The common indicators are regulated by Commission Delegated Regulation 2021/2106 of September 28, 2021, 
    and represent quantitative indicators common to all Member States, 
    related to the objectives of the Recovery and Resilience Facility (RRF) 
    in each of the six pillars of the RRF as outlined in Article 3 of Regulation 2021/241. 
    
    The CUP/CLP are reported independently of the submission and outcome of the validation process, 
    which is the periodic consolidation of information based 
    on the results of automatic consistency checks of the data entered into the system 
    by the Implementing Bodies and the appropriate administrative checks 
    carried out by the Administrations.
    """

    regis_comm_ind = fetch_csv_from_html(
        INDICATORI_UNIVERSO_REGIS_URL, 
        ITALIA_DOMANI_BASE_URL, 
        INDICATORI_UNIVERSO_REGIS_FILENAME
    )

    regis_comm_ind['FLG_INDICATORI_PERSONE'] = regis_comm_ind.apply(
        conditions_individuals, axis=1
    )

    regis_comm_ind['FLG_INDICATORI_GENERE'] = regis_comm_ind.apply(
        conditions_gender, axis=1
    )

    return regis_comm_ind