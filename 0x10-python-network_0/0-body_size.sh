#!/bin/bash
# Get the byte size of the HTTP response header for a given URL.
curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
