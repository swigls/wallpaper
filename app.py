import ctypes
import os
#from googlesearch import search
from google_images_download import google_images_download 
import requests
import datetime
from bs4 import BeautifulSoup

# Acceptance rate
#https://github.com/lixin4ever/Conference-Acceptance-Rate
headers = {
  "User-Agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}


### Utility functions
def set_wallpaper(image_path):
  SPI_SETDESKWALLPAPER = 20 
  ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)
  
def search_snippet(x):
  ph_search = 'https://www.google.com/search?q={}'
  ph_search = ph_search + '&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBQgAEIAEOgcIABBHELADOgYIABAWEB5KBAhBGABKBAhGGABQ4gRY3gdg3AloAXACeACAAXCIAcsCkgEDMC4zmAEAoAEByAEKwAEB'
  html = requests.get(ph_search.format(x), headers=headers).text
  soup = BeautifulSoup(html, 'html.parser')
  for s in soup.find_all(id="res"):
    print(s.text)
  #summary = soup.select_one('.Uo8X3b+ span').text

def this_year():
  today = datetime.date.today()
  year = int(today.strftime("%Y"))
  return year


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
  
def init_conference_info(names):
  '''
  # Initial crawling w/ ai-deadlines
  info_hub_url = 'http://aideadlin.es/?sub=ML,CV,NLP,SP'
  src = requests.get(info_hub_url)
  print(src.content)
  for name in names:
    print(name)
  # Secondary crawling w/ Google search
  pass
  '''
  ph_date = '{} date'
  ph_place = 'where is {}'
  ph_deadline = '{} paper submission deadline'
  q_date = ph_date.format(names[0] +" "+ str(this_year()))
  print(q_date)
  a = search_snippet(q_date)
   
  return []

def init_wallpaper_images(conferences):
  if not os.path.exists('data'):
    os.system('mkdir data')
  # Download wallpaper images from Google
  response = google_images_download.googleimagesdownload()
  for c in conferences:
    arguments = {'keywords':'4k wallpaper {}'.format(c)}


### Periodic functions
def draw():
  set_wallpaper(os.path.abspath('./sample.png'))
  pass


#########################################################
### Main functions
def main():
  setup()
  draw()

if __name__ == "__main__":
  main()
