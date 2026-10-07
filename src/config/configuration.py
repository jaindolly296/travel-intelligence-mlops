from src.constants import (
    RAW_DATA_DIR,
    ARTIFACTS_DIR,
    MERGED_DATA_PATH,
    CLEAN_DATA_PATH
)

from src.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    DataMergingConfig,
    DataCleaningConfig,
)

from src.entity.model_training_config import ModelTrainingConfig


class Configuration:

    # ==========================================================
    # Data Ingestion
    # ==========================================================
    def get_data_ingestion_config(self):

        return DataIngestionConfig(
            users_path=RAW_DATA_DIR / "users.csv",
            flights_path=RAW_DATA_DIR / "flights.csv",
            hotels_path=RAW_DATA_DIR / "hotels.csv",
        )

    # ==========================================================
    # Data Validation
    # ==========================================================
    def get_data_validation_config(self):

        return DataValidationConfig(
            validation_report_path=ARTIFACTS_DIR / "validation_report.json"
        )

    # ==========================================================
    # Data Transformation
    # ==========================================================
    def get_data_transformation_config(self):

        return DataTransformationConfig(
            processed_users_path=RAW_DATA_DIR.parent / "processed" / "users_processed.csv",
            processed_flights_path=RAW_DATA_DIR.parent / "processed" / "flights_processed.csv",
            processed_hotels_path=RAW_DATA_DIR.parent / "processed" / "hotels_processed.csv",
        )

    # ==========================================================
    # Data Merging
    # ==========================================================
    def get_data_merging_config(self):

        transformation_config = self.get_data_transformation_config()

        return DataMergingConfig(
            processed_users_path=transformation_config.processed_users_path,
            processed_flights_path=transformation_config.processed_flights_path,
            processed_hotels_path=transformation_config.processed_hotels_path,
            merged_data_path=MERGED_DATA_PATH,
        )

    # ==========================================================
    # Data Cleaning
    # ==========================================================
    def get_data_cleaning_config(self):

        return DataCleaningConfig(
            clean_data_path=CLEAN_DATA_PATH
        )

    # ==========================================================
    # Model Training
    # ==========================================================
    def get_model_training_config(self, model_type: str):

        if model_type == "flight":

            return ModelTrainingConfig(

                dataset_path=CLEAN_DATA_PATH,

                target_column="flight_price",

                categorical_columns=[
                    "gender",
                    "age_group",
                    "company",
                    "from",
                    "to",
                    "flightType",
                    "travel_weekday"
                ],

                numerical_columns=[
                    "age",
                    "company_frequency",
                    "time",
                    "distance",
                    "travel_year",
                    "travel_month",
                    "travel_day",
                    "is_weekend"
                ],

                selected_models=[
                    "Linear Regression",
                    "XGBoost"
                ],

                model_name="flight_price_model"

            )

        elif model_type == "hotel":

            return ModelTrainingConfig(

                dataset_path=RAW_DATA_DIR.parent / "processed" / "hotels_processed.csv",

                target_column="total",

                categorical_columns=[
                    "name",
                    "place",
                    "stay_weekday"
                ],

                numerical_columns=[
                    "days",
                    "stay_year",
                    "stay_month",
                    "stay_day"
                ],

                selected_models=[
                    "Linear Regression",
                    "Extra Trees"
                ],

                model_name="hotel_total_model"

            )

        else:

            raise ValueError(f"Unknown model type: {model_type}")

    # ==========================================================
    # XGBoost Hyperparameter Tuning
    # ==========================================================
    def get_xgboost_param_grid(self):

        return {

            "n_estimators": [
                100,
                200
            ],

            "learning_rate": [
                0.05,
                0.1
            ],

            "max_depth": [
                6,
                8
            ],

            "subsample": [
                0.8
            ],

            "colsample_bytree": [
                0.8
            ]

        }
