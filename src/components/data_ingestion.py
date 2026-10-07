import sys
import pandas as pd

from src.logger import logger
from src.exception import CustomException
from src.entity.config_entity import DataIngestionConfig


class DataIngestion:

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def load_data(self):

        try:

            logger.info("Starting data ingestion...")

            logger.info("Loading users dataset...")
            users = pd.read_csv(self.config.users_path)

            logger.info("Loading flights dataset...")
            flights = pd.read_csv(self.config.flights_path)

            logger.info("Loading hotels dataset...")
            hotels = pd.read_csv(self.config.hotels_path)

            logger.info("All datasets loaded successfully.")

            return users, flights, hotels

        except Exception as e:
            logger.error("Error during data ingestion.")
            raise CustomException(e, sys)
