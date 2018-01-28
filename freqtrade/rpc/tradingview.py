import json, requests

def trend_follower(pair):
    pair = pair.replace('-', "").replace('_', "")
    url = 'https://scanner.tradingview.com/crypto/scan'
    headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    payload = {
        "filter": [
            {
                "left": "Recommend.MA|15",
                "operation": "nempty"
            }, {
                "left": "exchange",
                "operation": "equal",
                "right": "BITTREX"
            }, {
                "left": "name,description",
                "operation": "match",
                "right": f"{pair}"
            }
        ],
        "symbols": {
            "query": {
                "types": []
            }
        },
        "columns": ["name", "Recommend.MA|15", "close|15", "SMA20|15", "SMA50|15", "SMA200|15", "BB.upper|15", "BB.lower|15", "description", "name", "subtype", "SMA20|15", "close|15", "SMA50|15", "SMA200|15", "BB.upper|15", "BB.lower|15"],
        "sort": {
            "sortBy": "Recommend.MA|15",
            "sortOrder": "desc"
        },
        "options": {
            "lang": "en"
        },
        "range": [0, 150]
    }

    r = requests.post(url, json=payload, headers=headers)
    data = r.json()
    return data['data'][0]['d'][1]
