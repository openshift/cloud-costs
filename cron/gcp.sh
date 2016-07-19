#!/bin/bash

TOP=${HOME}/git/cloud-costs

cd $TOP
source ${TOP}/env/bin/activate
python -m 'budget.scripts.gcp_billing_import' ${TOP}/development.ini
