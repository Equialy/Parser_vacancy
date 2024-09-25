import pprint

import requests
from bs4 import BeautifulSoup


cookies = {
    '__ddg1_': '5HJVnYRlMHbAYswDWZFC',
    'hhuid': 'vr1Wrj3eXRNI72bcrkg_Lw--',
    'tmr_lvid': 'c734fca4716de78cc32d64c53582e38e',
    'tmr_lvidTS': '1725738571009',
    '_ym_uid': '1725738571912886020',
    '_ym_d': '1725738571',
    'iap.uid': '7af1039a01f940f384919e0ceb73ac1a',
    'redirect_host': 'nn.hh.ru',
    'region_clarified': 'nn.hh.ru',
    'device_magritte_breakpoint': 'l',
    'device_breakpoint': 'l',
    'cookie_policy_agreement': 'true',
    '__zzatgib-w-hh': 'MDA0dC0jViV+FmELHw4/aQsbSl1pCENQGC9LX3YyPGgjGk5cJHlZVApZThZ4JVUKDgsVQHJveio/alEZOVURCxIXRF5cVWl1FRpLSiVueCplJS0xViR8SylEXE9/JRkWfXEoWAoTVy8NPjteLW8PKhMjZHYhP05yHv3YrQ==',
    '__zzatgib-w-hh': 'MDA0dC0jViV+FmELHw4/aQsbSl1pCENQGC9LX3YyPGgjGk5cJHlZVApZThZ4JVUKDgsVQHJveio/alEZOVURCxIXRF5cVWl1FRpLSiVueCplJS0xViR8SylEXE9/JRkWfXEoWAoTVy8NPjteLW8PKhMjZHYhP05yHv3YrQ==',
    '_ym_isad': '1',
    'domain_sid': 'XVCZxNKUBXGaVZB0x2fyq%3A1727208142357',
    'uxs_uid': 'd0d5a500-6f94-11ef-b8cb-451e7b4d3945',
    '_xsrf': '1ff9aca9cf6636ff737b8576ff06f7a2',
    'hhrole': 'anonymous',
    'hhtoken': 'zyU_SOqJLKylnLgSSmuv8PNJUc2y',
    'regions': '66',
    'display': 'desktop',
    'crypted_hhuid': 'C4193D1F13CA9E39FBBC4B5D1C8E491977F2D752325012CD95CA2F792771FF4D',
    'GMT': '3',
    '_ym_visorc': 'b',
    'cfidsgib-w-hh': 'X9h/Tnf2DpfILfAnlGJyOqg7RKXG65h+ScO7fJHQ0XBIfAZhI4ljdnCzf0eFwVsQhQ8oeHceeWUR3JcDq0+dM11a5L7XgCPPCHwOBn0XvsmFNIbJeQM24M1CYECTK6v3EVvQ7J+DY6DvqxRVXVBJ/nat/ZnviHs8G/JRElE=',
    'cfidsgib-w-hh': 'X9h/Tnf2DpfILfAnlGJyOqg7RKXG65h+ScO7fJHQ0XBIfAZhI4ljdnCzf0eFwVsQhQ8oeHceeWUR3JcDq0+dM11a5L7XgCPPCHwOBn0XvsmFNIbJeQM24M1CYECTK6v3EVvQ7J+DY6DvqxRVXVBJ/nat/ZnviHs8G/JRElE=',
    'gsscgib-w-hh': 'MxjsHOph3BHT4sMTfrkkkIq788g9nXP3Pm08WcU6racWcJ0diWo9T6UsZLfM5M7vPMSpVDVj2h29vMpbl7tyrME4QEVLL5IEe0QIaFm/ERXjL95dYb2HQV6EcwHpX6T6neF3zAm9EFyuNP5M+h+m2VGJjD1FDPwyj6wyIo5Mx6/v4O1f5zPDA6ZjsYPfYZ7dlkWC3+Dnum87lIt3rZBCpp2GwUMmAIQQRMosxY7b4TGBFdrnceK5V5tsGnpazoZ3cA==',
    'gsscgib-w-hh': 'MxjsHOph3BHT4sMTfrkkkIq788g9nXP3Pm08WcU6racWcJ0diWo9T6UsZLfM5M7vPMSpVDVj2h29vMpbl7tyrME4QEVLL5IEe0QIaFm/ERXjL95dYb2HQV6EcwHpX6T6neF3zAm9EFyuNP5M+h+m2VGJjD1FDPwyj6wyIo5Mx6/v4O1f5zPDA6ZjsYPfYZ7dlkWC3+Dnum87lIt3rZBCpp2GwUMmAIQQRMosxY7b4TGBFdrnceK5V5tsGnpazoZ3cA==',
    'gsscgib-w-hh': '01st2FImfd3O9xmKTNRcAOIk2OQkky1dzBdcSE3cDE6x65BXgpQw4slpWBCoD4wqXplROf8+ALOYw3GYrxZ2TqukhM0BC87rSP9qiFk9nvMs5LlwJ4b74LXD8AviW2sE+xefigsgwfMNHqxQ7PB1UkqezJL2BHLhP2bNZEWABd0niWtM+7N+XoW5vUdXPsbC7ewX685yiANLGt20UBRknhrxcG9BJG+uFKsMZY0elfdBO5G2kY7jlvbw9MOAEw2JaA==',
    'cfidsgib-w-hh': 'CO7mG1a2yb3jM2CI6aUpnrxPi5+Y2KUsP163FDKyIROBT4yQW+OyhMuVByOBJejpAegvkEzxBYGMcvwVGM8p9exQ4jchFEEMhkfej5h6vGY8SuhtQAPMf68InDCKraqTA3Oy8VbYP6EzjkbstmC9XfUfeY61Tnr6ZD1S/OY=',
    'total_searches': '1',
    'tmr_detect': '1%7C1727268437220',
    'fgsscgib-w-hh': 'efAj203f5aad9f34de0940b8437772f958c632d9',
    'fgsscgib-w-hh': 'efAj203f5aad9f34de0940b8437772f958c632d9',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9',
    # 'cookie': '__ddg1_=5HJVnYRlMHbAYswDWZFC; hhuid=vr1Wrj3eXRNI72bcrkg_Lw--; tmr_lvid=c734fca4716de78cc32d64c53582e38e; tmr_lvidTS=1725738571009; _ym_uid=1725738571912886020; _ym_d=1725738571; iap.uid=7af1039a01f940f384919e0ceb73ac1a; redirect_host=nn.hh.ru; region_clarified=nn.hh.ru; device_magritte_breakpoint=l; device_breakpoint=l; cookie_policy_agreement=true; __zzatgib-w-hh=MDA0dC0jViV+FmELHw4/aQsbSl1pCENQGC9LX3YyPGgjGk5cJHlZVApZThZ4JVUKDgsVQHJveio/alEZOVURCxIXRF5cVWl1FRpLSiVueCplJS0xViR8SylEXE9/JRkWfXEoWAoTVy8NPjteLW8PKhMjZHYhP05yHv3YrQ==; __zzatgib-w-hh=MDA0dC0jViV+FmELHw4/aQsbSl1pCENQGC9LX3YyPGgjGk5cJHlZVApZThZ4JVUKDgsVQHJveio/alEZOVURCxIXRF5cVWl1FRpLSiVueCplJS0xViR8SylEXE9/JRkWfXEoWAoTVy8NPjteLW8PKhMjZHYhP05yHv3YrQ==; _ym_isad=1; domain_sid=XVCZxNKUBXGaVZB0x2fyq%3A1727208142357; uxs_uid=d0d5a500-6f94-11ef-b8cb-451e7b4d3945; _xsrf=1ff9aca9cf6636ff737b8576ff06f7a2; hhrole=anonymous; hhtoken=zyU_SOqJLKylnLgSSmuv8PNJUc2y; regions=66; display=desktop; crypted_hhuid=C4193D1F13CA9E39FBBC4B5D1C8E491977F2D752325012CD95CA2F792771FF4D; GMT=3; _ym_visorc=b; cfidsgib-w-hh=X9h/Tnf2DpfILfAnlGJyOqg7RKXG65h+ScO7fJHQ0XBIfAZhI4ljdnCzf0eFwVsQhQ8oeHceeWUR3JcDq0+dM11a5L7XgCPPCHwOBn0XvsmFNIbJeQM24M1CYECTK6v3EVvQ7J+DY6DvqxRVXVBJ/nat/ZnviHs8G/JRElE=; cfidsgib-w-hh=X9h/Tnf2DpfILfAnlGJyOqg7RKXG65h+ScO7fJHQ0XBIfAZhI4ljdnCzf0eFwVsQhQ8oeHceeWUR3JcDq0+dM11a5L7XgCPPCHwOBn0XvsmFNIbJeQM24M1CYECTK6v3EVvQ7J+DY6DvqxRVXVBJ/nat/ZnviHs8G/JRElE=; gsscgib-w-hh=MxjsHOph3BHT4sMTfrkkkIq788g9nXP3Pm08WcU6racWcJ0diWo9T6UsZLfM5M7vPMSpVDVj2h29vMpbl7tyrME4QEVLL5IEe0QIaFm/ERXjL95dYb2HQV6EcwHpX6T6neF3zAm9EFyuNP5M+h+m2VGJjD1FDPwyj6wyIo5Mx6/v4O1f5zPDA6ZjsYPfYZ7dlkWC3+Dnum87lIt3rZBCpp2GwUMmAIQQRMosxY7b4TGBFdrnceK5V5tsGnpazoZ3cA==; gsscgib-w-hh=MxjsHOph3BHT4sMTfrkkkIq788g9nXP3Pm08WcU6racWcJ0diWo9T6UsZLfM5M7vPMSpVDVj2h29vMpbl7tyrME4QEVLL5IEe0QIaFm/ERXjL95dYb2HQV6EcwHpX6T6neF3zAm9EFyuNP5M+h+m2VGJjD1FDPwyj6wyIo5Mx6/v4O1f5zPDA6ZjsYPfYZ7dlkWC3+Dnum87lIt3rZBCpp2GwUMmAIQQRMosxY7b4TGBFdrnceK5V5tsGnpazoZ3cA==; gsscgib-w-hh=01st2FImfd3O9xmKTNRcAOIk2OQkky1dzBdcSE3cDE6x65BXgpQw4slpWBCoD4wqXplROf8+ALOYw3GYrxZ2TqukhM0BC87rSP9qiFk9nvMs5LlwJ4b74LXD8AviW2sE+xefigsgwfMNHqxQ7PB1UkqezJL2BHLhP2bNZEWABd0niWtM+7N+XoW5vUdXPsbC7ewX685yiANLGt20UBRknhrxcG9BJG+uFKsMZY0elfdBO5G2kY7jlvbw9MOAEw2JaA==; cfidsgib-w-hh=CO7mG1a2yb3jM2CI6aUpnrxPi5+Y2KUsP163FDKyIROBT4yQW+OyhMuVByOBJejpAegvkEzxBYGMcvwVGM8p9exQ4jchFEEMhkfej5h6vGY8SuhtQAPMf68InDCKraqTA3Oy8VbYP6EzjkbstmC9XfUfeY61Tnr6ZD1S/OY=; total_searches=1; tmr_detect=1%7C1727268437220; fgsscgib-w-hh=efAj203f5aad9f34de0940b8437772f958c632d9; fgsscgib-w-hh=efAj203f5aad9f34de0940b8437772f958c632d9',
    'priority': 'u=0, i',
    'referer': 'https://nn.hh.ru/search/vacancy?text=python&area=66&hhtmFrom=main&hhtmFromLabel=vacancy_search_line',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "YaBrowser";v="24.7", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 YaBrowser/24.7.0.0 Safari/537.36',
}

params = {
    'text': 'python',
    'salary': '',
    'ored_clusters': 'true',
    'enable_snippets': 'true',
    'area': '66',
    'hhtmFrom': 'vacancy_search_list',
    'hhtmFromLabel': 'vacancy_search_line',
    'page':0,
}


# url_main = 'https://nn.hh.ru/search/vacancy'
def extract_parser(url: str) -> int:
    """Создаем запрос к сайту"""
    response = requests.get(url, params=params, cookies=cookies, headers=headers)

    hh_soup = BeautifulSoup(response.text, 'html.parser')

    paginator = hh_soup.find('ul', {'class': 'magritte-number-pages-container___YIJLn_4-0-14'}).find('a').text

    if paginator:
        max_page = int(paginator[-1])  # Последняя страница
    else:
        max_page = 1  # Если пагинации нет, значит одна страница

    return max_page


def extract_jobs_dict(html) -> dict:
    """Находим нужные данные со страницы HTML"""
    name_vacancy = html.find('a').text
    link_vacany = html.find('a')['href']
    company = html.find('div', {'class': 'company-name-badges-container--kC8yYUJPFyg6J6XQs62Y'}).find('a').text
    location = html.find('span', {'data-qa': 'vacancy-serp__vacancy-address'}).text.partition(',')[0]
    return {'title': name_vacancy, 'company': company, 'location': location, 'link': link_vacany}


def extract_jobs(max_pages: int, url: str):
    jobs = []
    for page in range(max_pages):
        pprint.pprint(f'Парсинг страницы {page}')
        params['page'] = page #Номер страницы в параметр запроса
        result = requests.get(f'{url}&page={page}', headers=headers)
        soup = BeautifulSoup(result.text, 'html.parser')

        vacancy = soup.find_all('div', {'class': 'magritte-redesign'})
        for result in vacancy:
            jobs.append(extract_jobs_dict(result))
    return jobs

def get_jobs(job: str)->list:
    """Получаем вакансии"""
    url = f'https://nn.hh.ru/search/vacancy'
    max_page = extract_parser(url)
    jobs = extract_jobs(max_page, url)
    return jobs