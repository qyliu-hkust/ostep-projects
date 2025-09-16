#! /bin/bash

if ! [[ -x mycat ]]; then
    echo "mycat executable does not exist"
    exit 1
fi

../../tester/run-tests.sh $*


