#!/usr/bin/env bash

FWDIR="$(cd `dirname "${BASH_SOURCE-$0}"`; pwd)"

cd ${FWDIR}

admin() {

python3 ../src/atm_admin.py

}


case "$1" in
    start)
        admin
        ;;
    *)
        echo $"Usage: $0 {start}"
        exit 2
esac

