from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://leetcode.com/accounts/login/')
time.sleep(30)


urls = []
titles = []

for i in range(46):

    driver.get('https://leetcode.com/problemset/all/?page=' + str(i+1))

    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    all_ques_div = soup.findAll('a', {'class': 'h-5'})

    for q in all_ques_div:

        urls.append("https://leetcode.com"+q.get('href'))
        titles.append(q.text.split(' ', 1)[1])


with open('problems_urls.txt', 'w+') as f:
    f.write('\n'.join(urls))

with open('problems_titles.txt', 'w+') as f:
    f.write('\n'.join(titles))


cnt = 0
for url in urls:
    driver.get(url)
    cnt += 1
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    if soup.find('div', {'class': 'description__24sA'}):
        problem_text = soup.find('div', {"class": "content__u3I1"}).get_text()
    else:
        problem_text = ''

    # print(problem_text)
    problem_text = problem_text.encode("utf-8")
    problem_text = str(problem_text)

    path = 'problems/'
    file = "problem"+str(cnt)+".txt"

    fileName = os.path.join(path, file)

    with open(fileName, "w+") as f:
        f.write(problem_text)
