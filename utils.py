from collections import Counter

import requests
from requests.exceptions import RequestException

import settings


counter = Counter()


def get_random_word():
    try:
        resp = requests.get(settings.GET_RANDOM_WORD_URL, timeout=settings.HTTP_TIMEOUT)
    except RequestException as exc:
        return 'Error to get random word', None

    if resp and resp.status_code == requests.codes.ok:
        if 'wrong' in resp.text:
            return 'Wrong API key', None

        data = resp.json()
        try:
            word = data[0]
        except Exception as exc:
            return 'Error parsing respnonse', None
        else:
            return None, word


def get_word_content(word, format="json"):
    """Returns an article content of provided word from Wikipedia."""

    params = {
        "action": "parse",
        "section": 0,
        "prop": "text",
        "page": word,
        "format": format
    }
    try:
        resp = requests.get(settings.WIKIPEDIA_API, params=params)
    except RequestException as exc:
        return 'Error to get response from Wikipedia', None

    if resp.status_code == requests.codes.ok:
        counter[word] += 1
        try:
            data = resp.json()
            text = data['parse']['text']['*']

        except Exception as exc:
            return 'Error to parse Wikipedia response', None

        else:
            return None, text


def get_joke(fname, lname):
    params = {'firstName': fname, 'lastName': lname}
    try:
        resp = requests.get(settings.JOKES_API, params=params)
    except RequestException as exc:
        return 'Error to get response from Joke', None

    if resp.status_code == requests.codes.ok:
        try:
            data = resp.json()
            text = data['value']['joke']

        except Exception as exc:
            return 'Error to parse Joke response', None

        else:
            return None, text


def get_words_stats(limit=1):
    """Get statistics of most commond words"""
    return None, dict(counter.most_common(limit))
    
