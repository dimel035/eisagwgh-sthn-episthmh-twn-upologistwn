import urllib2
def findthosethings(url):
    response = urllib2.urlopen(url)
    html = response.read()
    x=html.count("<br>")
    y=html.count("</p>")
    z=html.count("href=")
    a=x+y
    print "Number of links: ",z
    print "Number of line changes: ",a



def check(url):
    while url=="":
        url=raw_input("Please give URL: ")
    return url


url=raw_input("please give URL: ")
url=check(url)
findthosethings(url)
