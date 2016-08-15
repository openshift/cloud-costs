#!/bin/bash

TOP=${HOME}/git/cloud-costs

cd $TOP
source ${TOP}/env/bin/activate
python -m 'budget.scripts.aws_inventory_update' ${TOP}/production.ini
