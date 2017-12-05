import urllib2

response = urllib2.urlopen("http://python.org")
html = response.read()

with open("pytong.txt", "w") as f:
    f.write(html)
    f.close()
