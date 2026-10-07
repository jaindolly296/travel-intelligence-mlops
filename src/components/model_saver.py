import sys
import joblib
from pathlib import Path

from src.logger import logger
from src.exception import CustomException


class ModelSaver:

    def __init__(self):
        pass

    def save_model(
        self,
        model,
        preprocessor,
        model_name,
        preprocessor_name=None,
        model_dir="models/regression"
    ):

        try:

            logger.info("Saving model...")

            model_path = Path(model_dir)

            model_path.mkdir(
                parents=True,
                exist_ok=True
            )

            if preprocessor_name is None:
                preprocessor_name = f"{model_name}_preprocessor.pkl"

            joblib.dump(
                model,
                model_path / f"{model_name}.pkl"
            )

            joblib.dump(
                preprocessor,
                model_path / preprocessor_name
            )

            logger.info(
                f"Model saved successfully: {model_name}.pkl"
            )

        except Exception as e:

            logger.error("Failed to save model.")

            raise CustomException(e, sys)
