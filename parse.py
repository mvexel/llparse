#!/usr/bin/python

import sys
import cgi
import re 

if __name__ == "__main__":
    #print "Content-Type: text/html\n"
    lon = 0.0
    lat = 0.0
    zoom = 17
    arguments = cgi.FieldStorage()
    if not "dirtystring" in arguments:
        print "Status: 500 Internal Server Error"
    else:
        dirtystring = arguments["dirtystring"].value
        #print dirtystring
        coordinates = re.findall('-*\d+\.\d+', dirtystring)
        if len(coordinates) != 2:
            print "500 Internal Server Error"
        for coord in coordinates:
            coord = float(coord)
            if coord > 0: 
                lat = coord
            else:
                lon = coord
    if "zoom" in arguments:
        zoom = int(arguments["zoom"].value)
    osmurl = "http://osm.org/?mlon=%f&mlat=%f&zoom=%i" % (lon, lat, zoom)
    sys.stdout.write("Status: 302 Moved\r\nLocation: %s\r\n\r\n" % osmurl)
