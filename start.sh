#!/bin/bash
set -e
echo "Starting Blockchain-Based Supply Chain Tracker..."
uvicorn app:app --host 0.0.0.0 --port 9061 --workers 1
