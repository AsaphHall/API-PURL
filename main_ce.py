import json
import requests
import jmespath
from link_api_calls import *

entry_id = "FTbatW2VKQo5Omcy-wl0owMB1TSe"

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
    path = string[::-1]
    slice_indicator = path.index(".")
    path = path[slice_indicator+1::]
    path = path [::-1]
    path_list.append(path)
        


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
    control_file_2 = open("CE_Links.txt","w")
    #data = json.loads(df2.content.decode('ascii')[24:-2])
    for name in name_list:     
        try:
            path = path_list[i]
            res = jmespath.search("[?name == '{}']".format(path), doc['metainfo']['packages'])[0]
            section = jmespath.search("[?name == '{}']".format(name),  res["section_definitions"])[0]
            x = str(section["links"])
            control_file_2.write("\n"+name+": "+x)
            #print(section["links"])
            i = i+1
            
        except IndexError:
            i=i+1
            control_file_2.write("\n"+name+": Error")
        except KeyError:
            i = i+1
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