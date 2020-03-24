import requests










def Get_Site_Information():
    rivernet_api_url = 'https://epiic-fa01-dev.azurewebsites.net/api/sites'

    response = requests.get(rivernet_api_url)
    print(response.text)