from xml.dom import minidom


dom = minidom.parse("artisteDevoir.xml")

artistes = dom.getElementsByTagName('artiste')

for artiste in artistes:
    nom = artiste.getAttribute('nom')
    print(f"Nom: {nom}")
    
    site = artiste.getElementsByTagName('site')[0]
    url = site.getAttribute('url')
    print(f"URL: {url}")
    
    ville = artiste.getAttribute('ville')
    print(f"Ville: {ville}")
    
    biographie = artiste.getElementsByTagName('biographie')[0].firstChild.nodeValue
    print(f"Biographie: {biographie}")
    
    print("")  


dom.unlink()
