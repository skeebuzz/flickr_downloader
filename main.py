#!/usr/bin/env python

import urllib.request
import sys
import os
import flickrapi
import xml.etree.ElementTree as ET


api_key = '78fa534193acf30e53d7c9e95dfdc567'
api_secret = '34160d71501154cd'

nArguments = 3
usageString = "usage: python flickr_download.py <user_id> <access_type>"
download_folder = "flickr_downloads"

if len(sys.argv)!= nArguments:
	print(usageString)
	sys.exit()
elif not sys.argv[2] == "private" and not sys.argv[2] == "public":
	print("Error: access_type should be either public or private")
	sys.exit()
else:
	user_id = sys.argv[1]
	access_type = sys.argv[2]
		
flickr = flickrapi.FlickrAPI(api_key, api_secret)
if access_type == "private":
	flickr.authenticate_via_browser(perms='read')	

# getting all the albums of the user
setsXML = flickr.photosets.getList(user_id=user_id)

if setsXML.attrib['stat'] == 'ok':
	sets = setsXML.findall('.//photoset')

	# for each album
	for set in sets:

		title = set.find('title').text
		print("             |")
		print("Downloading \|/ ")
		print(title)
		print("\n")

		# get the title of the album
		album_folder = download_folder + "/" + title
		if os.path.exists(album_folder):
			continue

		print("creating directory for album: {}".format(title))
		os.makedirs(album_folder)

		id = set.attrib['id']

		# store the metadata of the album in a file
		# metadata_file = open(download_folder + "/" + id + "/" + id + '.xml','w')
		# md_str = ET.tostring(set, encoding='utf8', method='xml').decode('utf-8')
		# title_tag = next(set.iter(tag='title'))

		# getting the files in the album
		photosXML = flickr.photosets.getPhotos(photoset_id=id)
		photos = photosXML.findall('.//photo')

		# for each file in the album
		for photo in photos:
			photo_id = photo.attrib['id']
			
			sizesXML = flickr.photos.getSizes(photo_id=photo_id)
			large_size = sizesXML.find('.//size[@label="Large"]')

			photo_url = large_size.attrib['source']

			photo_name = photo_url.split('/')[-1]
			# print("		" + photo_name)
			
			# store the metadata of the file
			# metadata_file = open(download_folder + "/" + id + "/" + photo_name.split('.')[-2] + '.xml','w')
			# metadata_file.write(ET.tostring(photo, encoding='utf8', method='xml').decode('utf-8'))
			# metadata_file.close()

			# downloading the file
			print("downloading {}".format(photo_url))
			urllib.request.urlretrieve(photo_url, album_folder + '/' + photo_name)
else:
	print("Flickr error")
