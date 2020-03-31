import requests
import json



def Get_Site_Information():
    rivernet_api_url = 'https://epiic-fa01-dev.azurewebsites.net/api/sites'
    response = requests.get(rivernet_api_url)
    json_sites = json.loads(response.text)
    return json_sites