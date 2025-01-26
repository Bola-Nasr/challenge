#!/bin/bash
if [ ! -f data_loaded.flag ]; then
  echo "Loading initial data..."
  cd backend && python3 load_data.py
  touch ../data_loaded.flag
else
  echo "Data already loaded. Skipping data load step."
fi

docker-compose up --build