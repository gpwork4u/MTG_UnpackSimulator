import requests
from bs4 import BeautifulSoup
import numpy as np
import random
import argparse
import matplotlib.pyplot as plt
import sys


def get_pack(card_list):
    if random.randint(0, 6) < 5:
        rare_slot = list(np.random.choice(card_list['Rare'], 1))
    else:
        rare_slot = list(np.random.choice(card_list['Mythic'], 1))

    uncommon_slot = list(np.random.choice(card_list['Uncommon'], 3))
    common_slot = list(np.random.choice(card_list['Common'], 10))
    return rare_slot + uncommon_slot + common_slot


def download_card_list(version):
    url = 'https://www.mtggoldfish.com/index/%s#paper' % version
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    table = soup.find('div', 'table-responsive mt-3').find('tbody')
    card_list = {'Mythic': [], 'Rare': [], 'Uncommon': [], 'Common': []}
    price_table = {}
    for tr in table.findAll('tr'):
        td = tr.findAll('td')
        name = td[0].text
        rare = td[2].text
        price = float(td[3].text.strip('\n'))
        if price < 5:
            price = 0
        try:
            card_list[rare].append((name))
            price_table[name] = price
        except:
            pass
    return card_list, price_table


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', required=True,
                        type=str, help='Version of pack')
    parser.add_argument('-t', '--times', required=True,
                        type=int, help='times for simulates')
    parser.add_argument('-n', '--pack_num', type=int, default=36,
                        help='packs number in each box, default is 36')
    args = parser.parse_args()

    card_list, price_table = download_card_list(args.version)
    total_price_list = []
    for i in range(args.times):
        total_price = 0
        for i in range(args.pack_num):
            pack = get_pack(card_list)
            card_price = [price_table[card] for card in pack]
            total_price += sum(card_price)
        total_price_list.append((total_price))
    plt.hist(total_price_list, bins=10)
    plt.show()
