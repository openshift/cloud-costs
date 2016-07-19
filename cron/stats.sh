#!/bin/bash

TOP=${HOME}/git/cloud-costs

cd $TOP
source ${HOME}/bin/prod.env
source ${TOP}/env/bin/activate
# TODO
# python -m 'budget.scripts.openshift_stats' ${TOP}/development.ini
# TODO
# python -m 'budget.scripts.openshift_v3_stats' ${TOP}/development.ini
