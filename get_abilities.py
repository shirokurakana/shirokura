from os import path
import pandas as pd
import re
import json

cwd = path.dirname(__file__)

with open(path.join(cwd,'card.html'),'r',encoding='utf-8') as f:
    text = f.read()

out = {}
df = pd.read_html(text, encoding='utf-8', header=0)[0]
cards = list(df.T.to_dict().values())
for card in cards:
    index = card['编号'] - 1
    out[str(index)] = card['名称']
    trans = [x for x in re.split('[，。]', card['效果与备注（非官方）']) if x]
    out[f'{index}_0'] = trans

with open(path.join(cwd,'abilities.js'),'w',encoding='utf-8') as f:
    json.dump(out,f,indent=4,ensure_ascii=False)
