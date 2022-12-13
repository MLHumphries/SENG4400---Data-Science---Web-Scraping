# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:23:00 2022

@author: hummitl
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import re
import urllib.request


#Film ID for various Star Wars films
anh_id = "tt0076759"
esb_id = "tt0080684"
rotj_id = "tt0086190"
rots_id = "tt0121766"
tfa_id = "tt2488496"

#Name ID for various Star Wars actors
hamill_id ="nm0000434"
ford_id = "nm0000148"
fisher_id = "nm0000402"
ridley_id = "nm5397459"
witwer_id = "nm1022429"



def imbdFetchFilm(filmID):
    url = "https://www.imdb.com/title/" + filmID + "/fullcredits"
    
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    time.sleep(1)
    #print(html)
    
    castTable = soup.find_all("table", "cast_list")[0]
    #print(castTable)
    
    tdList = castTable.find_all("td", "primary_photo")
    nameIDs = []
    for td in tdList:
        #print("\n" + str(td) + "\n")
        aTag = td.find_all("a")[0]
        #print(aTag.get('href'))
        href = aTag.get('href')
        nameID = href.strip("/").split("/")[1]
        #print(nameID)
        nameIDs.append(nameID)
    return(nameIDs)


def imbdFetchPerson(nameID):
    url = "https://www.imdb.com/name/nm4004793"
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
    page = urllib.request.urlopen( req )
   
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    filmIds = []
    #for film in filmList:
    for s in soup.find_all("button",id=re.compile("nm-flmg_cred-act.*-tt.*")):
        filmIds.append(s.get('id').split('-')[-1])
    return filmIds
    
################################################
#Film ID for various Star Wars films
anh_id = "tt0076759"
esb_id = "tt0080684"
rotj_id = "tt0086190"
rots_id = "tt0121766"
tfa_id = "tt2488496"

#Name ID for various Star Wars actors
hamill_id ="nm0000434"
ford_id = "nm0000148"
fisher_id = "nm0000402"
ridley_id = "nm5397459"
witwer_id = "nm1022429"


#Star Wars: A New Hope
aNewHopeList = imbdFetchFilm(anh_id)
print(aNewHopeList)

#Star Wars: The Empire Strikes Back
esbList = imbdFetchFilm(esb_id)
print(esbList)

#Star Wars: Return of the Jedi
rotjList = imbdFetchFilm(rotj_id)
print(rotjList)

#Star Wars: Revenge of the Sith
rotsList = imbdFetchFilm(rots_id)
print(rotsList)

#Star Wars: The Force Awakens
tfaList = imbdFetchFilm(tfa_id)
print(tfaList)

#Mark Hamill
markHamill = imbdFetchPerson(hamill_id)
print(markHamill)

#Harrison Ford
harrisonFord = imbdFetchPerson(ford_id)
print(harrisonFord)

#Carrie Fisher
carrieFisher = imbdFetchPerson(fisher_id)
print(carrieFisher)

#Daisy Ridley
daisyRidley = imbdFetchPerson(ridley_id)
print(daisyRidley)

#Sam Witwer
samWitwer = imbdFetchPerson(witwer_id)
print(samWitwer)