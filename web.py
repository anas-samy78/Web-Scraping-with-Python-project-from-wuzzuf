import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs
import requests
import csv
from urllib.parse import urljoin

url_1 = "https://wuzzuf.net/search/jobs?q=data%20analysis&start=0&a=hpb"

url_open = requests.get(url_1)


def main(url_open):

    soup = bs(url_open.content,"lxml")
    wuzzuf = soup.find_all("div",{"class":"css-ghe2tq e1v1l3u10"})
    print(len(wuzzuf))
    #print(wuzzuf)
    print("="*100)

    titles = []
    companies = []
    addresses = []
    jobs_type = []
    workplaces = []
    skills = []
    links = []

    for x in range(47):

        url_1 = f"https://wuzzuf.net/search/jobs?q=data%20analysis&start={x}&a=hpb"
        url_open = requests.get(url_1, timeout=15)

        soup = bs(url_open.content,"lxml")
        wuzzuf = soup.find_all("div",{"class":"css-ghe2tq e1v1l3u10"})
        #print(len(wuzzuf))

        for i in range(len(wuzzuf)):

            titel = wuzzuf[i].find("h2",{"class":"css-193uk2c"})
            cname = wuzzuf[i].find("a",{"class":"css-ipsyv7"})
            address = wuzzuf[i].find("span",{"class":"css-16x61xq"})
            job_type = wuzzuf[i].find("span",{"class":"css-uc9rga eoyjyou0"})
            workplace = wuzzuf[i].find("span",{"class":"css-uofntu eoyjyou0"})
            skill = list(wuzzuf[i].find("div",{"class":"css-1rhj4yg"}))[-1]
            link = titel.find("a",{"class":"css-o171kl"}).attrs["href"]
            link = urljoin("https://wuzzuf.net",titel.find("a",{"class":"css-o171kl"}).attrs["href"])

            titles.append(titel.text.strip())
            companies.append(cname.text.strip())
            addresses.append(address.text.strip())
            jobs_type.append(job_type.text.strip())
            workplaces.append(workplace.text.strip())
            skills.append(skill.text.strip())
            links.append(link)

            #print(titel)
            #print(cname)
            #print(address)
            #print(job_type)
            #print(workplace)
            #print(skill)

        df = pd.DataFrame({
                "Job titel":titles,
                "Company name":companies,
                "Address":addresses,
                "Job type":jobs_type,
                "Workplace":workplaces,
                "Job skills":skills,
                "Links":links,
                })
        #print(df)
        df.to_csv("Jobs.csv",index=False)

main(url_open)

print("="*100)
