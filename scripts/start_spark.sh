#!/bin/bash

docker start spark-master
docker start  spark-worker-1

echo "Spark started"