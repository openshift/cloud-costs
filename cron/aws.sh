#!/bin/bash

TOP=/home/blentz/git/budget

cd $TOP
source /home/blentz/bin/prod.env
source ${TOP}/env/bin/activate
python -m 'budget.scripts.aws_billing_import' ${TOP}/development.ini
python -m 'budget.scripts.aws_pricing_data' ${TOP}/development.ini
