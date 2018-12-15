#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import urllib2
import pytube
import os
import multiprocessing
####### User inputs
download_folder='periodfilm5'
playlist_url ='https://www.youtube.com/playlist?list=PLJ5V1Lymzk1SEQ9nPLTqRNcQNGpGBZ0Dt'
###########

if not os.path.exists(download_folder):
    os.mkdir(download_folder)

def extract_links(playlist_url):
    open_link = urllib2.urlopen(playlist_url)
    read_data = open_link.readlines()
    print (len(read_data))
    store_data=[]
    for line in read_data:
        if 'pl-video-title-link' in line:
            #print (line)
            store_data.append(line)
    print len(store_data)

    partial_urls=[]
    for videos in store_data:
        partial_urls.append(videos.split('href="',1)[1].split('" ',1)[0])

    full_urls=[]

    for part_url in partial_urls:
        full_urls.append('http://www.youtube.com'+part_url)
    print len(full_urls)
    return full_urls

download_links=extract_links(playlist_url)

print('We found ---->'+str(len(download_links))+' links in the playlist')
print('Downloding....')

def download_videos(url):
    yt=pytube.YouTube(url)
    video =  yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    try:
        video.download(download_folder)
        print('Donwloaded---'+url+'---:):):)')
    except:
        #print('could not download the file--->'+url)
        pass

#### You can change the number of processes if you want
pool = multiprocessing.Pool(processes=1) 
pool.map(download_videos, download_links)   
