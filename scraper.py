import requests
from bs4 import BeautifulSoup
from selenium import webdriver



def airbnb_jobs():
    address = 'https://www.airbnb.com/careers/departments'
    html = requests.get(address).text
    soup = BeautifulSoup(html, 'html.parser')
    anchors = soup.find_all("a", class_="jobs-card link-reset")
    urls = []
    for link in anchors:
        urls.append("https://www.airbnb.com" + link.get('href'))

    links = []
    jobs = []

    for url in urls:
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        try:
            soup.tbody.find_all('a')
        except:
            continue
        links.append(soup.tbody.find_all('a'))
    for link in links:
        for idx, anchor in enumerate(link):
            if (idx % 2 == 0):
                jobs.append([anchor.get_text()])
            else:
                jobs.append(jobs[-1].append(anchor.get_text()))

    return __clean_airbnb_data(jobs)



def twilio_jobs():
    address = 'https://www.twilio.com/company/jobs'
    result = []

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(address)

    html = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html, 'html.parser')
    jobs = soup.find_all("div", class_="accordion-heading")
    jobs = jobs[0].find_all('a')

    for anchors in jobs:
        location = anchors.find_all('span')[0].get_text()
        title = anchors.get_text().split(location)[0]
        result.append([title,location])

    return __clean_twilio_data(result)


def __clean_airbnb_data(jobs):
    result = []
    for job in jobs:
        if job != None:
            result.append(job)
    return result

def __clean_twilio_data(arr):
    result = []
    for job in arr:
        if job[0] == '':
            continue
        else:
            result.append(job)
    return result
