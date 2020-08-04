from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.4icu.org//us//a-z//"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
page_soup = page_soup.tbody

rows = page_soup.findAll("tr", attrs={'class': None}) # this is a list 

filename = "colleges.csv"
f = open(filename, "w")

header = "College Name\n"
f.write(header)

for row in rows:
    college = row.findAll("a")[0].text
    college = college.replace(",", "|")
    f.write(college + "\n")
    print(college)

f.close()
