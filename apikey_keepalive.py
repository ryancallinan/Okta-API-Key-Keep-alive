#!/usr/bin/env python3.4

import requests
import json
import argparse
from argparse import ArgumentParser
from datetime import datetime

parser = ArgumentParser()
parser.add_argument("cfg",nargs='?',default='api_keys.json',help="config file")
args = parser.parse_args()
cfg = args.cfg

with open(cfg) as json_file:
  apikeys = json.load(json_file)
  dateTime = datetime.now()
  for key in apikeys:
     r = requests.request("POST", "https://" + key + "/api/v1/users?q=cenet&limit=1", headers={'Authorization': "SSWS "+ apikeys[key], 'Content-Type':'application/json'})
     print(r, dateTime)
