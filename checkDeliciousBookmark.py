#!/usr/bin/python3
# -*- coding: utf-8 -*-


from HTMLParser import HTMLParser
import requests

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print_tag = False
	       for attr in attrs:
	              if attr[0] == 'href':
			         try:
				#print "Trying ",attr[1]
				res = requests.get(attr[1])
			except:
                                print "Error on : ", attr[1]
                                print_tag=True
                if print_tag and attr[0] == 'tags':
                        print 'tags: ', attr[1]
                        print_tag=False

    def handle_endtag(self, tag):
	pass
    def handle_data(self, data):
	pass


# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')

with open('delicious.html') as source:
	for line in source:
		parser.feed(line)
