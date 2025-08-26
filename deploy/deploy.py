import os
from google.cloud import aiplatform

PROJECT_ID = os.getenv("PROJECT_ID")
REGION = os.getenv("REGION", "us-central1")
BUCKET = os.getenv("BUCKET")
MODEL_DISPLAY_NAME = "iris-pickle-model"
ENDPOINT_DISPLAY_NAME = "iris-endpoint"

aiplatform.init(project=PROJECT_ID, location=REGION, staging_bucket=BUCKET)

# Upload model
model = aiplatform.Model.upload(
    display_name="iris-model",
    artifact_uri=f"gs://{BUCKET}/models/",
    serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-0:latest",
)

print("Model uploaded:", model.resource_name)

# Create endpoint
endpoint = aiplatform.Endpoint.create(
    display_name="iris-endpoint"
)

print("Endpoint created:", endpoint.resource_name)

# Deploy model to endpoint
deployed_model = model.deploy(
    endpoint=endpoint,
    machine_type="n1-standard-2"
)

print("Model deployed to endpoint:", endpoint.resource_name)