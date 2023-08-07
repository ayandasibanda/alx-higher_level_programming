#!/bin/bash

# Checks if the environment variable PYFILE is set
if [ -z "$PYFILE" ]; then
  echo "Error: The PYFILE environment variable has not been set."
  exit 1
fi

# Checks if the specified Python file exists
if [ ! -f "$PYFILE" ]; then
  echo "Error: The specified Python file does not exist."
  exit 1
fi

# Run the Python script
python3 "$PYFILE"

