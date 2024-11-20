#!/bin/bash
sudo ./start-init.sh
uvicorn back.main:app --reload &
FOO_PID=$!
/usr/bin/node /home/oleg/Documents/IDEAProjects/web-lab-back/proxy/main.js
kill $FOO_PID
