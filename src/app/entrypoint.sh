#!/bin/bash

pwd
ls
uvicorn --version
uvicorn main:app --reload
