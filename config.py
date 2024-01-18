from pathlib import Path
import time

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Chromium";v="118", "YaBrowser";v="23.11", "Not=A?Brand";v="99", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36',
}

urls = [
    'https://gas-kvas.com/uploads/posts/2023-02/1675483689_gas-kvas-com-p-fonovii-risunok-dlya-kompyutera-priroda-15.jpg',
    'https://opdm.su/wa-data/public/shop/products/44/28/2844/images/2059/2059.750x0.jpg',
    'https://mykaleidoscope.ru/x/uploads/posts/2022-09/1663189031_3-mykaleidoscope-ru-p-stolitsa-chernozemya-dostoprimechatelnosti-3.jpg']


def download_dir(val: str) -> str:
    """
    Проверка директории сохранения
    :param val: str
    :return path dir: str
    """
    if not Path(f'{val}_dowload_img').exists():
        Path(f'{val}_dowload_img').mkdir()
    return f'{val}_dowload_img'


def working_hours(fanc):
    """
    Вычисление затраченного времени на операцию
    :param fanc:
    :return:
    """

    def wraper(*args, **kwargs):
        start_time = time.time()
        fanc(*args, **kwargs)
        print(f'Общее время работы: {time.time() - start_time:.2f} сек')

    return wraper
