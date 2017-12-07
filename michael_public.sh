#!/usr/bin/env bash

PUB_DIR=/home/mwang6/public_html/league_project

if rm -rf ${PUB_DIR}; then
    echo "Successful rm"
else
    echo "Failed rm"
fi

if mkdir ${PUB_DIR}; then
    echo "Successful mkdir"
else
    echo "Failed mkdir"
fi

if cp -rf ~/public-paradigms-fall17/ParadigmsFinal/www* ${PUB_DIR}; then
    echo "Successful copy"
else
    echo "Failed copy"
fi
