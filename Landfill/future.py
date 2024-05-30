import requests
import jmespath
import json



#get_links_of_section(`chemical_energy.CE_NOME_CyclicVoltammetry', 'data')

def get_links_of_quantity_or_section(m_def: str, path: str):
    #resp = requests.get("https://nomad-hzb-se.de/nomad-oasis/gui/artifacts.js")
    #doc = json.loads(resp.content.decode('ascii')[24:-2])
    #res = jmespath.search("[?m_def == '{}']".format(path), doc['metainfo']['packages'])[0]
    #section = jmespath.search("[?name == '{}']".format(name),  res["section_definitions"])[0]
    #print(res)
    m_def = m_def.split("_")
    print(m_def[-1])

get_links_of_quantity_or_section("chemical_energy.CE_NOME_CyclicVoltammetry", "data")
