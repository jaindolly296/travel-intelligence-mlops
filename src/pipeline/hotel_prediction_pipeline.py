import sys
import joblib
import pandas as pd

from src.constants import MODELS_DIR
from src.logger import logger
from src.exception import CustomException


class HotelPredictionPipeline:

    def __init__(self):

        try:
            model_dir = MODELS_DIR / "regression"

            logger.info("Loading Hotel Prediction Model...")

            self.model = joblib.load(
                model_dir / "hotel_total_model.pkl"
            )

            self.preprocessor = joblib.load(
                model_dir / "hotel_total_model_preprocessor.pkl"
            )

            logger.info("Hotel Prediction Model Loaded Successfully.")

        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, input_data: dict):

        try:

            df = pd.DataFrame([input_data])

            transformed = self.preprocessor.transform(df)

            prediction = self.model.predict(transformed)

            return float(prediction[0])

        except Exception as e:
            raise CustomException(e, sys)
