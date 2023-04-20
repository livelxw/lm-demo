#!/bin/sh

nohup sh ./run-torchserve.sh >torchserve.log 2>&1 &

while ! timeout 1 bash -c "echo > /dev/tcp/localhost/7070"; do
    echo "Waiting Torchserve grpc service to launch on 7070..."
    sleep 1
done

echo "Torchserve grpc service launched!"

python -u src/ts_scripts/console_client.py
