#!/bin/bash

TOP=/home/blentz/git/budget

cd $TOP
source /home/blentz/bin/prod.env
source ${TOP}/env/bin/activate
# TODO
# python -m 'budget.scripts.openshift_stats' ${TOP}/development.ini
# TODO
# python -m 'budget.scripts.openshift_v3_stats' ${TOP}/development.ini
