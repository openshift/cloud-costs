#!/bin/bash

TOP=/home/blentz/git/budget

cd $TOP
source ${TOP}/env/bin/activate
python -m 'budget.scripts.gcp_billing_import' ${TOP}/development.ini
