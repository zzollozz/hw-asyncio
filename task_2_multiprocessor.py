import sys
from multiprocessing import Process

import requests

from config import headers, download_dir, urls, working_hours

root_path = download_dir('multiproc')


def dowload_img(url):
    filename = url.split('/')[-1]
    response = requests.get(url, headers=headers)

    with open(f'{root_path}/{filename}', 'wb') as file:
        file.write(response.content)


@working_hours
def main(urls):
    processes = []
    for url in urls:
        process = Process(target=dowload_img, args=(url,))
        processes.append(process)
        process.start()

    for proc in processes:
        proc.join()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        urls = sys.argv[1:]
    main(urls)
