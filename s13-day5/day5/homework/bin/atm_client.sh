#!/usr/bin/env bash

FWDIR="$(cd `dirname "${BASH_SOURCE-$0}"`; pwd)"

cd ${FWDIR}

main() {

python3 ../src/atm_client.py

}


case "$1" in
    start)
        main
        ;;
    *)
        echo $"Usage: $0 {start}"
        exit 2
esac



