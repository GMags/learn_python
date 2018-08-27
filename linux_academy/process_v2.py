#!/usr/bin/python3.6

import os
import glob
import json
import shutil
import math

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exits")

# Get a list of the reciepts 
reciepts = glob.glob('./test_data/reciept-[0-9]*.json')
subtotal = 0.0

for reciept in reciepts:
    with open(reciept) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    #name = reciept.split('/')[-1]
    #destination = f"./processed/{name}"
    destination = reciept.replace('new', 'processed')
    shutil.move(reciept, destination)
    print(f"moved '{reciept}' to '{destination}'")

#print("Reciept subtotal: $%.2f" % subtotal)
print(f"Reciept subtotal: ${round(subtotal, 2)}")
