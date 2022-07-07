import requests

url_main = "https://raw.githubusercontent.com/Paturages/derpament/master/docs/data/{}"
_4dm3_main_file_name = "4dmwc3.json"
_4dm3_round_data = "4dmwc3.{}.json"

def get_main_data():
    return requests.get(url_main.format(_4dm3_main_file_name)).json()

def get_round_data(round_id):
    return requests.get(url_main.format(_4dm3_round_data.format(round_id))).json()
