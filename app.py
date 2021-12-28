import ctypes
import os
#from googlesearch import search
from google_images_download import google_images_download 
import requests
import datetime
from bs4 import BeautifulSoup
import re
from dateutil.parser import parse as dtparse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Acceptance rate
#https://github.com/lixin4ever/Conference-Acceptance-Rate
HEADERS = {
  "User-Agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
  "Accept-Language": "en-US,en;q=0.5",
  }
#HEADERS = {
#  "User-Agent":
#  "Chrome/70.0.3538.102",
#}

CONF_NAMES = [
'NeurIPS',
'ICML',
'ICLR',
'AAAI',
#'ICASSP',
#'Interspeech',
#'CVPR',
#'ECCV',
#'ACL',
#'EMNLP',
]

### Utility functions
def set_wallpaper(image_path):
  SPI_SETDESKWALLPAPER = 20 
  ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)
  
def search_snippet(x, driver):
  ph_search = 'https://www.google.com/search?q={}'
  #ph_search = ph_search + '&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBQgAEIAEOgcIABBHELADOgYIABAWEB5KBAhBGABKBAhGGABQ4gRY3gdg3AloAXACeACAAXCIAcsCkgEDMC4zmAEAoAEByAEKwAEB'
  driver.get(ph_search.format(x))
  try: # Big
    result = driver.find_element_by_css_selector(".Z0LcW").text
    print('Big')
    return result
  except: pass
  try: # Small where bold fonts are used for snippet
    result = driver.find_element_by_css_selector(".hgKElc").text
    print('Small')
    result = result.split('<b>')[1].split('</b>')[0]
    return result
  except: pass
  try: # Table
    result = driver.find_element_by_css_selector(".iKJnec").text
    result = result.split('<b>')[1].split('</b>')[0]
    print('Table')
    return result
  except: pass

    
  '''
  html = requests.get(ph_search.format(x), headers=HEADERS).text
  #html = requests.get(ph_search.format(x)).text
  #soup = BeautifulSoup(html, 'html.parser')
  soup = BeautifulSoup(html, 'lxml')
  #for s in soup.find_all(id="res"):
  #  print(s)
  for s in soup.find_all("div", class_="Z0LcW"): # Big featured snippet
    text = re.sub("[\<].*?[\>]","",s.text)   
    return text
  #for s in soup.find_all("div", class_="d9FyLd"): # Small featured snippet w/ bold important phrase
  for s in soup.find_all("span", class_="hgKElc"): # Small featured snippet w/ bold important phrase
    try:
      text = s.split('<b>')[1].split('</b>')[0]
    except:
      continue
    #re.sub("[\<].*?[\>]","",text)  
    return text
  #soup = BeautifulSoup(html, 'html.parser')
  #for s in soup.find_all("div", class_="IZ6rdc"): # Big & Small featured snippet
    
  #  a = 0
  #  return None
  for s in soup.find_all("div", class_="iKJnec"): # Table
    print(s)
    try:
      text = s.split('<b>')[1].split('</b>')[0]
    except:
      continue
    return text 
  '''
  return None

def normalize_time(x):
  x = x.replace('through','-')
  y = x.split('-')

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
  options = webdriver.ChromeOptions()
  #options.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
  options.add_argument('--lang=en-US')
  #options.add_argument('--lang=en-GB')
  driver = webdriver.Chrome(options=options)
  # Conference wallpaper
  conferences = init_conference_info(CONF_NAMES, driver)
  init_wallpaper_images(conferences)
  #
  driver.close()
  driver.quit()

def init_conference_info(names, driver):
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
  ph_place = '{} place'
  ph_deadline = '{} paper submission deadline'

  for name in names:
    for year in [this_year(), this_year()+1]:
      q_date = ph_date.format(name +" "+ str(year))
      a = search_snippet(q_date, driver)
      print(q_date, a)
      q_place = ph_place.format(name +" "+str(year))
      b = search_snippet(q_place, driver)
      print(q_place, b)
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
