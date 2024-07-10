"""Used to collect and wrangle data for Period's PNRR Web App"""
import pandas as pd
from logging import getLogger

from src.data_collection.comuni import fetch_dataset_comuni
from src.data_collection.indicators import get_indicators
from src.data_collection.indicators_sdg import get_indicators_and_sdg 
from src.data_collection.missioni import fetch_pnrr_missions
from src.data_collection.p01 import get_p01
from src.data_collection.p02 import get_p02
from src.data_collection.p03 import get_p03
from src.data_collection.p04 import get_p04
from src.data_collection.p05 import get_p05
from src.data_collection.targets import get_targets
from src.data_processing.wrangling import cat_conditions, map_comp, map_investimento, map_importo

logger = getLogger(__name__)

COLONNE_DA_SELEZIONARE = [
    'CIG', 
    'CUP',  
    'Regione', 
    'provincia',  
    'Comune', 
    'importo_complessivo_gara', 
    'CLASSE_IMPORTO', 
    'Missione', 
    'Descrizione Missione',
    'Componente',  
    'Descrizione Componente',
    'ID Misura', 
    'Codice Univoco Misura',
    'Descrizione Misura', 
    'ID Submisura', 
    'Codice Univoco Submisura', 
    'Descrizione Submisura',
    'cod_mis_premiale', 
    'misura_premiale', 
    'CATEGORIA', 
    'flag_quote', 
    'quota_femminile', 
    'quota_giovanile', 
    'cod_mot_deroga', 
    'mot_deroga', 
    'data_pubblicazione', 
    'anno_pubblicazione', 
    'FLAG_URGENZA', 
    'MOTIVO_URGENZA', 
    'ESITO',
]


if __name__ == "__main__":

    logger.info("Starting getting datasets; this may take a while..")

    p01 = get_p01()

    p02 = get_p02()

    p03 = get_p03()
    p03 = p03.rename(columns={'cig':'CIG'})
    p03['CATEGORIA'] = p03.apply(cat_conditions,axis=1)

    p04 = get_p04()

    p05 = get_p05()
    p05 = p05.rename(columns={'cig':'CIG'})
    p05['importo_complessivo_gara'] = p05['importo_complessivo_gara'].astype(float)
    p05['CLASSE_IMPORTO'] = p05['importo_complessivo_gara'].apply(map_importo)

    comuni = fetch_dataset_comuni()
    comuni['Codice Comune Alfanumerico'] = comuni['Codice Comune Alfanumerico'].astype(str)

    missions, components = fetch_pnrr_missions()

    logger.info("Done fetching datasets, now we'll merge them..")

    p02 = p02.merge(
        missions,left_on="Missione", 
        right_on=missions.index, how='inner'
        ).drop_duplicates()
    p02 = p02.merge(
        components,
        left_on="Componente", 
        right_on=components.index, 
        how='inner').drop_duplicates()
    
    p05=p05.merge(
        comuni,
        left_on='luogo_istat', 
        right_on='Codice Comune Alfanumerico',
        how='left'
    ).drop_duplicates()

    leftnew_3 = p05.merge(p03, on='CIG', how='left').drop_duplicates()
    leftnew_34 = leftnew_3.merge(p04, on='CIG', how='left').drop_duplicates()
    leftnew_341 = leftnew_34.merge(p01, on='CIG', how='left').drop_duplicates()
    leftnew_3412 = leftnew_341.merge(p02,how='left',left_on='CUP',right_on='CUP').drop_duplicates()
    
    master_table = leftnew_3412[COLONNE_DA_SELEZIONARE]
    master_table.to_csv("data/updated/master_table_base.csv", sep=";")
    
    logger.info("Master Table saved.")

