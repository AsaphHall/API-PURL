import json
import jmespath

link_a = "ce_nome_s.CE_NOME_Chronoamperometry"
link_b = "ce_nome_s.CE_NOME_Chronocoulometry"
link_c = "ce_nome_s.CE_NOME_Chronoamperometry"

def split_m_def(m_def):
        splitted_m_def = m_def.split(".")
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
        path_to_package = jmespath.search("[?name =='{}']".format(splitted_m_def[-2]), data["metainfo"]["packages"])[0]
        path_to_section_defs = jmespath.search("[?name =='{}']".format(splitted_m_def[-1]), path_to_package["section_definitions"])[0]
        base_sec_split =  get_basesection(path_to_section_defs)
        path_2 = base_sec_split[2]
        path_3 = base_sec_split[4]
        path_to_link = jmespath.search("[?m_parent_index==`{}`]".format(path_2), data["metainfo"]["packages"])[0]
        path_to_link_2 = jmespath.search("[?m_parent_index==`{}`]".format(path_3), path_to_link["section_definitions"])[0]

    return path_to_link_2["links"]

print(t_link_retrieval(link_c))