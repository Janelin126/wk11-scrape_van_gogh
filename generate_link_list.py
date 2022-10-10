from bs4 import BeautifulSoup
import requests

limit= 10 # retrieve the first 10 links
url = 'https://en.wikipedia.org/wiki/List_of_works_by_Vincent_van_Gogh'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
links = []
links_list = []
error_log = []

for link in soup.select('.wikitable .image'):
    links.append(link['href'])

for media_page in links[0:limit]:
    req = requests.get('https://en.wikipedia.org' + media_page)
    soup = BeautifulSoup(req.text, 'html.parser')
    img_div = soup.find('div', {'class': 'mw-filepage-resolutioninfo'})# you can change this for different size images
    try:
        img_path = 'https:' + img_div.find('a')['href'] #find
        links_list.append(img_path)
        print(img_path)
    except:
        failed_msg = "couldn't add link for: " + media_page
        error_log.append(failed_msg)
        print(failed_msg)

txt_file = open('download.txt', 'w')
for line in links_list:
     txt_file.write(line)
     txt_file.write('\n')
txt_file.close()

error_file = open('errors.txt', 'w')
for line in error_log:
     error_file.write(line)
     error_file.write('\n')
error_file.close()

# 5. run the script using: python3 generate_link_list(file name).py
#links show on terminal are the scraped data, copy and paste in url box.
# if you want to download the images, use: xargs -n 1 curl -O < download.txt
