import urllib.request

url = "https://www.rfc-editor.org/rfc/rfc739.txt"
saveas = "rfc739.txt"

urllib.request.urlretrieve(url, saveas)
