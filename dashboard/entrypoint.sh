#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Check if the node_modules directory exists.
if [ ! -d "node_modules" ]; then
  echo "Node modules not found. Running npm install..."
  npm install
fi

# Execute the command passed to this script (from the Dockerfile's CMD)
exec "$@"
