from currency_converter import CurrencyConverter
import requests
from bs4 import BeautifulSoup

class Exchange:

    def __init__(self):
        self.currencies = 0


    def get_all_currencies(self):
        cc = CurrencyConverter()
        return cc.currencies

    def change_usd_to_krw(self):
        cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
        return cc.convert(1, 'USD', 'KRW')

    def get_exchange_rate(target1, target2):
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Content-Type': 'text/html; charset=utf-8'
        }

        response = requests.get(r"https://kr.investing.com/currencies/{target1}, {target2}", headers=headers)
        content = BeautifulSoup(response.content, 'html.parser')
        containers = content.find('span', {'data-test': 'instrument-price-last'})
        return containers.text


if __name__ == '__main__':
    e = Exchange()
    ead_file_path = r"9. 영어로된 문서를 한글로 자동번역\영어파일.txt"
    write_file_path = r"9. 영어로된 문서를 한글로 자동번역\한글파일.txt"

    with open(read_file_path, 'r') as f:
        readLines = f.readlines()

    for lines in readLines:
        result1 = translator.translate(lines, dest='ko')
        print(result1.text)
        with open(write_file_path, 'a', encoding='UTF8') as f:
            f.write(result1.text + '\n')

