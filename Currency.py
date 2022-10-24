import json
import requests
import Constants as keys

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': keys.API_KEY_COIN,
}

r = requests.get(url, headers=headers)

data = r.json()['data']

bitcoin = r.json()['data'][0]['quote']['USD']['price']
bitcoinPercentChange = r.json()['data'][0]['quote']['USD']['percent_change_24h']
bitcoinResponse = "Current price of Bitcoin is: $" + "{:.2f}".format(bitcoin) + " USD which is " + "{:.2f}".format(bitcoinPercentChange) + "% higher than yesterday"

etherium = r.json()['data'][1]['quote']['USD']['price']
etheriumPercentChange = r.json()['data'][1]['quote']['USD']['percent_change_24h']
etheriumResponse = "Current price of Etherium is: $" + "{:.2f}".format(etherium) + " USD which is " + "{:.2f}".format(etheriumPercentChange) + "% higher than yesterday"


def getCurrency(name):
    result = list(filter(lambda x: x['name'] == name, data))
    try:
        return f"Current price of {result[0]['name']} is: $" + "{:.2f}".format(
            result[0]['quote']['USD']['price']) + " USD which is " + "{:.2f}".format(
            result[0]['quote']['USD']['percent_change_24h']) + "% higher than yesterday"
    except IndexError:
        return f"Cannot find \"{name}\" in the Cryptocurrencies list, be cautious of typos!"


