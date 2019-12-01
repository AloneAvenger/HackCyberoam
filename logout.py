#!/usr/bin python

import urllib
import time
import datetime
import urllib2
import sys
import xml.dom.minidom as XML

#CountDown And Credits
def countdown(num):
    for i in xrange(num,0,-1):
        time.sleep(1)
        sys.stdout.write(str(i%10)+'\r')
        sys.stdout.flush()
        



username = raw_input("enter user id :")


def sendLogoutRequest(username):
    url = 'http://172.29.0.1:8090/httpclient.html'
    post_data = 'mode=193' + '&username=' + username
    req = urllib2.Request(url, post_data)
    response = urllib2.urlopen(req)
    print response
    print 'logout.'

sendLogoutRequest(username)
