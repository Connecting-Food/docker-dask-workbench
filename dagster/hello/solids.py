from dagster import solid


@solid
def hello_world(context):
    context.log.info("Hello, world!")
