import sys
import pandas as pd

from src.logger import logger
from src.exception import CustomException


class HotelRecommender:

    def __init__(self):
        pass

    def recommend_hotels(
        self,
        dataset: pd.DataFrame,
        destination: str,
        days: int,
        top_n: int = 5
    ):

        try:

            logger.info("Starting Hotel Recommendation...")

            hotels = dataset.copy()

            hotels = hotels[
                hotels["place"].str.lower() == destination.lower()
            ]

            if hotels.empty:
                logger.warning("No hotels found.")
                return pd.DataFrame()

            hotels = hotels.drop_duplicates(
                subset=["name"]
            )

            hotels["total_cost"] = (
                hotels["price"] * days
            )

            hotels = hotels.sort_values(
                by="price"
            )

            logger.info(
                "Hotel Recommendation Completed."
            )

            return hotels.head(top_n)

        except Exception as e:

            logger.error(
                "Hotel Recommendation Failed."
            )

            raise CustomException(e, sys)
