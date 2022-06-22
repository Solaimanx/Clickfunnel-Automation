import requests
import concurrent.futures
import time



def main():
    for i in range(1000,2001):
        url = "https://www.larvalabs.com/cryptopunks/cryptopunk{}.png".format(i)
        response = requests.get(url)
        if response.status_code == 200:
            with open("/Users/mohammadsolaiman/Downloads/CryptoPunk/cryptopunk{}.png".format(i), 'wb') as f:
                f.write(response.content)


start = time.perf_counter()

url_list = []


headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
"Accept-Encoding": "gzip, deflate", 
"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
"Dnt": "1", 
"Host": "httpbin.org", 
"Upgrade-Insecure-Requests": "1", 
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36", 
}

for i in range(1,10001):
    url = "https://www.larvalabs.com/cryptopunks/cryptopunk{}.png".format(i)
    url_list.append(url)


def download(url):
    response = requests.get(url,headers=headers)
    i = url.replace("https://www.larvalabs.com/cryptopunks/cryptopunk","").replace(".png","")
    print(i)
    if response.status_code == 200:
        with open("/Users/mohammadsolaiman/Downloads/CryptoPunk2/cryptopunk{}.png".format(i), 'wb') as f:
            f.write(response.content)
    else:
        print('failed')




with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
    results = {pool.submit(download, url ): url for url in url_list }



finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} seconds(s)')