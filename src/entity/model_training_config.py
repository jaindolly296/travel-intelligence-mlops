from dataclasses import dataclass
from pathlib import Path


@dataclass
class ModelTrainingConfig:

    # Dataset
    dataset_path: Path

    # Target
    target_column: str

    # Feature Lists
    categorical_columns: list
    numerical_columns: list

    # Models
    selected_models: list

    # Saved model filename
    model_name: str
