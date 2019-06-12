import csv
import requests
import json
from helpers import okta_url, api_key

reader = csv.DictReader(open("import_csv_template.csv", 'r'))
dict_list = []
for line in reader:
    dict_list.append(line)

for user_list in dict_list:
    dup_list = dict(user_list)
    print(dup_list.get("password"))

    url = "{0}/api/v1/users".format(okta_url)

    password = {"password": user_list.get("password")}
    dup_list.pop("password", None)

    querystring = {"activate": "true"}
    payload = json.dumps({"profile": dup_list, "credentials": password})

    headers = {
        'accept': "application/json",
        'content-type': "application/json",
        'authorization': "SSWS {0}".format(api_key),
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)