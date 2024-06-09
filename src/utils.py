import requests
import pandas as pd
import zipfile

from io import StringIO
from io import BytesIO
from logging import getLogger
from typing import List, Optional
from zipfile import ZipFile



logger = getLogger(__name__)


def fetch_csv(url: str) -> pd.DataFrame:
    """
    Fetches CSV data from a specified URL and returns it as a `pd.DataFrame`.

    -------
    Params:
    -------
    `url`: `str` 
        The URL of the CSV file.
    --------
    Returns:
    --------
    `pd.DataFrame` 
        The CSV data as a pandas DataFrame.
    """
    try:
        logger.info(f'Starting to fetch CSV data from {url}')
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        csv_data = StringIO(response.text)
        df = pd.read_csv(csv_data)
        logger.info(f'Successfully fetched and read CSV data into DataFrame')
        return df
    except requests.exceptions.RequestException as e:
        logger.error(f'Error fetching CSV data: {e}')
        return None
    except pd.errors.ParserError as e:
        logger.error(f'Error parsing CSV data: {e}')
        return None
    

def fetch_csv_from_zip(
    url: str, 
    csv_filename: str,
    separator: str = ";",
    na_values: Optional[list] = ["NA", "ND"]
    ) -> pd.DataFrame:
    """
    Fetches a ZIP file from a specified URL, extracts the specified CSV file, 
    and returns it as a pandas DataFrame.

    -------
    Params:
    -------
    `url`: `str`
        The URL of the ZIP file.
    `csv_filename`: `str`
        The name of the CSV file within the ZIP archive.
    ``: ```
        The separator used in the CSV file
    `na_values`: `list`

    --------
    Returns:
    --------
    `pd.DataFrame` 
        The CSV data as a pandas DataFrame.
    """
    try:
        logger.info(f'Starting to fetch ZIP file from {url}')
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Use BytesIO to handle the ZIP file in memory
        with ZipFile(BytesIO(response.content)) as zip:
            with zip.open(csv_filename) as file:
                df = pd.read_csv(file, sep=separator, na_values=na_values)
                logger.info(f'Successfully read {csv_filename} from ZIP file into DataFrame')
                return df
    except requests.exceptions.RequestException as e:
        logger.error(f'Error fetching ZIP file: {e}')
        return None
    except zipfile.BadZipFile as e:
        logger.error(f'Error opening ZIP file: {e}')
        return None
    except KeyError as e:
        logger.error(f'Error extracting {csv_filename} from ZIP file: {e}')
        return None
    except pd.errors.ParserError as e:
        logger.error(f'Error parsing CSV data: {e}')
        return None