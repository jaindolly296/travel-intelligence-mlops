import sys
import pandas as pd

from src.logger import logger
from src.exception import CustomException
from src.entity.config_entity import DataTransformationConfig


class DataTransformation:

    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # ==========================================================
    # Validate Numeric Columns
    # ==========================================================
    def validate_numeric_columns(self, users, flights, hotels):

        logger.info("Validating numeric columns...")

        # -------------------------
        # Users
        # -------------------------
        invalid_age_low = (users["age"] < 18).sum()
        invalid_age_high = (users["age"] > 100).sum()

        if invalid_age_low > 0:
            raise ValueError(
                f"Users dataset contains {invalid_age_low} records with age less than 18."
            )

        if invalid_age_high > 0:
            raise ValueError(
                f"Users dataset contains {invalid_age_high} records with age greater than 100."
            )

        # -------------------------
        # Flights
        # -------------------------
        invalid_price = (flights["price"] <= 0).sum()
        invalid_distance = (flights["distance"] <= 0).sum()
        invalid_time = (flights["time"] <= 0).sum()

        if invalid_price > 0:
            raise ValueError(
                f"Flights dataset contains {invalid_price} invalid price records."
            )

        if invalid_distance > 0:
            raise ValueError(
                f"Flights dataset contains {invalid_distance} invalid distance records."
            )

        if invalid_time > 0:
            raise ValueError(
                f"Flights dataset contains {invalid_time} invalid travel time records."
            )

        # -------------------------
        # Hotels
        # -------------------------
        invalid_days = (hotels["days"] <= 0).sum()
        invalid_hotel_price = (hotels["price"] <= 0).sum()
        invalid_total = (hotels["total"] <= 0).sum()

        if invalid_days > 0:
            raise ValueError(
                f"Hotels dataset contains {invalid_days} invalid stay duration records."
            )

        if invalid_hotel_price > 0:
            raise ValueError(
                f"Hotels dataset contains {invalid_hotel_price} invalid hotel price records."
            )

        if invalid_total > 0:
            raise ValueError(
                f"Hotels dataset contains {invalid_total} invalid total amount records."
            )

        logger.info("Numeric validation completed successfully.")

    # ==========================================================
    # Flight Feature Engineering
    # ==========================================================
    def engineer_flight_features(self, flights):

        logger.info("Creating flight features...")

        flights["travel_year"] = flights["date"].dt.year
        flights["travel_month"] = flights["date"].dt.month
        flights["travel_day"] = flights["date"].dt.day
        flights["travel_weekday"] = flights["date"].dt.day_name()

        flights["is_weekend"] = (
            flights["date"].dt.weekday >= 5
        ).astype(int)

        logger.info("Flight features created successfully.")

        return flights

    # ==========================================================
    # Hotel Feature Engineering
    # ==========================================================
    def engineer_hotel_features(self, hotels):

        logger.info("Creating hotel features...")

        hotels["stay_year"] = hotels["date"].dt.year
        hotels["stay_month"] = hotels["date"].dt.month
        hotels["stay_day"] = hotels["date"].dt.day
        hotels["stay_weekday"] = hotels["date"].dt.day_name()

        hotels["stay_cost_per_day"] = (
            hotels["total"] / hotels["days"]
        ).round(2)

        logger.info("Hotel features created successfully.")

        return hotels

    # ==========================================================
    # User Feature Engineering
    # ==========================================================
    def engineer_user_features(self, users):

        logger.info("Creating user features...")

        # Age Group
        users["age_group"] = pd.cut(
            users["age"],
            bins=[17, 25, 35, 50, 100],
            labels=[
                "Young Adult",
                "Adult",
                "Middle Age",
                "Senior"
            ]
        )

        # Company Frequency
        company_frequency = (
            users["company"]
            .value_counts()
            .to_dict()
        )

        users["company_frequency"] = users["company"].map(
            company_frequency
        )

        logger.info("User features created successfully.")

        return users

    # ==========================================================
    # Data Transformation
    # ==========================================================
    def transform(self, users, flights, hotels):

        try:

            logger.info("Starting data transformation...")

            # Remove duplicate rows
            users = users.drop_duplicates()
            flights = flights.drop_duplicates()
            hotels = hotels.drop_duplicates()

            logger.info("Duplicate rows removed.")

            # Convert date columns
            flights["date"] = pd.to_datetime(
                flights["date"],
                format="%m/%d/%Y"
            )

            hotels["date"] = pd.to_datetime(
                hotels["date"],
                format="%m/%d/%Y"
            )

            logger.info("Date columns converted successfully.")

            # Validate numeric columns
            self.validate_numeric_columns(
                users,
                flights,
                hotels
            )

            # Flight Feature Engineering
            flights = self.engineer_flight_features(
                flights
            )

            # Hotel Feature Engineering
            hotels = self.engineer_hotel_features(
                hotels
            )

            # User Feature Engineering
            users = self.engineer_user_features(
                users
            )

            # Create processed directory
            self.config.processed_users_path.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            # Save processed datasets
            users.to_csv(
                self.config.processed_users_path,
                index=False
            )

            flights.to_csv(
                self.config.processed_flights_path,
                index=False
            )

            hotels.to_csv(
                self.config.processed_hotels_path,
                index=False
            )

            logger.info("Processed datasets saved successfully.")

            return users, flights, hotels

        except Exception as e:

            logger.error("Data transformation failed.")

            raise CustomException(e, sys)
