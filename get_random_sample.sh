#!/bin/bash

accounting_file=$SGE_ROOT/$SGE_CELL/common/accounting
date=`date +%Y%M%d`

awk -v outfile="sample-$date.txt" 'BEGIN  {srand()} !/^$/  { if (rand() <= .05 || FNR==1) print > outfile }' $accounting_file
