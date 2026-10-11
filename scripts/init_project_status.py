#!/usr/bin/env python3
"""Cria baseline explícito, sem sobrescrever status existente."""
import argparse
from datetime import date
import json
from pathlib import Path
from project_status import validate

parser=argparse.ArgumentParser()
parser.add_argument('directory',type=Path)
parser.add_argument('--repository',required=True)
parser.add_argument('--publish',action='store_true')
args=parser.parse_args()
data={'schema_version':1,'repository':args.repository,'name':args.repository.split('/')[-1], 'publish':args.publish,'updated_at':date.today().isoformat(),'scope':{'name':'Base a definir','revision':1},'milestones':[]}
validate(data)
args.directory.mkdir(parents=True,exist_ok=True)
with (args.directory/'PROJECT_STATUS.json').open('x',encoding='utf-8') as handle:
    json.dump(data,handle,ensure_ascii=False,indent=2)
    handle.write('\n')
print('PROJECT_STATUS.json criado: 0%; definir escopo antes de estimar progresso.')
