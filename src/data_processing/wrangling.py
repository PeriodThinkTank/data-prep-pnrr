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