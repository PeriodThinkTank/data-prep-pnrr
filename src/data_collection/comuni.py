import pandas as pd
from logging import getLogger

from src.sources import PATH_COMUNI

logger = getLogger(__name__)

def fetch_dataset_comuni() -> pd.DataFrame:
    """
    Returns the dataset with Italian municipalities
    """
    comuni = pd.read_csv(PATH_COMUNI, delimiter=';')
    comuni.columns = comuni.columns.str.replace('�', 'à')
    comuni.columns = comuni.columns.str.strip().str.replace('\r\n', ' ', regex=False)
    comuni = comuni[
        [
            'Denominazione Regione', 
            'Denominazione dell\'Unità territoriale sovracomunale  (valida a fini statistici)', 
            'Denominazione in italiano', 
            'Codice Comune formato alfanumerico'
        ]
    ]
    comuni = comuni.rename(
    columns=
        {
            'Denominazione in italiano': 'Comune', 
            'Codice Comune formato alfanumerico': 'Codice Comune Alfanumerico',
            'Denominazione dell\'Unità territoriale sovracomunale  (valida a fini statistici)':'Denominazione sovracomunale',
            'Denominazione Regione':'Regione'
        }
    )
    comuni['Codice Comune Alfanumerico']= comuni['Codice Comune Alfanumerico'].astype(str)
    comuni['Denominazione sovracomunale']=comuni['Denominazione sovracomunale'].replace(to_replace=r"Valle d'Aosta/Vallée d'Aoste", value='Aosta', regex=False)
    comuni['Denominazione sovracomunale']=comuni['Denominazione sovracomunale'].replace(to_replace=r"Bolzano/Bozen", value='Bolzano',regex=False)
    comuni['Denominazione sovracomunale']=comuni['Denominazione sovracomunale'].str.upper()
    comuni=comuni.drop_duplicates()

    return comuni