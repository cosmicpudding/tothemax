from astropy.io import ascii
import base64
import sys

####################################################

# User input
bgcolor = '#000000'

# Get name of user file and number of images
try: 
	urlfile = sys.argv[1]
	imgnum = int(sys.argv[2])

	# Truncate to avoid server limit
	if imgnum > 75:
		print 'You are likely to have trouble with URL length... truncating to 75!'
		imgnum = 75

except:
	print 'No input specified... using defaults'
	urlfile = 'apodurl.txt'
	imgnum = 5	

####################################################

# Example for a subset of latest N apod images
d = ascii.read(urlfile)

# Check if the number of images is greater than the list provided
if imgnum > len(d):
	print 'You do not have as many images as you think you have... truncating to %s!' % len(d)
	imgnum = len(d)
subset = d[-imgnum:]

# Convert each URL to a string, and join the list
s = [str(x[0]) for x in subset]
s2 = '","'.join(s)

####################################################

# example
jstr = '{"background":"%s","images":["%s"]}' % (bgcolor,s2)
url = 'http://koalastothemax.com/?'+base64.b64encode(jstr)
print '\nURL for custom images:\n'
print url
print

# Check URL length
if len(url) > 8000:
	print 'Warning! Your URL is likely to fail due to its length of %s characters...' % len(url)

####################################################