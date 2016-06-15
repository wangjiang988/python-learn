#!/usr/bin/env bash

FWDIR="$(cd `dirname "${BASH_SOURCE-$0}"`; pwd)"

cd ${FWDIR}

shopping() {

python3 ../src/shopping.py

}

case "$1" in
    start)
        shopping
        ;;
    *)
        echo $"Usage: $0 {start}"
        exit 2
esac


