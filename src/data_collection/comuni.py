import pandas as pd
from logging import getLogger

from src.sources import PATH_COMUNI

logger = getLogger(__name__)

def fetch_dataset_comuni() -> pd.DataFrame:
    """
    Returns the dataset with Italian municipalities
    """
    comuni = pd.read_csv(PATH_COMUNI, delimiter=';',encoding = "ISO-8859-1")
    comuni = comuni[['Denominazione Regione','Denominazione dell\'Unità territoriale sovracomunale \n(valida a fini statistici)']]
    comuni = comuni.rename(columns={'Denominazione dell\'Unità territoriale sovracomunale \n(valida a fini statistici)':'Denominazione sovracomunale','Denominazione Regione':'Regione'})
    comuni['Denominazione sovracomunale']=comuni['Denominazione sovracomunale'].replace(to_replace=r"Valle d'Aosta/Vallée d'Aoste", value='Aosta', regex=False)
    comuni['Denominazione sovracomunale']=comuni['Denominazione sovracomunale'].replace(to_replace=r"Bolzano/Bozen", value='Bolzano',regex=False)
    comuni['Denominazione sovracomunale']=comuni['Denominazione sovracomunale'].str.upper()
    comuni=comuni.drop_duplicates()

    return comuni