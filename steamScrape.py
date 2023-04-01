from bs4 import BeautifulSoup
import requests

search = ""

def itemSearch(item):
    steamMarketURL = itemURL(item)

    request = requests.get(steamMarketURL)
    soup = BeautifulSoup(request.content, 'html.parser')

    query_results = soup.find(id='searchResultsRows')
    item_name = query_results.find_all('span', class_="market_listing_item_name")
    item_price_query = query_results.find_all('span', class_="normal_price")

    results = {}

    item_price_result = []
    for x in range(len(item_price_query)):
        if x%2 != 0:
            item_price_result.append(item_price_query[x].get_text())

    for (listing, price) in zip(item_name, item_price_result):
        results[listing.get_text()] = price

    return results

def itemURL(item):
    steamMarketURL = f'https://steamcommunity.com/market/search?appid=730&q={item}'

    return steamMarketURL

def createMsg(query):
    msg_output = "```"
    for key, value in query.items():
        msg_output += f'{key}        current price: {value}\n'
    msg_output += "```"

    return msg_output