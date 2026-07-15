#!/bin/bash

mkdir -p /logs/verifier

pytest /tests/test_outputs.py
RESULT=$?

echo "{}" > /logs/verifier/ctrf.json

if [ $RESULT -eq 0 ]; then
    echo 1 > /logs/verifier/reward.txt
else
    echo 0 > /logs/verifier/reward.txt
fi

exit 0