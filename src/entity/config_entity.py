from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    users_path: Path
    flights_path: Path
    hotels_path: Path


@dataclass(frozen=True)
class DataValidationConfig:
    validation_report_path: Path


@dataclass(frozen=True)
class DataTransformationConfig:
    processed_users_path: Path
    processed_flights_path: Path
    processed_hotels_path: Path

@dataclass(frozen=True)
class DataMergingConfig:

    processed_users_path: Path
    processed_flights_path: Path
    processed_hotels_path: Path

    merged_data_path: Path


@dataclass(frozen=True)
class DataCleaningConfig:

    clean_data_path: Path
