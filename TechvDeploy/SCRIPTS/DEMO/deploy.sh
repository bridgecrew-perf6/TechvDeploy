#!/bin/bash

branch=$1
d_id=$2
log=/tmp/${d_id}.txt
echo $log


echo "deploying started for ${d_id} with branch ${branch}" >$log

echo "##########" >>$log
