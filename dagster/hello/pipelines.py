from dagster import pipeline

from .solids import hello_world


@pipeline
def hello_world_pipeline():
    hello_world()


def define_hello_world_pipeline():
    return hello_world_pipeline
