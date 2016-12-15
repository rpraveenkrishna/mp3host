from bottle import get, post,request, static_file, view, route, run, template
import bottle
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import argparse
import youtube_dl


DEVELOPER_KEY = "{{ DEVELOPER KEY HERE  }}"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()

  videos = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append( (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))

  return videos

@post('/search')
@view('index_template')
def index2():
  name = request.forms.get('search')
  arg_parser = argparse.ArgumentParser()
  arg_parser.add_argument("--q", help="Search term", default=name)
  arg_parser.add_argument("--max-results", help="Max results", default=10)
  args = arg_parser.parse_args()
  videos = youtube_search(args)
  return dict(rows=videos, title='mp3host - search results for - ' + name)




@route('/mp3/<name>/<ids>')
@view('mp3')
def mp3(name, ids):
  url = 'http://youtube.com/' + name
  options = {
    'format': 'bestaudio/best', # choice of quality
    'extractaudio' : True,      # only keep the audio
    'audioformat' : "mp3",      # convert to mp3 
    'outtmpl': '%(title)s.mp3',        # name the file the ID of the video
    'noplaylist' : True,        # only download single song, not playlist
  }
  with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(['http://www.youtube.com/watch?v='+ ids])
  url = '/download/' + name  + '.mp3'
  return dict(mp3=url, name=name)

@route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root='/Users/rpraveenkrishna/Documents/src/python/mp3host', download=filename)



@route('/css/<filename:path>')
def static(filename):
    return static_file(filename, root='/Users/rpraveenkrishna/Documents/src/python/mp3host/views/css', download=filename)


@route('/images/<filename:path>')
def static(filename):
    return static_file(filename, root='/Users/rpraveenkrishna/Documents/src/python/mp3host/views/images', download=filename)


@route('/')
@view('homepage')
def index():
    return dict(title='mp3host')

#bottle.debug(True)
run(reloader=True,host='localhost', port=8005)
