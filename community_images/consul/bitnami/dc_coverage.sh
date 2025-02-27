#!/bin/bash

set -x
set -e

SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

# shellcheck disable=SC1091
. "${SCRIPTPATH}"/../../common/scripts/bash_helper.sh

JSON_PARAMS="$1"

JSON=$(cat "$JSON_PARAMS")

echo "Json params for docker compose coverage = $JSON"

PROJECT_NAME=$(jq -r '.project_name' < "$JSON_PARAMS")

# Container name for consul-node1
CONTAINER_NAME="${PROJECT_NAME}"-consul-node1-1

# Wait for all the member nodes to get in sync
sleep 20

# Exec into consul server(node1) and run coverage scrip(Additional: This script also has instructions to register a sample service)
docker exec -i "${CONTAINER_NAME}" bash -c /opt/bitnami/scripts/coverage_script.sh

# log for debugging
docker inspect "${CONTAINER_NAME}"

# find non-tls and tls port
docker inspect "${CONTAINER_NAME}" | jq -r ".[].NetworkSettings.Ports.\"8300/tcp\"[0].HostPort"
docker inspect "${CONTAINER_NAME}" | jq -r ".[].NetworkSettings.Ports.\"8301/tcp\"[0].HostPort"
docker inspect "${CONTAINER_NAME}" | jq -r ".[].NetworkSettings.Ports.\"8301/udp\"[0].HostPort"
docker inspect "${CONTAINER_NAME}" | jq -r ".[].NetworkSettings.Ports.\"8500/tcp\"[0].HostPort"
docker inspect "${CONTAINER_NAME}" | jq -r ".[].NetworkSettings.Ports.\"8600/tcp\"[0].HostPort"
docker inspect "${CONTAINER_NAME}" | jq -r ".[].NetworkSettings.Ports.\"8600/udp\"[0].HostPort"

# Checking Consul members list in all server and client nodes
docker exec -i "${PROJECT_NAME}"-consul-node2-1 consul members
docker exec -i "${PROJECT_NAME}"-consul-node3-1 consul members
docker exec -i "${PROJECT_NAME}"-consul-node4-1 consul members

# exec into consul client(node4) and run coverage script
docker exec -i "${PROJECT_NAME}"-consul-node4-1 bash -c /opt/bitnami/scripts/coverage_script.sh

# Query our service using DNS API on consul-node1 via consul-node3
docker exec -i "${PROJECT_NAME}"-consul-node3-1 bash -c /opt/bitnami/scripts/coverage_script.sh

# Deregistering/removing sample service in consul-node1
docker exec -i "${CONTAINER_NAME}" consul services deregister /consul.d/sample_service.json   

# Shutting down consul
docker exec -i "${PROJECT_NAME}"-consul-node2-1 consul leave