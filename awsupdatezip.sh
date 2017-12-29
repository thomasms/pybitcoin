#!/bin/bash

OUTPUT_ZIP=aws.zip

zip -r ${OUTPUT_ZIP} dependencies exchanges util lambda_function.py
