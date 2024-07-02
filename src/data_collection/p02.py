import pandas as pd

from logging import getLogger

from src.sources import P02_URL, P02_FILENAME, ITALIA_DOMANI_BASE_URL
from src.utils import fetch_csv_from_html


logger = getLogger(__name__)


def get_p02() -> pd.DataFrame:

    """
    Fetches the P02 Dataset.  

    The dataset PNRR Projects - ReGiS Universe provides, 
    for each measure or sub-measure of the Plan, the complete set of information 
    for all projects identified through CUP/CLP present on the ReGiS platform as of the extraction date, 
    regardless of the submission and outcome of the validation process, 
    that is, the periodic consolidation of information through automatic consistency checks 
    and through appropriate administrative checks carried out by the Responsible Administrations. 
    
    For each CUP/CLP, it reports the activation procedure, the status of the CUP, 
    the nature, the type, the sector, the sub-sector, the category, the title, the summary, 
    the total funding and funding broken down by source, the implementing entity, 
    the variable indicating whether it is an ongoing project, 
    and the expected and actual start and end dates of the project.
    """
    logger.info("Fetching P02..")

    try:
        p02 = fetch_csv_from_html(
            P02_URL, 
            ITALIA_DOMANI_BASE_URL, 
            P02_FILENAME
        )
        p02['Codice Fiscale Soggetto Attuatore'] = p02[
            'Codice Fiscale Soggetto Attuatore'
            ].astype(str)
        
        logger.info("Done fetching P02 Dataset")
        return p02
    
    except Exception as e:
        logger.error(f"Error fetching P02 Dataset: {e}")