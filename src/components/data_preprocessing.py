import sys

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

from src.logger import logger
from src.exception import CustomException


class DataPreprocessing:

    def __init__(self):
        pass

    def preprocess(
        self,
        X_train,
        X_test,
        categorical_columns,
        numerical_columns
    ):

        try:

            logger.info("Starting Data Preprocessing...")

            categorical_pipeline = Pipeline(

                steps=[

                    (
                        "encoder",
                        OneHotEncoder(
                            handle_unknown="ignore"
                        )
                    )

                ]

            )

            numerical_pipeline = Pipeline(

                steps=[

                    (
                        "scaler",
                        StandardScaler()
                    )

                ]

            )

            preprocessor = ColumnTransformer(

                transformers=[

                    (
                        "categorical",
                        categorical_pipeline,
                        categorical_columns
                    ),

                    (
                        "numerical",
                        numerical_pipeline,
                        numerical_columns
                    )

                ]

            )

            logger.info("Fitting Preprocessor...")

            X_train = preprocessor.fit_transform(
                X_train
            )

            X_test = preprocessor.transform(
                X_test
            )

            logger.info("Preprocessing completed successfully.")

            return (
                X_train,
                X_test,
                preprocessor
            )

        except Exception as e:

            logger.error("Data preprocessing failed.")

            raise CustomException(e, sys)
