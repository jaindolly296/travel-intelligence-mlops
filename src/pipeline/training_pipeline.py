import pandas as pd

from src.config.configuration import Configuration

from src.components.feature_selection import FeatureSelection
from src.components.data_splitter import DataSplitter
from src.components.data_preprocessing import DataPreprocessing
from src.components.model_trainer import ModelTrainer
from src.components.hyperparameter_tuner import HyperparameterTuner
from src.components.model_evaluation import ModelEvaluation
from src.components.model_saver import ModelSaver
from src.components.mlflow_tracker import MLflowTracker

from src.logger import logger


class TrainingPipeline:

    def __init__(self):
        self.config = Configuration()

    def run_pipeline(self, model_type: str):

        logger.info("=" * 60)
        logger.info("Training Pipeline Started")
        logger.info("=" * 60)

        # =====================================================
        # Model Training Configuration
        # =====================================================

        training_config = self.config.get_model_training_config(
            model_type
        )

        # =====================================================
        # Load Processed Dataset
        # =====================================================

        processed_path = training_config.dataset_path

        logger.info(
            f"Loading dataset from: {processed_path}"
        )

        clean_dataset = pd.read_csv(processed_path)

        logger.info(f"Dataset Shape : {clean_dataset.shape}")

        # =====================================================
        # Feature Selection
        # =====================================================

        feature_selector = FeatureSelection()

        X, y = feature_selector.select_features(

            df=clean_dataset,

            target_column=training_config.target_column,

            feature_columns=(
                training_config.categorical_columns
                + training_config.numerical_columns
            )

        )

        # =====================================================
        # Train Test Split
        # =====================================================

        splitter = DataSplitter()

        X_train, X_test, y_train, y_test = splitter.split_data(
            X,
            y
        )

        # =====================================================
        # Data Preprocessing
        # =====================================================

        preprocessing = DataPreprocessing()

        X_train, X_test, preprocessor = preprocessing.preprocess(

            X_train,
            X_test,

            training_config.categorical_columns,
            training_config.numerical_columns

        )

        # =====================================================
        # Train Selected Models
        # =====================================================

        trainer = ModelTrainer(
            selected_models=training_config.selected_models
        )

        trained_models = trainer.train_models(
            X_train,
            y_train
        )

        # =====================================================
        # Hyperparameter Tuning
        # =====================================================

        if "XGBoost" in trained_models:

            logger.info("=" * 60)
            logger.info("Starting XGBoost Hyperparameter Tuning")
            logger.info("=" * 60)

            tuner = HyperparameterTuner()

            tuned_model = tuner.tune_model(

                model=trained_models["XGBoost"],

                param_grid=self.config.get_xgboost_param_grid(),

                X_train=X_train,

                y_train=y_train

            )

            trained_models["XGBoost"] = tuned_model

            logger.info("XGBoost tuning completed.")

        # =====================================================
        # Evaluate Models
        # =====================================================

        evaluator = ModelEvaluation()

        best_model_name, best_model, results = evaluator.evaluate_models(
            trained_models,
            X_test,
            y_test
        )

        # =====================================================
        # MLflow Tracking
        # =====================================================

        logger.info("=" * 60)
        logger.info("Logging Best Model to MLflow")
        logger.info("=" * 60)

        tracker = MLflowTracker()

        params = {}

        if hasattr(best_model, "get_params"):
            params = best_model.get_params()

        tracker.log_complete_model(

            model_name=best_model_name,

            model=best_model,

            metrics={
                "R2": results[best_model_name]["R2"],
                "RMSE": results[best_model_name]["RMSE"],
                "MAE": results[best_model_name]["MAE"]
            },

            params=params

        )

        logger.info("Best model logged to MLflow successfully.")

        # =====================================================
        # Save Best Model
        # =====================================================

        saver = ModelSaver()

        saver.save_model(

            model=best_model,

            preprocessor=preprocessor,

            model_name=training_config.model_name

        )

        # =====================================================
        # Print Leaderboard
        # =====================================================

        logger.info("=" * 60)
        logger.info("Model Leaderboard")
        logger.info("=" * 60)

        for model_name, metrics in results.items():

            logger.info(
                f"{model_name:<25}"
                f"R2={metrics['R2']:.4f}   "
                f"RMSE={metrics['RMSE']:.4f}   "
                f"MAE={metrics['MAE']:.4f}"
            )

        logger.info("=" * 60)
        logger.info(f"Best Model : {best_model_name}")
        logger.info("=" * 60)
        logger.info("Training Pipeline Completed")

        return {

            "best_model": best_model_name,

            "results": results

        }
