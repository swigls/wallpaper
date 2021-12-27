import ctypes
import os
from googlesearch import search
from google_images_download import google_images_download 
import requests

# Acceptance rate
#https://github.com/lixin4ever/Conference-Acceptance-Rate

### Utility functions
def set_wallpaper(image_path):
  SPI_SETDESKWALLPAPER = 20 
  ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 0)
  
def parse_aideadline(conference):
  

### Setup functions
class Conference():
  def __init__(self, name, place, date, deadline):
    self.name = name
	self.place = place
	self.date = date
	self.deadline = deadline
	
def setup():
  # Conference wallpaper
  conferences = init_conference_info(["NeurIPS","ICML","ICLR","AAAI","ICASSP","InterSpeech","CVPR","ECCV","ACL","EMNLP"])
  init_wallpaper_images(conferences)
  
def init_conference_info():
  # Initial crawling w/ ai-deadlines
  info_hub_url = 'http://aideadlin.es/?sub=ML,CV,NLP,SP'
  requests.get(info_hub_url)
  # Secondary crawling w/ Google search

def init_wallpaper_images(conferences):
  # Download wallpaper images from Google
  response = google_images_download.googleimagesdownload()
  for c in conferences:
  arguments = {'keywords':'4k wallpaper {}'.format(c)}

### Periodic functions
def draw():
  pass

#########################################################
### Main functions
def main():
  setup()
  draw()

if __name__ == "__main__":
  main()