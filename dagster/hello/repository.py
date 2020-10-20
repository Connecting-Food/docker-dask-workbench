from dagster import repository

from .pipelines import define_hello_world_pipeline


@repository
def hello_world_repository():
    return {
        "pipelines": {
            "hello_world_pipeline": define_hello_world_pipeline,
        },
    }

