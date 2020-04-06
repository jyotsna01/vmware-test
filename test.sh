#!/bin/bash

echo "===================="
echo "hostname: $(hostname)"
echo "pwd: $(pwd)"
echo "id: $(id)"

echo "===================="
echo "Running test..."
python3 -m pytest \
  --junit-xml=${BUILD_SOURCESDIRECTORY}/test_result.xml --durations=25 \
  --numprocesses=4 --dist=loadfile \
  ${BUILD_SOURCESDIRECTORY}/test/
exitCode=$?

echo "===================="
echo "Exit code ${exitCode}"
exit ${exitCode}
