import urllib2
from xml.dom import minidom

def zapisDoPliku(url):
    with open("band.xml", 'w') as sitefile:
        sitefile.write(urllib2.urlopen(url).read())

zapisDoPliku('https://www.metal-archives.com/bands/Manowar/83')
xmldoc = minidom.parse('band.xml')
name = xmldoc.getElementsByTagName('name')
year = xmldoc.getElementsByTagName('formed')
genre = xmldoc.getElementsByTagName('genre')
location = xmldoc.getElementsByTagName('location')

print "name: " + name.childNodes[0].nodeValue
print "year: " + year.childNodes[0].nodeValue
print "genre: " + genre.childNodes[0].nodeValue
print "location: " + location.childNodes[0].nodeValue
