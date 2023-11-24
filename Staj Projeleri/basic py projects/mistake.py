links = [
    'www..io',
    'www.youtube.com',
    'www.google.com',
    'www.wikipedia.org',
]

#for link in links:
    #print(link.lstrip("w."))



for link in links:
    print(link.removeprefix("www."))