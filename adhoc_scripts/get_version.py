#!/usr/bin/env python3.6

import requests
import xml.etree.ElementTree as ET

def getSite():
    
    confluence = 'https://confluence.atlassian.com/rest/applinks/latest/manifest?_ga=2.218951257.1304743660.1557864921-526801536.1555455902'

    resp = requests.get(confluence)
    print(dir(resp))
    rc = resp.status_code

    if rc == 200:

        print(f"Confluence receives {rc} assuming app is up.")
        
        with open('confluence.xml',  'wb') as f:
            f.write(resp.content)
    else:
        print(f"Confluence is down")

def getVer(xmlFile):

    tree = ET.parse(xmlFile)
    root = tree.getroot()

    for item in root.findall("./version"):
        ver = item.text
        print(f"Conflunence version is: {ver}")

def main():
    getSite()
    
    getVer('confluence.xml')

if __name__ == "__main__":
    main()