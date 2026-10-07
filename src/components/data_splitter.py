import sys

from sklearn.model_selection import train_test_split

from src.logger import logger
from src.exception import CustomException


class DataSplitter:

    def __init__(
        self,
        test_size=0.2,
        random_state=42
    ):

        self.test_size = test_size
        self.random_state = random_state

    def split_data(self, X, y):

        try:

            logger.info("Starting Train-Test Split...")

            X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=self.test_size,
                random_state=self.random_state
            )

            logger.info("Train-Test Split completed successfully.")

            logger.info(f"X Train Shape : {X_train.shape}")
            logger.info(f"X Test Shape : {X_test.shape}")
            logger.info(f"y Train Shape : {y_train.shape}")
            logger.info(f"y Test Shape : {y_test.shape}")

            return (
                X_train,
                X_test,
                y_train,
                y_test
            )

        except Exception as e:

            logger.error("Train-Test Split failed.")

            raise CustomException(e, sys)
