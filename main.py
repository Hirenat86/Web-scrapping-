from pprint import pprint
import requests
import bs4


KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/articles/')
soap = bs4.BeautifulSoup(response.text, 'lxml')

articles_list = soap.select_one('div.tm-articles-list')

articles = articles_list.select('.tm-articles-list__item')

parsed_data = []

for article in articles:
    for keyword in KEYWORDS:
        if keyword.lower() in article.select_one('a.tm-title__link').text.lower():
            link = f'https://habr.com{article.select_one('a.tm-title__link')['href']}'
            header = article.select_one('a.tm-title__link').text.strip()
            data_article = article.select_one('time')['title']
            parsed_data.append(f'{data_article} - {header} - {link}')

pprint(parsed_data)
