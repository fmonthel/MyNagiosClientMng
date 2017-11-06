#!/bin/sh
 
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no flaprdmon01@flaprdmon01.flox-arts.in <<EOF
  cd /srv/flaprdmon01/tools/MyNagiosClientMng
  git reset --hard origin/master
  git pull origin
  exit
EOF
