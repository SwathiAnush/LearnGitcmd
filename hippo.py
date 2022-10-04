#re -->regex
import re
#request-->the only Non-GMO HTTP library for Python
import requests
#BS4 is used to extract data out of html or xml
from bs4 import BeautifulSoup

url=" https://www.k7computing.com/in/"
response=requests.get(url)

soup=BeautifulSoup(response.text,"html.parser")
image_tags=soup.find_all('img')

urls=[img['src'] for img in image_tags]

for pic in urls:
    filename=re.search(r'/([w_-]+[.](jpg|gif|png))$',pic)
    with open(filename.group(1),'wb') as f:
        if 'http' not in pic:
            pic='{}{}'.format(url,pic)
        response=requests.get(pic)
        f.write(response.content)




