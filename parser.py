
import requests
from bs4 import BeautifulSoup

from .params import headers


class RequestGet:

    def extract_parser(self, url: str, job: str) -> int:
        """Создаем запрос к сайту"""
        params = {
            'text': job,
            'salary': '',
            'ored_clusters': 'true',
            'enable_snippets': 'true',
            'area': '66',
            'hhtmFrom': 'vacancy_search_list',
            'hhtmFromLabel': 'vacancy_search_line',

        }

        response = requests.get(url, params=params, headers=headers)

        hh_soup = BeautifulSoup(response.text, 'html.parser')

        paginator = hh_soup.find('ul', {'class': 'magritte-number-pages-container___YIJLn_4-0-14'})
        links = []
        if paginator:
            for page in paginator:
                links.append(int(page.find('a').text))
            # Последняя страница
        else:
            links.append(1)  # Если пагинации нет, значит одна страница

        return links[-1]


class ParsingData:

    def extract_jobs_dict(self, html) -> dict:
        """Находим нужные данные со страницы HTML"""
        name_vacancy = html.find('a').text
        link_vacany = html.find('a')['href']
        company = html.find('div', {'class': 'company-name-badges-container--kC8yYUJPFyg6J6XQs62Y'}).find('a').text
        location = html.find('span', {'data-qa': 'vacancy-serp__vacancy-address'}).text.partition(',')[0]
        return {'title': name_vacancy, 'company': company, 'location': location, 'link': link_vacany}

    def extract_jobs(self, max_pages: int, url: str, job: str):
        jobs = []
        for page in range(max_pages):
            print(f'Парсинг страницы {page + 1} из {max_pages}')
            params = {
                'text': job,  # Передаем введенную вакансию вместо python
                'salary': '',
                'ored_clusters': 'true',
                'enable_snippets': 'true',
                'area': '66',
                'hhtmFrom': 'vacancy_search_list',
                'hhtmFromLabel': 'vacancy_search_line',
                'page': page  # Добавляем номер страницы
            }

            result = requests.get(url, params=params, headers=headers)
            soup = BeautifulSoup(result.text, 'html.parser')

            vacancy = soup.find_all('div', {'class': 'magritte-redesign'})

            for result in vacancy:
                jobs.append(self.extract_jobs_dict(result))
        return jobs


class GetJobs(RequestGet, ParsingData):

    def get_jobs(self, job: str) -> list:
        """Получаем вакансии"""
        url = f'https://nn.hh.ru/search/vacancy'
        max_page = self.extract_parser(url, job)
        print(f'Найдено {max_page} страниц')
        jobs = self.extract_jobs(max_page, url, job)
        return jobs
