#!/bin/bash

OUTPUT_ZIP=aws.zip

zip -r ${OUTPUT_ZIP} pybitcoin lambda_function.py
