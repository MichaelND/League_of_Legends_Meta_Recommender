#!/usr/bin/env bash

PUB_DIR=~/my_www/League_Project

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

if cp -rf ~/progParadigms/ParadigmsFinal/www/* ~/my_www/League_Project; then
    echo "Successful copy"
else
    echo "Failed copy"
fi
