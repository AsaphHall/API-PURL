# Letzter Stand:
#   .split() durch .rsplit() ersetzt um nur nach dem letzten Punkt zu teilen und basesections zu erreichen
#

import json
import jmespath

link_a="ce_nome_s.CE_NOME_Chronoamperometry"
link_b="ce_nome_s.CE_NOME_Chronocoulometry"
link_c="ce_nome_s.CE_NOME_Chronoamperometry"
link_d="nomad.datamodel.metainfo.basesections.Measurement"
link_e="baseclasses.material_processes_misc.annealing"

def split_m_def(m_def):
        splitted_m_def = m_def.rsplit(".",1)
        return splitted_m_def


def get_basesection(path_to_section):
    base_sec = path_to_section['base_sections'][0]
    base_sec_split = base_sec.split("/")
    path_2 = base_sec_split[2]
    path_3 = base_sec_split[4]
    return base_sec_split
    
def t_link_retrieval(m_def):
    splitted_m_def = split_m_def(m_def)
    with open("artifacts_ce.json") as f:
        data = json.load(f)
        print(splitted_m_def)
        path_to_package = jmespath.search("[?name =='{}']".format(splitted_m_def[-2]), data["metainfo"]["packages"])[0]
        print("Path to package: ")
        print(path_to_package)
        path_to_section_defs = jmespath.search("[?name =='{}']".format(splitted_m_def[-1]), path_to_package["section_definitions"])[0]
        base_sec_split =  get_basesection(path_to_section_defs)
        parent_index_1 = base_sec_split[2]
        parent_index_2 = base_sec_split[4]
        #Wie Quantities? resistance = ["metainfo"]["packages"][]
        path_to_link = jmespath.search("[?m_parent_index==`{}`]".format(parent_index_1), data["metainfo"]["packages"])[0]
        path_to_link_2 = jmespath.search("[?m_parent_index==`{}`]".format(parent_index_2), path_to_link["section_definitions"])[0]

    return path_to_link_2["links"]

def t_quantity_link_retrieval(m_def):
    splitted_m_def = split_m_def(m_def)
    with open("artifacts_ce.json") as f:
        data = json.load(f)
        print(splitted_m_def)
        path_to_package = jmespath.search("[?name =='{}']".format(splitted_m_def[-2]), data["metainfo"]["packages"])[0]
        print("Path to package: ")
        print(path_to_package)
        path_to_section_defs = jmespath.search("[?name =='{}']".format(splitted_m_def[-1]), path_to_package["section_definitions"]["quantities"])[0]
        base_sec_split =  get_basesection(path_to_section_defs)
        parent_index_1 = base_sec_split[2]
        parent_index_2 = base_sec_split[4]
        #Wie Quantities? resistance = ["metainfo"]["packages"][]
        path_to_link = jmespath.search("[?m_parent_index==`{}`]".format(parent_index_1), data["metainfo"]["packages"])[0]
        path_to_link_2 = jmespath.search("[?m_parent_index==`{}`]".format(parent_index_2), path_to_link["section_definitions"])[0]

    return path_to_link_2["links"]

print(t_quantity_link_retrieval(link_d))

################
# Ende der Funktionen
####################



































print(t_link_retrieval(link_e))


with open("artifacts_ce.json") as f:
        data = json.load(f)
def get_pfad(pfad, m_def, data):
    pfad = 'data["metainfo"]["packages"][0]'
    path_to_package = jmespath.search("[?name =='{}']".format(m_def[-2]), pfad)
    pfad = path_to_package
    if(1==1):
        print(pfad)
    else:
         get_pfad(pfad, m_def, data)

#get_pfad('data["metainfo"]["packages"]',split_m_def(link_a),data)




######
# Pfade von durch Rekursion am Beispiel von cyclicvoltammetry
#######
#
#suche name -> adaptiere pfad -> suche 
#