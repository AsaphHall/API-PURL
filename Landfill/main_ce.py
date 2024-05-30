import json
import requests
import jmespath
from link_api_calls import *

entry_id2 = "FTbatW2VKQo5Omcy-wl0owMB1TSe"
entry_id = "kv6JW1Gdzo7yzaIW-6CfOhZBOgdK"

token = t_get_token(nomad_ce_url,name_t)
entry_data = get_entry_data(entry_id,token,nomad_ce_url)

with open("ce_entry_data2.json","w") as f:
    json.dump(entry_data,f, indent=4)

resp = requests.get("https://nomad-hzb-ce.de/nomad-oasis/gui/artifacts.js")
doc = json.loads(resp.content.decode('ascii')[24:-2])

section_list = []
with open("ce_entry_data2.json","r") as df:
    data = json.load(df)
for sections in data['data']['section_defs']:
    section_list.append(sections['definition_qualified_name'])

### Get Path from QualityName

path_list = []
for string in section_list:
    path = string.rsplit(".",1)
    path_list.append(path[0])
        


### Get last word after '.' from path -> e.g. CyclicVoltammetry of baseclasses.etc.etc.CyclicVoltammetry
name_list = []
for string in section_list:
    name = string.split(".")
    name_list.append(name[-1])

i = 0
with open("artifact_data.json","r") as df2:
    control_file_2 = open("CE_Links.txt","w")
    #data = json.loads(df2.content.decode('ascii')[24:-2])
    for i,name in enumerate(name_list):     
        try:
            path = path_list[i]
            res = jmespath.search("[?name == '{}']".format(path), doc['metainfo']['packages'])[0]
            section = jmespath.search("[?name == '{}']".format(name),  res["section_definitions"])[0]
            x = str(section["links"])
            control_file_2.write("\n"+name+": "+x)
            
        except IndexError:
            control_file_2.write("\n"+name+": Error")
        except KeyError:
            control_file_2.write("\n"+name+": No Link")


control_file_1 = open("Quantities.txt","w")
for name in path_list:
    control_file_1.write("\n"+name)
control_file_1.close()
control_file_2.close()
print("\n"+"path_list"+"\n")
print(path_list)
print("\n"+"name_list"+"\n")
print(name_list)