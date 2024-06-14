import json
import jmespath

link_a = "ce_nome_s.CE_NOME_Chronoamperometry"
link_b = "ce_nome_s.CE_NOME_Chronocoulometry"
link_c = "ce_nome_s.CE_NOME_CyclicVoltammetry"

path_to_artifact_file = "/home/a2853/Documents/Projects/nomad/API-PURL/artifacts_ce.json"

with open("artifacts_ce.json") as f:
    data = json.load(f)


def get_ids(base_string):
    base_sec_split = base_string.split("/")
    return int(base_sec_split[2]), int(base_sec_split[4])


def get_section_link_from_section_def(section_def):
    if "links" in section_def:
        return section_def["links"]
    package_id, section_id = get_ids(section_def["base_sections"][0])
    return get_section_link_from_section_def(data["metainfo"]["packages"][package_id]["section_definitions"][section_id])


def get_section_from_mdef(m_def):
    splitted_m_def = m_def.split(".")
    package = jmespath.search("[?name =='{}']".format(".".join(splitted_m_def[:-1])), data["metainfo"]["packages"])[0]
    section_def = jmespath.search("[?name =='{}']".format(splitted_m_def[-1]), package["section_definitions"])[0]
    return section_def


def get_section_link(m_def):
    return get_section_link_from_section_def(get_section_from_mdef(m_def))


def get_quantity_link_from_section_def(section_def, path):
    if "sub_section" in section_def:
        package_id, section_id = get_ids(section_def["sub_section"])
        return get_quantity_link_from_section_def(data["metainfo"]["packages"][package_id]["section_definitions"][section_id], path)

    path_splitted = path.split(".")
    if len(path_splitted) == 1:
        quantities = jmespath.search("[?name =='{}']".format(path_splitted[0]), section_def["quantities"])
        if len(quantities) > 0 and "links" in quantities[0]:
            return quantities[0]["links"]
        else:
            return []
    elif "sub_sections" in section_def:
        subsections = jmespath.search("[?name =='{}']".format(path_splitted[0]), section_def["sub_sections"])
        if len(subsections) > 0:
            return get_quantity_link_from_section_def(subsections[0], ".".join(path_splitted[1:]))
    package_id, section_id = get_ids(section_def["base_sections"][0])
    return get_quantity_link_from_section_def(data["metainfo"]["packages"][package_id]["section_definitions"][section_id], path)


def get_quantity_link(m_def, path):
    section_def = get_section_from_mdef(m_def)
    return get_quantity_link_from_section_def(section_def, path)


link1 = "nomad.datamodel.metainfo.basesections.Measurement"
link2 = "ce_nome_s.CE_NOME_Sample"

# print(t_link_retrieval(link_a))
print(get_section_link(link2))

path = "properties.limit_potential_1"

print(get_quantity_link(link_c, path))
