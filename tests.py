import unittest
from unittest import TestCase, mock

import settings
from utils import (get_random_word, get_word_content, get_joke, get_words_stats)


class MockResponse:
    def __init__(self, status_code, data):
        self.data = data
        self.status_code = status_code

    def json(self):
        return self.data


def mocked_requests_get(*args, **kwargs):
    if args[0].startswith(settings.GET_RANDOM_WORD_URL):
        return MockResponse(200, ["test"])

    elif args[0].startswith(settings.WIKIPEDIA_API):
        return MockResponse(200, {'parse': {'text': {'*': 'word text'}}})

    elif args[0].startswith(settings.JOKES_API):
        return MockResponse(200, {'value': {'joke': 'Alex Golt is a funny'}})

    return MockResponse(404, None)


class RandomWordTestCase(TestCase):
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_random_word(self, mock_get):
        error, word = get_random_word()
        self.assertEqual(error, None)
        self.assertEqual(word, 'test')

    def test_stats(self):
        error, stats = get_words_stats(1)
        self.assertEqual(error, None)
        self.assertEqual(stats, {})


class JokeTestCase(TestCase):
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_joke_content(self, mock_get):
        error, word = get_joke('Alex', 'Golt')
        self.assertEqual(error, None)
        self.assertEqual(word, 'Alex Golt is a funny')


class WikipediaWordTestCase(TestCase):
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_word_content(self, mock_get):
        error, word = get_word_content('word')
        self.assertEqual(error, None)
        self.assertEqual(word, 'word text')


if __name__ == '__main__':
    unittest.main()
