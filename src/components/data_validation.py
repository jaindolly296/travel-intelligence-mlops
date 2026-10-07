import json
import sys

from src.logger import logger
from src.exception import CustomException
from src.entity.config_entity import DataValidationConfig


class DataValidation:

    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate(self, users, flights, hotels):

        try:

            logger.info("Starting data validation...")

            report = {}

            datasets = {
                "users": users,
                "flights": flights,
                "hotels": hotels
            }

            for name, df in datasets.items():

                logger.info(f"Validating {name} dataset")

                report[name] = {
                    "rows": int(df.shape[0]),
                    "columns": int(df.shape[1]),
                    "missing_values": df.isnull().sum().to_dict(),
                    "duplicate_rows": int(df.duplicated().sum()),
                    "data_types": {
                        col: str(dtype)
                        for col, dtype in df.dtypes.items()
                    }
                }

            self.config.validation_report_path.parent.mkdir(exist_ok=True)

            with open(self.config.validation_report_path, "w") as file:
                json.dump(report, file, indent=4)

            logger.info("Validation report saved successfully.")

            return report

        except Exception as e:
            logger.error("Validation failed.")
            raise CustomException(e, sys)
