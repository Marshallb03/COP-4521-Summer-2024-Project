#!/bin/bash

# Find and print the local IP address on a WSL environment

ip addr show | awk '/inet / {print $2}' | grep -v '127.0.0.1' | cut -d/ -f1
