import json
import jmespath
import jsonpath_ng as jp
pfad="data.test.pfad.34.wochenende"
pfad2="nomad.datamodel.metainfo.basesections.Measurement"
#   package name  = nomad.datamodel.metainfo.basesections

with open("test_json.json") as f:
    data_1 = json.load(f)
    path_to_link=""
    path_to_link = jmespath.search("[?name=='{}']".format("B1-2"), data_1["A"])
    path_to_link = jmespath.search("[?name=='{}']".format("B1-2"), data_1["B"])
f.close()

#print(path_to_link)

inp_parameter="name"    
inp_value = "B1-2"
path_to_package = "[?{parameter}=='{{value}}']"
path_to_package = path_to_package.format(parameter = inp_parameter)
path_to_package = path_to_package.format(value = inp_value)
path_to_package = jmespath.search(path_to_package, data_1["B"]["sections"])

#print(path_to_package)


with open("artifacts_ce.json") as d:
    data = json.load(d)
    name_query = jp.parse("metainfo.packages[*].name")
    result = name_query.find(data)
    #print(data["metainfo"]["packages"])
    for i in result:
        print(i.value)
    print(result)
    d.close()

with open("test_json.json") as c:
    data = json.load(c)
    name_query = jp.parse("B.B1.name")
    result = name_query.find(data)
    #print(result)
    c.close()



## Good:

### Makes the query params interchangeable
path_to_package = "[?{parameter}=='{{value}}']"
path_to_package = path_to_package.format(parameter = inp_parameter)
path_to_package = path_to_package.format(value = inp_value)
path_to_package = jmespath.search(path_to_package, pfad)