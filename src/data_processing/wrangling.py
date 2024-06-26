import pandas as pd
from typing import Union


def map_comp(tematica: str):
    """
    Used on P02 Dataset

    -------------
    example usage:
    -------------
    ```
        p02["COMPONENTE"] = p02['NOME_TEMATICA'].apply(map_comp)
    ```
    """
    if tematica.count('-')==1:
        componente = tematica[6:tematica.find('-')-1]
    else:
        componente = tematica[6:tematica.find('I')-4]
    return componente


def map_investimento(tematica):
    """
    Used on P02 Dataset

    -------------
    example usage:
    -------------
    ```
        p02["INVESTIMENTO"] = p02['NOME_TEMATICA'].apply(map_investimento)
    ```
    """
    # con numeri
    if tematica.count('-')==1:
        investimento = tematica[tematica.find('-')+2:]
    else:
        first = tematica.find('-')+1
        tematica = tematica[first:]
        investimento = tematica[tematica.find('-')+2:]
    return investimento


def cat_conditions(data: pd.DataFrame) -> Union[str, int]:
    """ 
    Used to categorize conditions on the P03 Dataset.

    -------------
    example usage:
    -------------
    ```
        p03['CATEGORIA'] = p03.apply(cat_conditions,axis=1)
    ```
    """
    if data['cod_mis_premiale'] in [1,2,9]:
        return "GENERALE"
    elif data['cod_mis_premiale'] in [3,8,12]:
        return "DISABILI"
    elif data['cod_mis_premiale'] in [4,6,10]:
        return "GENERE"
    elif data['cod_mis_premiale'] in [5,7,11]:
        return "ETÀ"
    else:
        return 0
    

def map_importo(importo: int) -> str:
    """
    Used to divide total amounts from a contract into categories 
    on the P05 Dataset.

    -------------
    example usage:
    -------------
    ```
        p05['CLASSE_IMPORTO'] = p05['importo_complessivo_gara'].apply(map_importo)
    ```
    """
    if importo <= 100000:
        return 'BASSA'
    elif importo <= 1000000:
        return 'MEDIA'
    else:
        return 'ALTA'
    

def conditions_individuals(data: pd.DataFrame):
    """
    Indicates whether the indicator refers to individuals. 

    Should be used on raw Regis Dataset.

    -------------
    example usage:
    -------------
    ```
        regis_comm_ind['FLG_INDICATORI_PERSONE'] = regis_comm_ind.apply(
        conditions_individuals, axis=1
        )
    ```
    """

    if data['Codice Indicatore'] in [
        "C10.A",
        "C10.B",
        "C10.C",
        "C10.D",
        "C10.E",
        "C10.F",
        "C10.G",
        "C10.H",
        "C10IA",
        "C10IB",
        "C10IC",
        "C10ID",
        "C10IE",
        "C10IF",
        "C10IG",
        "C10IH",
        "C11.A",
        "C11.B",
        "C11.C",
        "C11.D",
        "C11.E",
        "C11.F",
        "C11.G",
        "C11.H",
        "C12",
        "C14.F",
        "C14.M",
        "C4",
        "C7",
        "C8.F",
        "C8.M"
    ]:
        return 1
    else:
        return 0
    

def conditions_gender(data: pd.DataFrame):
    """
    Indicates the direct impacts based on gender.  

    Should be used on raw Regis Dataset.

    -------------
    example usage:
    -------------
    ```
        regis_comm_ind['FLG_INDICATORI_GENERE'] = regis_comm_ind.apply(
        conditions_gender, axis=1
        )
    ```
    """
    if data['Codice Indicatore'] in [
        "C10.E",
        "C10.F",
        "C10.G",
        "C10.H",
        "C10IE",
        "C10IF",
        "C10IG",
        "C10IH",
        "C11.E",
        "C11.F",
        "C11.G",
        "C11.H",
        "C14.F",
         "C8.F"
        ]:
        return 1
    else:
        return 0
