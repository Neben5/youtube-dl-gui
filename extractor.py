from __future__ import unicode_literals
import youtube_dl

status = ''
def downloader(destination, link):
    opts = {'outtmpl': destination.get(), 'progress_hooks': [my_hook], 'logger': MyLogger()}
    with youtube_dl.YoutubeDL(opts) as ydl:
        ydl.download([link.get()])


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        pass

#make it such that the status can be displayed in gui
def my_hook(d):
    status = d['status']


'''https://soundcloud.com/elysianrecords/believer'''
