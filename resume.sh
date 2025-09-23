#!/usr/bin/env bash
set -e
gcloud config set account shilpa.aiskill@gmail.com >/dev/null
gcloud config set project om-cemmind-proto >/dev/null
echo "✅ Active: $(gcloud config get-value core/account) / $(gcloud config get-value core/project)"
