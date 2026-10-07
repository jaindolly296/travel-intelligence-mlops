from src.pipeline.data_pipeline import DataPipeline
from src.pipeline.training_pipeline import TrainingPipeline

if __name__ == "__main__":

    print("=" * 60)
    print("Travel Intelligence MLOps")
    print("=" * 60)

    # Run Data Pipeline
    data_pipeline = DataPipeline()
    data_pipeline.run_pipeline()

    training_pipeline = TrainingPipeline()

    print("Training Flight Model...")
    training_pipeline.run_pipeline(model_type="flight")

    print("Training Hotel Model...")
    training_pipeline.run_pipeline(model_type="hotel")

    print("=" * 60)
    print("Pipeline Completed Successfully")
    print("=" * 60)
