#!/usr/bin/env bash
set -euo pipefail
SERVICE="cemmind-api"
REGION="us-central1"

# Deploy from source with conservative, stable runtime settings
gcloud run deploy "$SERVICE" \
  --source . \
  --region "$REGION" \
  --allow-unauthenticated \
  --port=8080 \
  --memory=512Mi \
  --cpu=1 \
  --concurrency=40 \
  --timeout=300 \
  --min-instances=1 \
  --max-instances=3 \
  --cpu-boost \
  --execution-environment=gen2

# Print URL
gcloud run services describe "$SERVICE" --region "$REGION" \
  --format='value(status.url)'
