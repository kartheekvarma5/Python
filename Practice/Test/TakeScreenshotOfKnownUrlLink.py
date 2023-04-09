import urllib.request
resource = urllib.request.urlopen("https://stackoverflow.com/questions/8286352/how-to-save-an-image-locally-using-python-whose-url-address-i-already-know")
output = open("file01.jpg","wb")
output.write(resource.read())
output.close()
