#!/bin/bash

ENV_FILE=".env.$1"

if [ -f "$ENV_FILE" ]; then
  cp "$ENV_FILE" .env
  echo "✔️ Switched to $ENV_FILE"
else
  echo "❌ Environment file $ENV_FILE does not exist"
  exit 1
fi
