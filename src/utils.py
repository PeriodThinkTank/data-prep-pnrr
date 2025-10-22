import random
import re
import time
import requests
import pandas as pd
import zipfile

from bs4 import BeautifulSoup
from io import StringIO
from io import BytesIO
from logging import getLogger
from typing import List, Optional, Union
from urllib.parse import urlparse
from urllib.request import urlopen
from zipfile import ZipFile


logger = getLogger(__name__)


def get_base_url(url: str) -> str:
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    return base_url 


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
    `separator`: `str`
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
    

def fetch_excel_from_zip(
    url: str, 
    xlsx_filename: str,
    sheet_name: str, 
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
    `xlsx_filename`: `str`
        The name of the Excel file within the ZIP archive.
    `sheet_name`: `str`
        The name of the relevant sheet
    `na_values`: `list`
    --------
    Returns:
    --------
    `pd.DataFrame` 
        The Excel data as a pandas DataFrame.
    """
    try:
        logger.info(f'Starting to fetch ZIP file from {url}')
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Use BytesIO to handle the ZIP file in memory
        with ZipFile(BytesIO(response.content)) as zip:
            with zip.open(xlsx_filename) as file:
                df = pd.read_excel(file, sheet_name=sheet_name, na_values=na_values)
                logger.info(f'Successfully read {xlsx_filename} from ZIP file into DataFrame')
                return df
    except requests.exceptions.RequestException as e:
        logger.error(f'Error fetching ZIP file: {e}')
        return None
    except zipfile.BadZipFile as e:
        logger.error(f'Error opening ZIP file: {e}')
        return None
    except KeyError as e:
        logger.error(f'Error extracting {xlsx_filename} from ZIP file: {e}')
        return None
    except pd.errors.ParserError as e:
        logger.error(f'Error parsing CSV data: {e}')
        return None
    

def fetch_csvs_from_url(url: str, files_title: str, separator: str = ";") -> Union[pd.DataFrame, None]:
    """
    Fetches multiple CSVs files with a common title (i.e. `cig_csv`) 
    from a URL, and returns a `pd.DataFrame` out of them. 

    -------
    Params:
    -------
    `url`: `str`
        The URL of the ZIP file.
    `files_title`: `str`  
        The common part of the title between the files you plan to fetch
    `separator`: `str`
        The separator used in the CSV file(s)
    --------
    Returns:
    --------
    `pd.DataFrame` 
        The CSVs data merged into a pandas DataFrame.
    """

    base_link = get_base_url(url)
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/118.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": base_link,
    }

    session = requests.Session()
    session.headers.update(headers)
    
    html_page = session.get(url)
    soup = BeautifulSoup(html_page.content, 'html.parser')
    file_urls = soup.findAll(
        'a', 
        class_="heading",
        title=re.compile(f"{files_title}")
    )

    links = [link.get('href') for link in file_urls]

    data_links = []

    for link in links:
        l = base_link+link
        html_page = session.get(l)
        soup = BeautifulSoup(html_page.content, 'html.parser')
        file_urls = soup.findAll(
            'a',
            class_="btn btn-primary resource-url-analytics resource-type-None"
        )
        data_links.append(file_urls[0].get('href'))

        time.sleep(random.uniform(1.5, 3.5))

    logger.info(f"Found {len(data_links)} .csv files in this link: {url}")

    full_df = pd.DataFrame()

    for link in data_links:
        if link.endswith('.zip'):
            resp = urlopen(link)
            zipfile = ZipFile(BytesIO(resp.read()))
            fname = zipfile.namelist()[0]
            df = pd.read_csv(zipfile.open(fname), dtype=object, delimiter=';')
            zipfile.close()
            full_df = pd.concat([full_df, df], ignore_index=True, sort=False)

            logger.info(f"File {fname} appended to the Dataset")
        else:
            print(f"Link {link} is not a zip file")

    num_rows = full_df.shape[0]
    num_columns = full_df.shape[1]

    if num_rows > 0:
        logger.info(f"Dataset has {num_rows} Number of rows")
        return full_df 
    else:
        logger.warning(f"Dataset from {url} is emty")
        return None


def fetch_csv_from_html(
        page_url: str, 
        base_url: str, 
        filename_contains: str,
        separator: str = ";",) -> pd.DataFrame:
    """
    Fetches CSV data from a webpage URL and returns it as a `pd.DataFrame`.

    -------
    Params:
    -------
    `page_url`: `str` 
        The URL of the webpage containing the CSV file link.
    `base_url`: `str`
        The base URL to construct the full CSV file URL.
    `filename_contains`: `str`
        A substring that the desired CSV file name contains.
    `separator`: `str`
        The separator used in the CSV file
    --------
    Returns:
    --------
    `pd.DataFrame` 
        The CSV data as a pandas DataFrame.
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        logger.info(f'Starting to fetch webpage content from {page_url}')
        response = requests.get(page_url, headers=headers)
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the span element containing the CSV file information
        spans = soup.find_all('span', class_='title-file', attrs={'data-extension': 'csv'})
        
        selected_span = None
        for span in spans:
            if filename_contains in span.text:
                selected_span = span
                break

        if not selected_span:
            logger.error(f'CSV file containing "{filename_contains}" not found on the page')
            return None
        
        # Construct the full URL of the CSV file
        csv_url = base_url + span['data-url']
        logger.info(f'CSV file URL found: {csv_url}')

        csv_response = requests.get(csv_url, headers=headers)
        csv_response.raise_for_status()
        csv_data = StringIO(csv_response.text)
        df = pd.read_csv(csv_data, on_bad_lines='skip', delimiter=separator)
        logger.info(f'Successfully fetched and read CSV data into DataFrame')
        return df
    except requests.exceptions.RequestException as e:
        logger.error(f'Error fetching webpage or CSV data: {e}')
        return None
    except pd.errors.ParserError as e:
        logger.error(f'Error parsing CSV data: {e}')
        return None
    

