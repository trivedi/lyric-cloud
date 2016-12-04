#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup


def scrape(url):
    '''
    url -> string
    Must be a Genius URL consisting of song lyrics
    '''
    lines = []
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    lyrics = soup.find('lyrics', class_='lyrics').find('p')
    sections = lyrics.find_all('a')
    for section in sections:
        if '[' not in section.text:
            print section.text
            lines += [section.text]
    return '\n'.join(lines)
