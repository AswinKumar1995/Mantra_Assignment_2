#program is complete

import tldextract # package for extracting main domain and subdomains(pip install tldextract)
URL1 = "https://blog.microsoft.com/test.html"
URL2 = "https://www.blog.microsoft.com/test/test"
URL3 = "https://www.microsoft.com"
def getSubDomain(URL):
    print(f"URL  : {URL}")
    URL = URL.replace("www.","").replace("http://","").replace("https://","").lower()
    mainDomain = tldextract.extract(URL).domain.lower()
    subDomain = tldextract.extract(URL).subdomain.lower()
    print(f"MainDomain : {mainDomain}")
    if(subDomain == ""):
        print("No SubDomain")
    else:
        print(f"SubDomain present : {subDomain}")
    return subDomain,mainDomain
subDomain,mainDomain = getSubDomain(URL1)
subDomain,mainDomain = getSubDomain(URL2)
subDomain,mainDomain = getSubDomain(URL3)
