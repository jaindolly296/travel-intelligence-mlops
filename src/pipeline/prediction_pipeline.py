import os
import joblib
import pandas as pd

from src.logger import logger
from src.exception import CustomException


class PredictPipeline:

    def __init__(self):

        try:

            self.model_path = os.path.join(
                "models",
                "regression",
                "flight_price_model.pkl"
            )

            self.preprocessor_path = os.path.join(
                "models",
                "regression",
                "preprocessor.pkl"
            )

            logger.info("Loading trained model...")
            self.model = joblib.load(self.model_path)

            logger.info("Loading preprocessor...")
            self.preprocessor = joblib.load(self.preprocessor_path)

            logger.info("Prediction pipeline initialized successfully.")

        except Exception as e:
            logger.error(f"Error loading prediction artifacts: {e}")
            raise CustomException(e)

    def predict(self, features: pd.DataFrame):

        try:

            logger.info("Starting prediction...")

            transformed_data = self.preprocessor.transform(features)

            prediction = self.model.predict(transformed_data)

            logger.info("Prediction completed successfully.")

            return prediction

        except Exception as e:

            logger.error(f"Prediction failed: {e}")

            raise CustomException(e)
