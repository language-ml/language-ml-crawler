from tqdm import tqdm
import requests
from bs4 import BeautifulSoup


with open('download_log.txt', 'r+') as f:
    lecture_names = f.readlines()
lecture_names = [i.strip() for i in lecture_names]

base_url = 'https://{user}:{pass}@language.ml/courses/nlp14022/'

# user = 
# pass_ = 

page = requests.get(f'https://{user}:{pass_}@language.ml/courses/nlp14022/index.html')

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('tbody')
trs = table.find_all('tr')

for i in tqdm(trs):
    tds = i.find_all('td')
    print(tds[0].string)
    print('-'*10)
    
    if tds[0].string in lecture_names and tds[0].string!=None:
        continue
        
    lecture_names.append(tds[0].string)
    if tds[2].a!=None:
        print(base_url+tds[2].a.get('href'))
        r = requests.get(base_url+tds[2].a.get('href'), auth=(user, pass_))
        with open(tds[0].string+'.pdf', 'wb') as f:
            f.write(r.content)
    if tds[3].a!=None:
        print(base_url+tds[3].a.get('href'))
        r = requests.get(base_url+tds[3].a.get('href'), auth=(user, pass_))
        with open(tds[0].string+'.mp4', 'wb') as f:
            f.write(r.content)
        

lecture_names = [i for i in lecture_names if i!=None]
with open('download_log.txt', 'w') as f:
    f.write('\n'.join(lecture_names))
