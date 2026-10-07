import sys
import pandas as pd

from src.logger import logger
from src.exception import CustomException
from src.entity.config_entity import DataCleaningConfig


class DataCleaning:

    def __init__(self, config: DataCleaningConfig):
        self.config = config

    def clean_data(self, df):

        try:

            logger.info("Starting data cleaning...")

            df = df.copy()

            # -----------------------------
            # Rename Columns
            # -----------------------------
            rename_columns = {
                "name_x": "user_name",
                "name_y": "hotel_name",
                "price_x": "flight_price",
                "price_y": "hotel_price",
                "date_x": "flight_date",
                "date_y": "hotel_date",
                "userCode_x": "flight_user_code",
                "userCode_y": "hotel_user_code",
            }

            df.rename(columns=rename_columns, inplace=True)

            logger.info("Columns renamed successfully.")

            # -----------------------------
            # Remove Unnecessary Columns
            # -----------------------------
            df = self.remove_unnecessary_columns(df)

            # -----------------------------
            # Handle Missing Values
            # -----------------------------
            df = self.handle_missing_values(df)

            # -----------------------------
            # Fix Data Types
            # -----------------------------
            df = self.fix_data_types(df)

            # -----------------------------
            # Save Dataset
            # -----------------------------
            self.save_clean_data(df)

            logger.info("Data cleaning completed successfully.")

            return df

        except Exception as e:

            logger.error("Data cleaning failed.")

            raise CustomException(e, sys)

    def remove_unnecessary_columns(self, df):

        try:

            logger.info("Removing unnecessary columns...")

            columns_to_drop = [
                "code",
                "flight_user_code",
                "hotel_user_code",
            ]

            existing_columns = [
                col for col in columns_to_drop
                if col in df.columns
            ]

            df = df.drop(columns=existing_columns)

            logger.info("Unnecessary columns removed successfully.")

            return df

        except Exception as e:

            logger.error("Failed to remove unnecessary columns.")

            raise CustomException(e, sys)

    def handle_missing_values(self, df):

        try:

            logger.info("Handling missing values...")

            # Numeric columns
            numeric_columns = [
                "hotel_price",
                "total",
                "stay_year",
                "stay_month",
                "stay_day",
                "stay_cost_per_day",
                "days",
                "age",
                "travel_year",
                "travel_month",
                "travel_day",
            ]

            for column in numeric_columns:
                if column in df.columns:
                    df[column] = (
                        pd.to_numeric(df[column], errors="coerce")
                        .replace([float("inf"), float("-inf")], pd.NA)
                        .fillna(0)
                    )

            # Categorical columns
            categorical_columns = [
                "hotel_name",
                "place",
                "hotel_date",
                "stay_weekday",
            ]

            for column in categorical_columns:
                if column in df.columns:
                    df[column] = df[column].fillna("Not Available")

            logger.info("Missing values handled successfully.")

            return df

        except Exception as e:

            logger.error("Failed to handle missing values.")

            raise CustomException(e, sys)

    def fix_data_types(self, df):

        try:

            logger.info("Fixing data types...")

            # Boolean column
            if "is_weekend" in df.columns:
                df["is_weekend"] = (
                    df["is_weekend"]
                    .fillna(False)
                    .astype(bool)
                )

            integer_columns = [
                "age",
                "travel_year",
                "travel_month",
                "travel_day",
                "stay_year",
                "stay_month",
                "stay_day",
                "days",
            ]

            for column in integer_columns:

                if column in df.columns:

                    df[column] = (
                        pd.to_numeric(df[column], errors="coerce")
                        .replace([float("inf"), float("-inf")], 0)
                        .fillna(0)
                        .astype(int)
                    )

            logger.info("Data types fixed successfully.")

            return df

        except Exception as e:

            logger.error("Failed to fix data types.")

            raise CustomException(e, sys)

    def save_clean_data(self, df):

        try:

            logger.info("Saving clean dataset...")

            self.config.clean_data_path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            df.to_csv(
                self.config.clean_data_path,
                index=False,
            )

            logger.info("Clean dataset saved successfully.")

        except Exception as e:

            logger.error("Failed to save clean dataset.")

            raise CustomException(e, sys)
