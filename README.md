# flickr Downloader for albums and tags
## Why the Fork
Flickr is going to start charging for storage in 2019, so I wanted to download all my shit so I can upload it all to one of my cloud drives. This script preserves albums and stores everything from albums in subdirectories so it was exactly what I was looking for.
</br>
Updates to the fork:</br>
- updated to work with python 3 (i'm using 3.7)
- changed the album directory names to use the album title instead of the id
- download a large version of the photo instead of the original size (i'd rather save space and my photos aren't with a crazy camera, but if you want to download the original change the "@label="Large" back to "@label="Original"
- don't bother saving the metadata files

## Why:
well, I was looking for a nice wallpapers and found these amazing photos by Masashi Wakui on flickr. </br>
tried downloading, but apparently flickr was not allowing any downloads.</br>
If I was to do it manually, then I would have to open each one of the pictures, click to download, </br>
then click to choose the size, open inspect elements, find the link to the image, </br>
copy, paste it to download. Annoying, isnt't it?</br>
</br>
So I wrote a code to do that. </br>
In order to use this you will need an API key and secret Key for Flickr, </br>
However I have left my API keys in there for everyone to use </br>
You will be asked to enter wether you want to search by the 'tag' or by the 'album'</br>
The quality is set to download the highest all the time. </br>
All the pictures will be saved into a folder called 'images/tag or albumID'; </br>
If folders do not exist, they will be automatically generated </br>
![alt tag](https://raw.githubusercontent.com/Denisolt/flickr_album_downloader/master/process.gif)</br>


## Dependencies:
- beautifulsoup4==4.6.0
- bs4==0.0.1
- certifi==2017.4.17
- chardet==3.0.3
- flickrapi==2.3
- idna==2.5
- oauthlib==2.0.2
- requests==2.17.3
- requests-oauthlib==0.8.0
- requests-toolbelt==0.8.0
- six==1.10.0
- urllib3==1.21.1

## Execution:
Download the project: </br>
```bash
git clone https://github.com/Denisolt/flickr_album_downloader.git
cd flickr_album_downloader
```
Activate virtual environment: </br>
```bash
source local/bin/activate
pip install -r requirements.txt
```
Run: </br>
```bash
python main.py
```
The output should be like this: </br>
![alt tag](https://raw.githubusercontent.com/Denisolt/flickr_album_downloader/master/img.png)</br>
