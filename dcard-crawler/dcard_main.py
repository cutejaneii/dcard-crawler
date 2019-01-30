# -*- coding: utf-8 -*-
from test import dcard_crawl, dcard_crawl_by_keyword
from argparse import ArgumentParser
import datetime

if __name__ ==  '__main__':
    parser = ArgumentParser()
    parser.add_argument('-o', '--output', help='output document name')
    parser.add_argument('-f', '--forum', default='trending', help='Dcard forum name (default: trending)')
    parser.add_argument('-a', '--article_id', type=int, default=1, help='Article id (default: 1)')
    parser.add_argument('-m', '--mode', type=int, default=0, help='Query mode (default:0)  0:Most popular articles, 1:Get NEWER articles, 2:get OLDER articles, 3:get articles by KEYWORD ')
    parser.add_argument('-c', '--count', type=int, default=10, help='Article count (default: 10)')
    parser.add_argument('-r', '--get_responses', type=int, default=0, help='Get response (default:0)  0:No responses, 1:With response')
    parser.add_argument('-k', '--keyword', default='pizza', help='Keyword')
    args = parser.parse_args()
    if args.output:
        print('output document name='+ args.output)

    data=[]

    check=True

    if (args.mode not in [0, 1, 2, 3]):
        print('[mode] can only be 0, 1, 2, 3')
        check=False

    if (args.get_responses not in [0, 1]):
        print('[get_responses] can only be 0, 1.')
        check=False


    if (args.count == 0):
        print('[count] should bigger than 0.')
        check=False

    k = str(datetime.datetime.now())

    if (check==True):
        if (args.mode in [0, 1, 2, 3]):
            if (args.mode==0):
                data = dcard_crawl(args.forum, 'true', 1, 1, args.count, args.get_responses)
            else:
                if (args.mode==1):
                    data = dcard_crawl(args.forum, 'false', 1, args.article_id, args.count, args.get_responses)
                elif (args.mode==2):
                    data = dcard_crawl(args.forum, 'false', args.article_id, 1, args.count, args.get_responses)
                else:
                    data = dcard_crawl_by_keyword(args.keyword, args.count, args.get_responses)

        for item in data:
            print('['+ str(item.article_id) +'] '+item.title)
            if (args.get_responses==1):
                print('-----------------RESPONSES-----------------------')
                for r in item.responses:
                    print(str(r.floor) + 'F: ' +r.content+'\n')
