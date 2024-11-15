#!/bin/bash
./start-init.sh
uvicorn back.main:app --reload