import requests
import json
import getpass

nomad_se_url = "https://nomad-hzb-se.de/nomad-oasis/api/v1"
nomad_ce_url = "https://nomad-hzb-ce.de/nomad-oasis/api/v1"
token = ""
name = ""
name_t = "tobias.roeschmann@helmholtz-berlin.de"


##################################################################################################################
# Eine Kopie meiner Funktion zur Extraktion von 
# 
##################################################################################################################

def get_entry_data(id,token,url):
    data = requests.get(f'{url}/entries/{id}', headers={'Authorization': f'Bearer {token}'})
    data = data.json()
    return data

##################################################################################################################
# Eine Funktion zur Extraktion der Sektions aus dem get_entry_data-File
# 
##################################################################################################################
def get_sections(data):
    sections = []
    for path in data['data'][0]['entry_metadata']['section_defs']['definition_qualified_name']:
        sections.append(path)
    print(sections)





##################################################################################################################
# Eine Kopie von Michas Funktion zur Erstellung eines Token
# 
##################################################################################################################

def t_get_token(url, name=None):
    user = name if name is not None else input("Username")
    print("Passwort: \n")
    password = getpass.getpass()
    
    # Get a token from the api, login
    response = requests.get(
        f'{url}/auth/token', params=dict(username=user, password=password))    
    return response.json()['access_token']

##################################################################################################################
# Eine Kopie von Michas Funktion
# Die Funktion extrahiert den Link zur Klasse Cyclic Voltammetry
##################################################################################################################
def michas_link_retrieval():
    resp = requests.get("https://nomad-hzb-ce.de/nomad-oasis/gui/artifacts.js")
    doc = json.loads(resp.content.decode('ascii')[24:-2])

    import jmespath
    # 'name': 'baseclasses.chemical_energy.cyclicvoltammetry',
    res = jmespath.search("[?name == 'baseclasses.chemical_energy.cyclicvoltammetry']", doc['metainfo']['packages'])[0]
    section = jmespath.search("[?name == 'CyclicVoltammetry']",  res["section_definitions"])[0]

    print(section["links"])

##################################################################################################################
# Diese Funktion soll Links die Section IDs/Pfade heraussuchen
#
##################################################################################################################
def t_link_retrieval():
    subsections = []
    data = get_entry_data(id,token)
    resp = requests.get("https://nomad-hzb-ce.de/nomad-oasis/gui/artifacts.js")
    doc = json.loads(resp.content.decode('ascii')[24:-2])

    import jmespath
    # 'name': 'baseclasses.chemical_energy.cyclicvoltammetry',
    res = jmespath.search("[?name == 'baseclasses.chemical_energy.cyclicvoltammetry']", doc['metainfo']['packages'])[0]
    section = jmespath.search("[?name == 'CyclicVoltammetry']",  res["section_definitions"])[0]

    print(section["links"])