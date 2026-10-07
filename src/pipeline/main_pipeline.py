from src.pipeline.data_pipeline import DataPipeline
from src.pipeline.training_pipeline import TrainingPipeline


def run_all():

    print("=" * 60)
    print("RUNNING COMPLETE ML PIPELINE")
    print("=" * 60)

    # Data Pipeline
    DataPipeline().run_pipeline()

    # Flight Model Training
    TrainingPipeline().run_pipeline("flight")

    # Hotel Model Training
    TrainingPipeline().run_pipeline("hotel")

    print("=" * 60)
    print("ALL PIPELINES COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    run_all()
