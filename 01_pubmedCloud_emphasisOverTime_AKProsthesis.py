#-*- coding:utf-8 -*-

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# 
# Copyright 2019 Ellankavi Ramasamy

from Bio import Entrez, Medline
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import searchQuery



if __name__ == '__main__':
  # Edit these details
  ncbiId = 'user@email.com'
  yearBegin = 1941
  yearEnd   = 2020  
  maxWords  = 100
  searchMode = 'both' # other modes: single, decade
  prefix = 'query_'
  # End edit
  
  # Note the space between the final triple quotes and the previous word is essential!
  # queryBase1 = """(((((((transfemoral) OR above-knee) 
  #                   AND prosthesis ) 
  #                     NOT osseointegrated* ) 
  #                     NOT implantation ) 
  #                     NOT bone-anchored)) """
  
  queryBase1 = """ ( (transfemoral prosthesis OR above-knee prosthesis) AND (amputee OR amputation) ) NOT
                     (osseointegrated OR bone-anchored) """

  if searchMode == 'single':    
    queryBase2 = 'AND (\"%d\"[Date - Publication] : \"%d\"[Date - Publication])'%(yearBegin,yearEnd)    
    query = queryBase1+queryBase2
    imgFile = "%sALL_%d_%d.png"%(prefix,yearBegin,yearEnd)
    
    titleText = searchQuery.search(ncbiId,query)
    if not titleText == ' ?':
      print 'Querying database for %d-%d\n'%(yearBegin,yearEnd)
      searchQuery.queryPubmed(query,maxWords,imgFile,ncbiId)

  elif searchMode == 'decade':
    nrQueries = (yearEnd+1-yearBegin)/10
    for ii in range(nrQueries):
      yrBegin = yearBegin+ii*10
      yrEnd   = yearBegin+(ii+1)*10-1
      imgFile = "%s%d_%d.png"%(prefix,yrBegin,yrEnd)
      
      queryBase2 = 'AND (\"%d\"[Date - Publication] : \"%d\"[Date - Publication])'%(yrBegin,yrEnd)    
      query = queryBase1+queryBase2
      
      titleText = searchQuery.search(ncbiId,query)      
      if not titleText == ' ?':
        print 'Querying database for %d-%d\n'%(yrBegin,yrEnd)
        searchQuery.queryPubmed(query,maxWords,imgFile,ncbiId)

  else:
    # perform both single and decade search queries
    # 1. Single
    queryBase2 = 'AND (\"%d\"[Date - Publication] : \"%d\"[Date - Publication])'%(yearBegin,yearEnd)    
    query = queryBase1+queryBase2
    imgFile = "%sALL_%d_%d.png"%(prefix,yearBegin,yearEnd)
    
    titleText = searchQuery.search(ncbiId,query)
    if not titleText == ' ?':
      print 'Querying database for %d-%d\n'%(yearBegin,yearEnd)
      searchQuery.queryPubmed(query,maxWords,imgFile,ncbiId)

    # 2. decade 
    nrQueries = (yearEnd+1-yearBegin)/10
    for ii in range(nrQueries):
      yrBegin = yearBegin+ii*10
      yrEnd   = yearBegin+(ii+1)*10-1
      imgFile = "%s%d_%d.png"%(prefix,yrBegin,yrEnd)
      queryBase2 = 'AND (\"%d\"[Date - Publication] : \"%d\"[Date - Publication])'%(yrBegin,yrEnd)    
      query = queryBase1+queryBase2
      
      titleText = searchQuery.search(ncbiId,query)
      if not titleText == ' ?':
        print 'Querying database for %d-%d\n'%(yrBegin,yrEnd)
        searchQuery.queryPubmed(query,maxWords,imgFile,ncbiId)