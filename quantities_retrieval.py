import json
import jmespath

link_a = "ce_nome_s.CE_NOME_Chronoamperometry"
link_b = "ce_nome_s.CE_NOME_Chronocoulometry"
link_c = "ce_nome_s.CE_NOME_Chronoamperometry"
link_e="baseclasses.material_processes_misc.annealing"
subsection = "layer"
path_to_quantity ="/packages/46/section_definitions/0"
path_cv="data.name#ce_nome_s.CE_NOME_CyclicVoltammetry"

def split_m_def(m_def):
        splitted_m_def = m_def.split(".")
        return splitted_m_def


def get_basesection(path_to_section):
    base_sec = path_to_section['base_sections'][0]
    base_sec_split = base_sec.split("/")
    path_2 = base_sec_split[2]
    path_3 = base_sec_split[4]
    return base_sec_split
    
def t_link_retrieval(name):
    path_to_package = ""
    with open("test_quantities3.txt","w") as c:
        with open("artifacts_ce.json") as f:
            data = json.load(f)
            for a,package in enumerate(data["metainfo"]["packages"]):
                for b,section_defintion in enumerate(data["metainfo"]["packages"][a]["section_definitions"]):
                    quantity_data = jmespath.search("[?name =='{}']".format(name), data["metainfo"]["packages"][a]["section_definitions"][b])
                    print(quantity_data)
                    try:
                        for c, quantities in enumerate(data["metainfo"]["packages"][a]["section_definitions"][b]["quantities"]):
                            quantity_data = jmespath.search("[?name =='{}']".format(name), data["metainfo"]["packages"][a]["section_definitions"][b]["quantities"])
                            #print(data["metainfo"]["packages"][a]["section_definitions"][b]["quantities"][c]["name"])
                            if len(quantity_data) == 0:
                                pass
                            else:   
                                print(quantity_data)
                                print("\n")
                            #return quantity_data["links"]
                    except KeyError:
                         pass
                    try:
                        for c, sub_section in enumerate(data["metainfo"]["packages"][a]["section_definitions"][b]["sub_section"]):
                            #print(data["metainfo"]["packages"][a]["section_definitions"][b]["sub_section"][c]["name"])
                            subsection_data = jmespath.search("[?name =='{}']".format(name), data["metainfo"]["packages"][a]["section_definitions"][b]["sub_section"])
                            if len(subsection_data) == 0:
                                pass
                            else:
                                print(subsection_data)
                                print("\n")
                        return subsection_data["links"]
                    except KeyError:
                         pass
        return "Na immerhin kein Fehler"
                    
                         
                        


print(t_link_retrieval("LayerProperties"))