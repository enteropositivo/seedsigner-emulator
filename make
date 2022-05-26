#!/bin/bash

echo "Copy content to SeedSigner"

cp -r seedsigner-emulator/* seedsigner/src/seedsigner/

# Run SeedSigner

cd seedsigner/src/
python3 main.py
