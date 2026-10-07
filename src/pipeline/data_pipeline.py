from src.config.configuration import Configuration

from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.data_merging import DataMerging
from src.components.data_cleaning import DataCleaning

from src.logger import logger


class DataPipeline:

    def __init__(self):
        self.config = Configuration()

    def run_pipeline(self):

        logger.info("=" * 60)
        logger.info("Starting Data Pipeline")
        logger.info("=" * 60)

        ingestion = DataIngestion(
            self.config.get_data_ingestion_config()
        )

        users_df, flights_df, hotels_df = ingestion.load_data()

        validation = DataValidation(
            self.config.get_data_validation_config()
        )

        validation.validate(
            users_df,
            flights_df,
            hotels_df
        )

        transformation = DataTransformation(
            self.config.get_data_transformation_config()
        )

        transformation.transform(
            users_df,
            flights_df,
            hotels_df
        )

        merger = DataMerging(
            self.config.get_data_merging_config()
        )

        merged_df = merger.merge_data()

        cleaning = DataCleaning(
            self.config.get_data_cleaning_config()
        )

        clean_df = cleaning.clean_data(
            merged_df
        )

        logger.info("=" * 60)
        logger.info("Data Pipeline Completed")
        logger.info("=" * 60)

        return clean_df
