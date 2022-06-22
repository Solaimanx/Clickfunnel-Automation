import time
import requests



def main():




    for i in range(5306,6001):
        url = "https://www.larvalabs.com/cryptopunks/cryptopunk{}.png".format(i)
        response = requests.get(url)
        if response.status_code == 200:
            with open("/Users/mohammadsolaiman/Downloads/CryptoPunk/Image5k_6k/cryptopunk{}.png".format(i), 'wb') as f:
                f.write(response.content)
        else:
            print('failed')

        print(i,"5-6k")

    for i in range(6001,7001):
        url = "https://www.larvalabs.com/cryptopunks/cryptopunk{}.png".format(i)
        response = requests.get(url)
        if response.status_code == 200:
            with open("/Users/mohammadsolaiman/Downloads/CryptoPunk/Image6k_7k/cryptopunk{}.png".format(i), 'wb') as f:
                f.write(response.content)
        else:
            print('failed')

        print(i,"6-7k")

    for i in range(7001,8001):
        url = "https://www.larvalabs.com/cryptopunks/cryptopunk{}.png".format(i)
        response = requests.get(url)
        if response.status_code == 200:
            with open("/Users/mohammadsolaiman/Downloads/CryptoPunk/Image7k_8k/cryptopunk{}.png".format(i), 'wb') as f:
                f.write(response.content)
        else:
            print('failed')

        print(i,"7k-8k")

    for i in range(8001,9001):
        url = "https://www.larvalabs.com/cryptopunks/cryptopunk{}.png".format(i)
        response = requests.get(url)
        if response.status_code == 200:
            with open("/Users/mohammadsolaiman/Downloads/CryptoPunk/Image8k_9k/cryptopunk{}.png".format(i), 'wb') as f:
                f.write(response.content)
        else:
            print('failed')

        print(i,"8-9k")

    for i in range(9001,10001):
        url = "https://www.larvalabs.com/cryptopunks/cryptopunk{}.png".format(i)
        response = requests.get(url)
        if response.status_code == 200:
            with open("/Users/mohammadsolaiman/Downloads/CryptoPunk/Image9k_10k/cryptopunk{}.png".format(i), 'wb') as f:
                f.write(response.content)
        else:
            print('failed')

        print(i,"9-10k")



for i in range(8001,9001):
    url = "https://www.larvalabs.com/cryptopunks/cryptopunk{}.png".format(i)
    response = requests.get(url)
    if response.status_code == 200:
        with open("/Users/mohammadsolaiman/Downloads/CryptoPunk/Image8k_9k/cryptopunk{}.png".format(i), 'wb') as f:
            f.write(response.content)
    else:
        print('failed')

    print(i,"8-9k")
