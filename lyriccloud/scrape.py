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
    print 'Getting lyrics from', url, '\n'
    for section in sections:
        if '[' not in section.text:
            lines += [section.text]
    return '\n'.join(lines)


def get_tracks(url):
    '''
    url -> string
    Must be a Genius URL for an album
    Return cover art URL and dictionary of track name - URL key-value pairs
    '''
    tracks = {}  # song title : url
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    cover_src = soup.find('img', class_='cover_art')['src']
    print 'Getting album cover\n', cover_src, '\nGetting album tracks!\n'
    for track in soup.find('ul', class_='song_list').find_all('li'):
        t = track.find('a')
        print 'Got url for', t.text.strip().encode('utf-8')
        tracks[t.text] = t['href'].encode('utf-8')
    return (cover_src, tracks)

