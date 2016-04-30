import requests
from bs4 import BeautifulSoup
import socket
from urllib.parse import urlparse



seed = set([input('Seed: ')])
done = set()
known = {}

total = 1

while seed:
    try:
        target = seed.pop()
        if target in done:
            continue
        done.add(urlparse(target).netloc)
        ip = socket.gethostbyname(urlparse(target).netloc)
        website = BeautifulSoup(requests.get(target).text, "html.parser")
        links = website.find_all('a', href=True)
        for link in links:
            link = link['href']
            if urlparse(link).netloc in seed or urlparse(link).netloc in done:
                continue
            if link.startswith("http://"):
                seed.add(link)
                known.setdefault(ip, [])
                if socket.gethostbyname(urlparse(link).netloc) not in known[ip]:
                    known[ip].append(socket.gethostbyname(urlparse(link).netloc))
                    print(total, ip, '->', socket.gethostbyname(urlparse(link).netloc))
                    total += 1
                    requests.get("http://127.0.0.1:8000/new_path/?from_ip={}&to_ip={}".format(
                        ip, socket.gethostbyname(urlparse(link).netloc)
                    ))
    except:
        pass
