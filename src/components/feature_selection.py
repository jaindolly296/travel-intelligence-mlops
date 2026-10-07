import sys
import pandas as pd

from src.logger import logger
from src.exception import CustomException


class FeatureSelection:

    def __init__(self):
        pass

    def select_features(
        self,
        df: pd.DataFrame,
        target_column: str,
        feature_columns: list
    ):

        try:

            logger.info("Starting feature selection...")

            missing_features = [
                col for col in feature_columns
                if col not in df.columns
            ]

            if missing_features:
                raise ValueError(
                    f"Missing feature columns: {missing_features}"
                )

            if target_column not in df.columns:
                raise ValueError(
                    f"Target column '{target_column}' not found."
                )

            X = df[feature_columns]

            y = df[target_column]

            logger.info("Feature selection completed successfully.")
            logger.info(f"Number of Features : {X.shape[1]}")
            logger.info(f"Target Column : {target_column}")

            return X, y

        except Exception as e:

            logger.error("Feature selection failed.")

            raise CustomException(e, sys)
