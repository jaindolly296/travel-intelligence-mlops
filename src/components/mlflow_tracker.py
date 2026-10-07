import os

import mlflow
import mlflow.sklearn
import mlflow.xgboost

from dotenv import load_dotenv
from xgboost import XGBRegressor

from src.logger import logger


load_dotenv()


class MLflowTracker:

    def __init__(self):

        tracking_uri = os.getenv(
            "MLFLOW_TRACKING_URI",
            "sqlite:///mlflow.db"
        )

        experiment_name = os.getenv(
            "MLFLOW_EXPERIMENT",
            "Travel Intelligence MLOps"
        )

        mlflow.set_tracking_uri(tracking_uri)

        mlflow.set_experiment(experiment_name)

    def log_complete_model(
        self,
        model_name,
        model,
        metrics,
        params=None
    ):

        logger.info("=" * 60)
        logger.info(f"Starting MLflow Run : {model_name}")
        logger.info("=" * 60)

        with mlflow.start_run(run_name=model_name):

            if params:
                mlflow.log_params(params)
                logger.info("Parameters logged.")

            mlflow.log_metrics(metrics)
            logger.info("Metrics logged.")

            # Disabled because Jenkins container has limited RAM.
            # Enable later if Docker memory is increased.
            #
            # if isinstance(model, XGBRegressor):
            #     mlflow.xgboost.log_model(
            #         xgb_model=model,
            #         name="model"
            #     )
            # else:
            #     mlflow.sklearn.log_model(
            #         sk_model=model,
            #         name="model"
            #     )

            logger.info("Model artifact logging skipped.")

        logger.info("=" * 60)
        logger.info("MLflow Run Completed Successfully")
        logger.info("=" * 60)
