import os
from google.cloud import aiplatform

PROJECT_ID = os.getenv("PROJECT_ID")
REGION = os.getenv("REGION", "us-central1")
BUCKET = os.getenv("BUCKET")
MODEL_DISPLAY_NAME = "iris-pickle-model"
ENDPOINT_DISPLAY_NAME = "iris-endpoint"

aiplatform.init(project=PROJECT_ID, location=REGION, staging_bucket=BUCKET)

# Upload model from pickle using prebuilt sklearn container
model = aiplatform.Model.upload(
    display_name=MODEL_DISPLAY_NAME,
    artifact_uri=f"gs://{BUCKET}/models/",
    serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-5:latest",
)

# Deploy model
endpoint = model.deploy(
    deployed_model_display_name="iris-deployed",
    endpoint_display_name=ENDPOINT_DISPLAY_NAME,
    machine_type="n1-standard-2",
)

print("✅ Models deployed at endpoint:", endpoint.resource_name)
