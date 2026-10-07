import sys
from math import sqrt

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from src.logger import logger
from src.exception import CustomException


class ModelEvaluation:

    def __init__(self):
        pass

    def evaluate_models(
        self,
        trained_models,
        X_test,
        y_test
    ):

        try:

            logger.info("Evaluating all models...")

            results = {}

            best_model_name = None
            best_model = None
            best_r2 = float("-inf")

            # Preferred order if scores are very close
            model_priority = [
                "XGBoost",
                "Gradient Boosting",
                "Extra Trees",
                "Ridge Regression",
                "Linear Regression",
                "Decision Tree",
                "Lasso Regression"
            ]

            for model_name, model in trained_models.items():

                logger.info(f"Evaluating {model_name}")

                predictions = model.predict(X_test)

                mae = mean_absolute_error(
                    y_test,
                    predictions
                )

                mse = mean_squared_error(
                    y_test,
                    predictions
                )

                rmse = sqrt(mse)

                r2 = r2_score(
                    y_test,
                    predictions
                )

                results[model_name] = {
                    "MAE": round(mae, 4),
                    "RMSE": round(rmse, 4),
                    "R2": round(r2, 4)
                }

                logger.info(
                    f"{model_name:<25}"
                    f"R2={r2:.4f}   "
                    f"RMSE={rmse:.4f}   "
                    f"MAE={mae:.4f}"
                )

                # Select highest R²
                if r2 > best_r2:
                    best_r2 = r2
                    best_model_name = model_name
                    best_model = model

                # If R² difference is tiny (<=0.001), prefer production-friendly model
                elif abs(r2 - best_r2) <= 0.001:

                    current_priority = model_priority.index(best_model_name)
                    new_priority = model_priority.index(model_name)

                    if new_priority < current_priority:
                        best_model_name = model_name
                        best_model = model
                        best_r2 = r2

            logger.info("=" * 60)
            logger.info(f"Best Model : {best_model_name}")
            logger.info(f"Best R2 Score : {best_r2:.4f}")
            logger.info("=" * 60)

            return (
                best_model_name,
                best_model,
                results
            )

        except Exception as e:

            logger.error("Model evaluation failed.")

            raise CustomException(e, sys)
