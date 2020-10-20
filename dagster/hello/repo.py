from dagster import pipeline, repository, solid


@solid
def hello_world(context):
    context.log.info("Hello, world!")


@pipeline
def hello_world_pipeline():
    hello_world()


@repository
def hello_world_repository():
    return [hello_world_pipeline]

