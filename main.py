import json
import requests
import jmespath
from link_api_calls import *

resp = requests.get("https://nomad-hzb-ce.de/nomad-oasis/gui/artifacts.js")
doc = json.loads(resp.content.decode('ascii')[24:-2])

section_list = []
with open("ce_entry_data.json","r") as df:
    data = json.load(df)
for sections in data['data']['section_defs']:
    section_list.append(sections['definition_qualified_name'])

### Get Path from QualityName

qual_name_list = []
for string in section_list:
    path = string[::-1]
    slice_indicator = path.index(".")
    path = path[slice_indicator+1::]
    path = path [::-1]
    qual_name_list.append(path)


### Get last word after '.' from path -> CyclicVoltammetry of baseclasses.etc.etc.CyclicVoltammetry
name_list = []
for string in section_list:
    name = string
    name = name[::-1]
    slice_indicator = name.index(".")
    name = name[slice_indicator-1::-1]
    name_list.append(name)

i = 0
with open("artifact_data.json","r") as df2:
    #data = json.loads(df2.content.decode('ascii')[24:-2])
    for name in name_list:
        try:
            path = qual_name_list[i]
            res = jmespath.search("[?name == '{}']".format(path), doc['metainfo']['packages'])[0]
            section = jmespath.search("[?name == '{}']".format(name),  res["section_definitions"])[0]
            print(section["links"])
            i = i+1
            
        except IndexError:
            i=i+1
            print("Error")
        except KeyError:
            print("Kein Link")