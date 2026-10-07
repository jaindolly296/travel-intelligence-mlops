from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data Directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MERGED_DATA_PATH = PROCESSED_DATA_DIR / "final_dataset.csv"
CLEAN_DATA_PATH = PROCESSED_DATA_DIR / "clean_dataset.csv"
# Models
MODELS_DIR = PROJECT_ROOT / "models"

# Artifacts
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"

# Configs
CONFIGS_DIR = PROJECT_ROOT / "configs"

# Logs
LOG_DIR = PROJECT_ROOT / "logs"

# MLflow
MLFLOW_DIR = PROJECT_ROOT / "mlruns"
