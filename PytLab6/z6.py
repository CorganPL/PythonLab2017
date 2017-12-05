import urllib2
from xml.dom import minidom

response = urllib2.urlopen("https://www.metal-archives.com/bands/Helloween/159")
html = response.read()
doc = minidom.parseString(html)

print html
