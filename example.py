#!/usr/bin/env python
"""
Minimal Example
===============
Generating a square wordcloud from a URL
"""
from PIL import Image
from os import path
from wordcloud import WordCloud, ImageColorGenerator
from requests import get
from StringIO import StringIO
import matplotlib.pyplot as plt
from numpy import array
from lyriccloud import scrape

url = 'http://genius.com/albums/Modest-mouse/Good-news-for-people-who-love-bad-news'

cover_url, tracks = scrape.get_tracks(url)
lyrics = ''
for track, url in tracks.items():
    print 'Getting lyrics for', track.strip()
    lyrics += scrape.get_lyrics(url)

img_content = get(cover_url).content
album_colors = alice_coloring = array(Image.open(StringIO(img_content)))

# create coloring based on album cover art
wordcloud_colors = ImageColorGenerator(album_colors)

# Generate a word cloud image
wordcloud = WordCloud(color_func=wordcloud_colors).generate(lyrics)

plt.imshow(wordcloud)

plt.axis("off")
plt.figure()
plt.show()

'''
# The pil way (if you don't have matplotlib)
image = wordcloud.to_image()
print image
image.show()
'''
