import requests
from bs4 import BeautifulSoup
from unicodedata import normalize
import youtube_dl
import argparse


def normalize_special_char(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


def sed(text):

    url = 'https://www.youtube.com'

    r = requests.get(url + '/results', params={'search_query': text})
    soup = BeautifulSoup(r.content, 'html.parser')
    for tag in soup.find_all('a', {'rel': 'spf-prefetch'}):
        title, video_url = tag.text, url + tag['href']
        if 'googleads' not in video_url:
            return normalize_special_char(title), video_url


def download(title, video_url):
    ydl_opts = {
        'outtmpl': '{}.%(ext)s'.format(title),
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    return ydl_opts["outtmpl"]


parser = argparse.ArgumentParser()
parser.add_argument('dl',
                    help='Enter song name to download', type=str, nargs='+')
args = parser.parse_args()
text = ' '.join(args.dl)
tittle, video_link = sed(text)
download(tittle, video_link)
