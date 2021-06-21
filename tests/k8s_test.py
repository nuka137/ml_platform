import airflow
from datetime import timedelta
from airflow import DAG
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator


dag = DAG(
    dag_id="k8s_test",
    default_args={
        "owner": "admin",
        "start_date": airflow.utils.dates.days_ago(2)
    },
    description="Airflow DAG on k8s",
    schedule_interval=timedelta(days=1),
    dagrun_timeout=timedelta(minutes=60),
)

k1 = KubernetesPodOperator(
    namespace="airflow",
    task_id="k8s_test_op",
    name="k8s_test_op_container",
    image="ubuntu:latest",
    image_pull_policy="IfNotPresent",
    cmds=["bash", "-cx"],
    arguments=["echo Hello"],
    in_cluster=True,
    is_delete_operator_pod=True,
    dag=dag
)

k1