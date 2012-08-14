#!/usr/bin/python
from urlparse import parse_qs
from struct import pack
import time

# getting GET parameters from URL string
params = parse_qs(os.environ['QUERY_STRING'])
seekat = params['position']
videofile = params['file']

# setting right HTTP headers

# disabling cache
current_time = time.gmtime(time.time())
current_time = time.strftime('%a, %d %m %Y %H:%M:%S GMT', current_time)

print("Expires: Mon, 26 Jul 1997 05:00:00 GMT")
print("Last-Modified: %s" % current_time) 
print("Cache-Control: no-store, no-cache, must-revalidate")
print("Cache-Control: post-check=0, pre-check=0", false)
print("Pragma: no-cache")

# printing type and length of content
print('Content-Type: video/x-flv')
print('Content-Length: %i' % os.path.getsize(videofile))

# starting magic
if seekat:
	print('FLV')
	print(pack('b', 1))
	print(pack('b', 1))
	print(pack('L', 9))
	print(pack('L', 9))
fh = open(videofile, 'rb')
fh.seek(seekat)
chunk = 16384 # slice chunk size
bites = fh.read(chunk)
while bites:
	print(bites)
	bites = fh.read(chunk)
fh.close()