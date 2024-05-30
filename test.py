#ce_nome_s.CE_NOME_CyclicVoltammetry
import json
import jmespath
from link_api_calls import *
from final_main import *
link_a = "ce_nome_s.CE_NOME_Chronoamperometry"
link_b = "ce_nome_s.CE_NOME_Chronocoulometry"
m_def = split_m_def(link_b)
print(m_def)
with open("artifacts_ce.json") as f:
    data = json.load(f)
    path_to_package = jmespath.search("[?name =='{}']".format(m_def[-2]), data["metainfo"]["packages"])[0]
    path_to_section_defs = jmespath.search("[?name =='{}']".format(m_def[-1]), path_to_package["section_definitions"])[0]
    print(path_to_section_defs['base_sections'])

base_sec = path_to_section_defs['base_sections'][0]
base_sec_split = base_sec.split("/")
path_2 = base_sec_split[2]
path_3 = base_sec_split[4]

path_to_link = jmespath.search("[?m_parent_index==`{}`]".format(path_2), data["metainfo"]["packages"])[0]
path_to_link_2 = jmespath.search("[?m_parent_index==`{}`]".format(path_3), path_to_link["section_definitions"])[0]
path_to_link_2 = jmespath.search("[?m_parent_index==`{}`]".format(path_3), path_to_link["subsections"])[0]

####Für Quantitäten [sub_sections] hinzufügen!


print(path_to_link_2["links"])
