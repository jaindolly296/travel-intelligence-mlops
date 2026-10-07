import sys
import pandas as pd

from src.logger import logger
from src.exception import CustomException
from src.entity.config_entity import DataMergingConfig


class DataMerging:

    def __init__(self, config: DataMergingConfig):
        self.config = config

    def merge_data(self):

        try:

            logger.info("Starting data merging...")

            # -----------------------------------
            # Load processed datasets
            # -----------------------------------
            users = pd.read_csv(
                self.config.processed_users_path
            )

            flights = pd.read_csv(
                self.config.processed_flights_path
            )

            hotels = pd.read_csv(
                self.config.processed_hotels_path
            )

            logger.info("Processed datasets loaded successfully.")

            # -----------------------------------
            # Merge Users + Flights
            # -----------------------------------
            users_flights = pd.merge(
                users,
                flights,
                left_on="code",
                right_on="userCode",
                how="inner"
            )

            logger.info("Users and Flights merged successfully.")

            # -----------------------------------
            # Merge with Hotels
            # -----------------------------------
            final_dataset = pd.merge(
                users_flights,
                hotels,
                on="travelCode",
                how="left"
            )

            logger.info("Hotels merged successfully.")

            # -----------------------------------
            # Remove duplicate columns
            # -----------------------------------
            final_dataset = final_dataset.loc[
                :,
                ~final_dataset.columns.duplicated()
            ]

            logger.info("Duplicate columns removed.")

            # -----------------------------------
            # Create directory if required
            # -----------------------------------
            self.config.merged_data_path.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            # -----------------------------------
            # Save merged dataset
            # -----------------------------------
            final_dataset.to_csv(
                self.config.merged_data_path,
                index=False
            )

            logger.info("Merged dataset saved successfully.")

            return final_dataset

        except Exception as e:

            logger.error("Data merging failed.")

            raise CustomException(e, sys)
