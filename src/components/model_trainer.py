import sys

from sklearn.linear_model import (
    LinearRegression,
    Ridge,
    Lasso
)

from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import (
    GradientBoostingRegressor,
    ExtraTreesRegressor
)

from xgboost import XGBRegressor

from src.logger import logger
from src.exception import CustomException


class ModelTrainer:

    def __init__(self, selected_models=None):

        self.available_models = {

            "Linear Regression":
                LinearRegression(),

            "Ridge Regression":
                Ridge(random_state=42),

            "Lasso Regression":
                Lasso(random_state=42),

            "Decision Tree":
                DecisionTreeRegressor(
                    random_state=42
                ),

            "Gradient Boosting":
                GradientBoostingRegressor(
                    random_state=42
                ),

            "Extra Trees":
                ExtraTreesRegressor(
                    n_estimators=100,
                    max_depth=20,
                    min_samples_split=10,
                    min_samples_leaf=5,
                    max_features="sqrt",
                    random_state=42,
                    n_jobs=1
                ),

            "XGBoost":
                XGBRegressor(

                    objective="reg:squarederror",

                    n_estimators=100,

                    learning_rate=0.05,

                    max_depth=6,

                    subsample=0.8,

                    colsample_bytree=0.8,

                    random_state=42,

                    n_jobs=2
                )
        }

        if selected_models is None:

            self.models = self.available_models

        else:

            self.models = {
                name: self.available_models[name]
                for name in selected_models
            }

    def train_models(self, X_train, y_train):

        try:

            logger.info(f"Training {len(self.models)} model(s)...")

            trained_models = {}

            for model_name, model in self.models.items():

                logger.info(f"Training {model_name}")

                model.fit(X_train, y_train)

                trained_models[model_name] = model

            logger.info("Training completed.")

            return trained_models

        except Exception as e:

            raise CustomException(e, sys)
