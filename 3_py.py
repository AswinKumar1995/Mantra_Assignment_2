#program is complete

#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import Request, urlopen
import urllib
from bs4 import BeautifulSoup
import time
import tldextract
class main:
    def __init__(self,URL,maxLinks):
        self.URL = URL
        self.maxLinks = maxLinks
        self.pageProperties = []
        self.process()   
    def get_domains(self,URL): #extracts only subdomains for URL
        print(f"URL  : {URL}")
        URL = URL.replace("www.","").replace("http://","").replace("https://","").lower()
        mainDomain = tldextract.extract(URL).domain.lower()
        subDomain = tldextract.extract(URL).subdomain.lower()
        print(f"MainDomain : {mainDomain}")
        if(subDomain == ""):
            print("No SubDomain")
        else:
            print(f"SubDomain present : {subDomain}")
        return subDomain
    
    def success(self,pageProperty,url): 
        subDomain = self.get_domains(url)
        pageProperty['subDomain'] = subDomain
        pageProperty['url'] = url
        self.pageProperties.append(pageProperty)
        
    def download(self,URL): # downloads the url as soup object
        try:
            url = URL.replace("//","||").split("/")[0].replace("||","//").replace("https://","http://")
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'}
            response = Request(url,headers=headers)
            page = urllib.request.urlopen(response,timeout=120)
            soup = BeautifulSoup(page)
            pageProperty = {'html':soup,'status':'success'}
            self.success(pageProperty,url)
        except Exception as error:
            print(error)
            self.pageProperties.append({'html':'','status':'failure','subDomain':'','url':URL})
            
    def process(self): # extracting the URLS from given URL
        url = URL.replace("//","||").split("/")[0].replace("||","//").replace("https://","http://")
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'}
        response = Request(url,headers=headers)
        page = urllib.request.urlopen(response,timeout=120)
        soup = BeautifulSoup(page)
        rawHrefList = []
        for atag in soup.find_all("a"): # extract all urls in home page
            try:
                route = atag.get("href")  # extract href
                if(route != None):
                    if("http" in route):
                        rawHrefList.append(route)
                        if(len(rawHrefList) > self.maxLinks):
                            break
                    else:
                        pass
                else:
                    pass
            except Exception as URLError:
                print("URL error : "+str(URLError))
                pass
        urls_queue = list(set(rawHrefList))
        for domainURL in urls_queue:
            self.download(domainURL)
            time.sleep(1)       


URL = input("Please input the URL to be parsed")
maxLinks = int(input("Mention the max links to be extracted : "))
mainObject = main(URL,maxLinks)
results_map = mainObject.pageProperties
print(results_map)

