# To The Max ![Image](https://camo.githubusercontent.com/9e95bcdd01de99de22be89233b899f4579e24902/687474703a2f2f696d672e736869656c64732e696f2f62616467652f4275696c7425323061742d253233646f74617374726f2d626c75652e7376673f7374796c653d666c6174?raw=true)

Simple Python code to wrap around http://koalastothemax.com for custom display of a set of images. 

## Input 
A text file containing a list of URLs to images to be included in the custom set of images. Each URL should be on a new line, as in the example file.

## To run
Default settings (input file: apodurl.txt, number of images: 5):

`python tothemax.py`

Custom settings (input file: custom.txt, number of images: N):

`python tothemax.py custom.txt N`

## Sharing #tothemax
If possible, please share your custom image sets (to the max) on Twitter with the hashtag #tothemax so that a #tothemax compilation can be constructed :) It might also be useful to tag me (@cosmicpudding) or add #dotastro to differentiate from the other intense #tothemax people out there. 

## Tips/notes
* Images will be automatically rescaled to a square shape regardless of original dimensions. 
* List is truncated by default to 75, to account for estimated server URL limitations. If you get a "Request-URI too large" error, reduce the number of images. 
* Convert the long URL containing base64 format to a tinyurl for clarity, e.g. http://tinyurl.com/apodtothemax
