from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "owner": "Dolly",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
}


with DAG(

    dag_id="travel_intelligence_training_pipeline",

    description="Travel Intelligence End-to-End MLOps Pipeline",

    start_date=datetime(2026, 1, 1),

    schedule=None,

    catchup=False,

    default_args=default_args,

    tags=["travel", "mlops", "machine-learning"]

) as dag:

    start = BashOperator(

        task_id="start_pipeline",

        bash_command="""
        echo "========================================"
        echo "Travel Intelligence MLOps Pipeline"
        echo "Pipeline Started"
        echo "========================================"
        """

    )

    data_pipeline = BashOperator(

        task_id="data_pipeline",

        bash_command="""
        cd /opt/airflow/project
        python -m src.pipeline.data_pipeline
        """

    )

    flight_training = BashOperator(

        task_id="flight_model_training",

        bash_command="""
        cd /opt/airflow/project
        python -c "from src.pipeline.training_pipeline import TrainingPipeline; TrainingPipeline().run_pipeline('flight')"
        """

    )

    hotel_training = BashOperator(

        task_id="hotel_model_training",

        bash_command="""
        cd /opt/airflow/project
        python -c "from src.pipeline.training_pipeline import TrainingPipeline; TrainingPipeline().run_pipeline('hotel')"
        """

    )

    finish = BashOperator(

        task_id="finish_pipeline",

        bash_command="""
        echo "========================================"
        echo "Pipeline Completed Successfully"
        echo "========================================"
        """

    )

    start >> data_pipeline >> flight_training >> hotel_training >> finish
