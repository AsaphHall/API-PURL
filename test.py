import requests
import json
from link_api_calls import *

####################################################################################################################
#   Test 1
#   diese Funktion ermöglicht die Eingabe des Qualitätsnamens als Variable
#   {} + .format() fügt Varibale zwischen geschw. Klammern ein
####################################################################################################################
resp = requests.get("https://nomad-hzb-ce.de/nomad-oasis/gui/artifacts.js")
doc = json.loads(resp.content.decode('ascii')[24:-2])

import jmespath
name = "CyclicVoltammetry"
res = jmespath.search("[?name == 'baseclasses.chemical_energy.cyclicvoltammetry']", doc['metainfo']['packages'])[0]
section = jmespath.search("[?name == '{}']".format(name),  res["section_definitions"])[0]

#print(section["links"])

####################################################################################################################
#   Test 2
#   Hier sollen mithilfe einer EntryID alle Links des Entries extrahiert werden
#   Idee: ID -> EntryData -> DefQualName (Pfad) aus den Section Defs -> Get Link via Pfad
####################################################################################################################

#ce_entry_id = "kv6JW1Gdzo7yzaIW-6CfOhZBOgdK"
#token = t_get_token(nomad_ce_url,name_t)
#data = get_entry_data(ce_entry_id,token,nomad_ce_url)
#with open("ce_entry_data.json","x") as df:
#    json.dump(data,df,indent = 4)


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


print("Namelist: ")
print(name_list)
print("Sectionlist: ")
print(section_list)
print("QualNameList: ")
print(qual_name_list)

#Bis hier funktioniert alles :)


i = 0
with open("artifact_data.json","r") as df2:
    #data = json.loads(df2.content.decode('ascii')[24:-2])
    for name in name_list:
        try:
            path = qual_name_list[i]
            #print("Name: "+name+", Pfad: "+path )
            res = jmespath.search("[?name == '{}']".format(path), doc['metainfo']['packages'])[0]
            section = jmespath.search("[?name == '{}']".format(name),  res["section_definitions"])[0]
            print(section["links"])
            i = i+1
            
        except IndexError:
            i=i+1
            print("Error")
        except KeyError:
            print("Kein Link")