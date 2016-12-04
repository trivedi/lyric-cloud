#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup


def get_lyrics(url):
    '''
    url -> string
    Must be a Genius URL consisting of song lyrics
    Returns string of song lyrics
    '''
    lines = []
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    lyrics = soup.find('lyrics', class_='lyrics').find('p')
    sections = lyrics.find_all('a')
    print 'Getting lyrics!'
    print
    for section in sections:
        if '[' not in section.text:
            print section.text
            lines += [section.text]
    return '\n'.join(lines)


def get_tracks(url):
    '''
    url -> string
    Must be a Genius URL for an album
    Return dictionary of track name - URL key-value pairs
    '''
    tracks = {}  # song title : url
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    print 'Getting tracks!'
    print
    for track in soup.find('ul', class_='song_list').find_all('li'):
        t = track.find('a')
        print 'Got url for', t.text.strip()
        tracks[t.text] = t['href']
    return tracks




