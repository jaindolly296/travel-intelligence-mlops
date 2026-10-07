import sys

from sklearn.model_selection import RandomizedSearchCV

from src.logger import logger
from src.exception import CustomException


class HyperparameterTuner:

    def tune_model(
        self,
        model,
        param_grid,
        X_train,
        y_train
    ):

        try:

            logger.info("Starting Hyperparameter Tuning...")

            random_search = RandomizedSearchCV(

                estimator=model,

                param_distributions=param_grid,

                n_iter=8,

                scoring="r2",

                cv=3,

                verbose=2,

                random_state=42,

                n_jobs=-1

            )

            random_search.fit(
                X_train,
                y_train
            )

            logger.info("Hyperparameter tuning completed.")

            logger.info(f"Best Score : {random_search.best_score_:.4f}")
            logger.info(f"Best Parameters : {random_search.best_params_}")

            return random_search.best_estimator_

        except Exception as e:

            raise CustomException(e, sys)
