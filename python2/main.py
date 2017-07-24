#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#	Programmer: Luis Navarro
#

# Librery 
import feedparser
from bs4 import BeautifulSoup as BS
import unicodedata

# version python 2
# Funciones Definidas
def elimina_tildes(cadena):
	s = ''.join((c for c in unicodedata.normalize('NFD',unicode(cadena)) if unicodedata.category(c) != 'Mn'))
	return s.decode()

# Data url
url = 'http://one--anime.blogspot.com/rss.xml'

# Instance URL
data = feedparser.parse(url)

# Count entries
totalEntries = len(data.entries)

print '##########################################################'
print 'Nombre del Blog:\t\t\t' + data.feed.title
print 'Url del Blog:\t\t\t' + data.feed.link
print 'Descripcion del Blog:\t\t' + data.feed.description
print '##########################################################'


# Datos a capturar
#
# title Post: 		data.entries[0].title
# Link  Post: 		data.entries[0].link
# Date  Post: 		data.entries[0].published
# Description Post: data.entries[0].summary_detail.value

# Iterate each post
for post in data.entries:

	# Array Empty
	info = []
	imagenes = []

	# Data for process
	html = post.summary_detail.value
	soup = BS(html, 'lxml')

	print 'Titulo del Post: ' + post.title
	print 'Fecha de Publicacion: ' + post.published

	for t in soup.find_all('div'):
		info.append(t)

	# Amount of array
	#print len(info)
	# Cantidad de span
	#print len(info)

	busqueda = ''

	if len(info) > 0:
		
		if len(info[0].text) == 0:

			if len(info[2]) == 0:
				# pass
				busqueda =  info[1].text 


		# Find all the images of Post
		for img in soup.find_all('img'):
			imagenes.append(img['src']) 

		else:
			busqueda =  info[0].text 


	# Convert unicode to string
	#conversion = busqueda.encode('ascii', 'ignore').decode('utf-8')
	# Data convert 
	#parrafo = conversion.capitalize()

	#if ''

	# Synopsis
	# Data where word begins
	positionSipnosis = busqueda.find('Datos')
	print busqueda[:positionSipnosis]

	# Title
	positionTitleEnd = busqueda.find('Tipo:')
	print busqueda[(positionSipnosis+5):positionTitleEnd]

	# Type
	positionTypeEnd = busqueda.find('Temporadas');
	print busqueda[positionTitleEnd:positionTypeEnd]

	# Season
	positionSeasonEnd = busqueda.find('Episodios:')
	print busqueda[positionTypeEnd:positionSeasonEnd]

	# Episodes
	positionEpisodesEnd = busqueda.find('neros:');
	print busqueda[positionSeasonEnd:(positionEpisodesEnd-2)]

	# Genders
	positionGendersEnd = busqueda.find('Calidad:')
	print busqueda[(positionEpisodesEnd-2):positionGendersEnd]

	# # Quality
	# positionQualityEnd = busqueda.find('Fuente:')
	# print busqueda[positionGendersEnd:positionQualityEnd]

	# # Source	
	# positionSourceEnd = busqueda.find('Peso:')
	# print busqueda[positionGendersEnd:positionSourceEnd]

	# # Weight
	# positionWeightEnd = busqueda.find('Subs:')
	# print busqueda[positionQualityEnd:positionWeightEnd]


	print imagenes

	print '\n\n'
