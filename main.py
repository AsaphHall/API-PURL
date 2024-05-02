from api_calls import *
token = ""
entry_id = "2XPJcwSC149dRVj9DdK0nfDopIuW"
token = t_get_token(nomad_se_url,name_t)
if token is None:
    print(token)
data = get_entry_data(entry_id,token,nomad_se_url)
get_sections(data)