#!/bin/bash

TOP=/home/blentz/git/budget

cd $TOP
source ${TOP}/env/bin/activate
python -m 'budget.scripts.aws_inventory_update' ${TOP}/development.ini
