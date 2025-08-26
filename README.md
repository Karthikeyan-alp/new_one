# Vertex AI MLOps with Pickle Model + GitHub Actions

This repo demonstrates:
- Train locally, save pickle
- Push to GitHub
- CI/CD deploys to Vertex AI

## Steps

### 1. Train Locally
```bash
cd scripts
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python generate_model.py
```

This saves `models/iris_model.pkl`.

Upload the `models/` folder to your GCS bucket manually or via script.

### 2. GitHub Setup
Add secrets in repo settings → Secrets → Actions:
- `GOOGLE_CLOUD_CREDENTIALS`: JSON key of service account with Vertex AI permissions
- `GCP_PROJECT_ID`
- `GCP_REGION` (e.g., us-central1)
- `GCS_BUCKET`

### 3. Trigger Deployment
- Push to `main`
- or Run workflow manually in GitHub Actions tab.

### 4. Check Deployment
Go to **Vertex AI → Endpoints** in GCP console. Your model is deployed 🚀.

