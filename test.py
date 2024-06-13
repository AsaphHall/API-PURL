import json
import jmespath
 
 #LayerProperties (+ Link) Zeile: 50282 Package: 19 Section_Def: 9

with open("artifacts_ce.json") as f:
    data = json.load(f)
    print(data["metainfo"]["packages"][19]["section_definitions"][9]["name"])
    print(data["metainfo"]["packages"][19]["section_definitions"][9]["links"])



# atmosphere
print(data["metainfo"]["packages"][19]["section_definitions"][11]["sub_sections"][0]["name"])
print(data["metainfo"]["packages"][19]["section_definitions"][11]["sub_sections"][0]["links"])

#layer_type, input  = "data.layer.layer_type"
#layer_type = ['https://purl.archive.org/tfsco/TFSCO_00000007']
#data["metainfo"]["packages"][19]["section_definitions"][9]["quantities"][0]["links"]
print(data["metainfo"]["packages"][19]["section_definitions"][9]["quantities"][0]["name"])
print(data["metainfo"]["packages"][19]["section_definitions"][9]["quantities"][0]["links"])

#path_to_package = jmespath.search("[?name =='{}']".format(splitted_m_def[-2]), data["metainfo"]["packages"])[0]
#path_to_section_defs = jmespath.search("[?name =='{}']".format(splitted_m_def[-1]), path_to_package["section_definitions"])[0]