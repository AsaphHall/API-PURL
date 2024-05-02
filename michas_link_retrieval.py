import requests
import json

# resp = requests.get("https://nomad-hzb-ce.de/nomad-oasis/gui/artifacts.js")
# doc = json.loads(resp.content.decode('ascii')[24:-2])

# import jmespath
# # 'name': 'baseclasses.chemical_energy.cyclicvoltammetry',
# res = jmespath.search("[?name == 'baseclasses.chemical_energy.cyclicvoltammetry']", doc['metainfo']['packages'])[0]
# section = jmespath.search("[?name == 'CyclicVoltammetry']",  res["section_definitions"])[0]

# section["links"]



##########################################
#   TEST
#
########################################

resp = requests.get("https://nomad-hzb-ce.de/nomad-oasis/gui/artifacts.js")
doc = json.loads(resp.content.decode('ascii')[24:-2])

import jmespath
name = "CyclicVoltammetry"
pfad = "baseclasses.chemical_energy.cyclicvoltammetry"
res = jmespath.search("[?name == '{}']".format(pfad), doc['metainfo']['packages'])[0]
section = jmespath.search("[?name == '{}']".format(name),  res["section_definitions"])[0]

print(section["links"])