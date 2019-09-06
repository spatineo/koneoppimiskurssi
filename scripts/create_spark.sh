#!/bin/bash

docker run --name spark-master -d -h spark-master -e ENABLE_INIT_DAEMON=false -d bde2020/spark-master:2.4.3-hadoop2.7

docker run --name spark-worker-1 -d --link spark-master:spark-master -e ENABLE_INIT_DAEMON=false -d bde2020/spark-worker:2.4.3-hadoop2.7

echo "Spark created"