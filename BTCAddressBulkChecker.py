from audioop import add
from operator import index
from requests import get
import pandas as pd
import json

data = pd.read_csv('output.csv')


def make_api_url():
    data = pd.read_csv('output.csv')
    Wallet_Address = (data.loc[:, "Address"])
    BASE_URL = "https://blockchain.info/balance"
    for addresses in Wallet_Address:
        addresses = '|'.join(Wallet_Address)

        url = BASE_URL + f"?active={addresses}"  # error
    print(url)
    return url
    

get_balance_url = make_api_url()
response = get(get_balance_url)
try:
    datas = response.json()
    finalbalance = []
    tx = []
    totalreceived = []

    new_dataset = pd.DataFrame.from_dict(datas, orient='index')
    print(new_dataset)
    finalbalance = new_dataset['final_balance'].to_list()
    tx = new_dataset['n_tx'].to_list()
    totalreceived = new_dataset['total_received'].to_list()
    data['Final Balance'] = finalbalance
    data['n_tx'] = tx
    data['Total Received'] = totalreceived
    new_dataset.to_csv('CheckedBTCAddress.csv', index=True, header=True)
except json.JSONDecodeError:
    print('Response could not be serialized')


# https://blockchain.info/balance?active=$address
