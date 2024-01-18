import sys
import threading

import requests

from config import headers, download_dir, urls, working_hours

root_path = download_dir('thread')


def dowload_img(url):
    response = requests.get(url, headers=headers)
    filename = url.split('/')[-1]
    with open(f'{root_path}/{filename}', 'wb') as file:
        file.write(response.content)


@working_hours
def main(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=dowload_img, args=[url])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        urls = sys.argv[1:]
    main(urls)
