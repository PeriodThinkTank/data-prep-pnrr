""" Used to collect and wrangle data for Period's PNRR Web App"""

from src.data_collection.p01 import get_p01
from src.data_collection.p02 import get_p02

if __name__ == "__main__":

    p01 = get_p01()

    p02 = get_p02()

