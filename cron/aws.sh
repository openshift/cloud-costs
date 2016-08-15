#!/bin/bash

TOP=${HOME}/git/cloud-costs

cd $TOP
source /home/blentz/bin/prod.env
source ${TOP}/env/bin/activate
python -m 'budget.scripts.aws_billing_import' ${TOP}/production.ini
python -m 'budget.scripts.aws_pricing_data' ${TOP}/production.ini
