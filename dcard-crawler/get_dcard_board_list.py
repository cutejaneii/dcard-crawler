# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from argparse import ArgumentParser

def get_board_list(is_school):
    boards=[]
    crawl_url='https://www.dcard.tw/f'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT10.0; Win64; rv:64.0)', 'charset':'utf-8'}
    response = requests.get(crawl_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    boardinfo = soup.select('ul.ForumEntryGroup_list_cdSR2f')
    try:
        boards=boardinfo[is_school].findAll('a')
    except Exception as exp:
        print(str(exp))
    return boards



if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-s', '--is_school_forum', type=int, default=0, help='get school forum, 0:get category forum, 1:get school forum')
    args = parser.parse_args()
    if (args.is_school_forum not in [0, 1]):
        print('[is_school_forum] can only be 0, 1')
    else:
        boards=[]
        boards = get_board_list(args.is_school_forum)
        for b in boards:
            print(b.text + ' -> ' + b['href'])
