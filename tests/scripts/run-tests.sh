#!/bin/bash

#
# Copyright (c) 2022, 2023, Oracle and/or its affiliates.
# Licensed under the Universal Permissive License v 1.0 as shown at
# https://oss.oracle.com/licenses/upl.
#

# Run compatability tests
set -e

# Set the following to include long running streaming tests
# INCLUDE_LONG_RUNNING=true

echo "create logs directory"
mkdir -p logs

echo "Coherence CE 22.06.5"
COHERENCE_CLIENT_REQUEST_TIMEOUT=180.0 \
  COHERENCE_IO_JSON_DEBUG=false \
  make clean test-cluster-shutdown remove-app-images build-test-images test-cluster-startup just-wait test
  make dump-logs test-cluster-shutdown
  mv ./tests/utils/run-logs.txt ./logs/server-run-logs-clear.txt
  mv ./client-log.txt ./logs/client-log-clear.txt

echo "Coherence CE 22.06.5 with SSL"
RUN_SECURE=true COHERENCE_IGNORE_INVALID_CERTS=true \
  COHERENCE_IO_JSON_DEBUG=false \
  COHERENCE_TLS_CERTS_PATH=$(pwd)/tests/utils/certs/guardians-ca.crt \
  COHERENCE_TLS_CLIENT_CERT=$(pwd)/tests/utils/certs/star-lord.crt \
  COHERENCE_TLS_CLIENT_KEY=$(pwd)/tests/utils/certs/star-lord.pem \
  COHERENCE_CLIENT_REQUEST_TIMEOUT=180.0 \
  PROFILES=,secure make clean certs test-cluster-shutdown remove-app-images \
                                                  build-test-images test-cluster-startup just-wait test
  make dump-logs test-cluster-shutdown
  mv ./tests/utils/run-logs.txt ./logs/server-run-logs-ssl.txt
  mv ./client-log.txt ./logs/client-log-ssl.txt
