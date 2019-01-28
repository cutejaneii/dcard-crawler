# -*- coding: utf-8 -*-
from crawler import dcard_crawl
from argparse import ArgumentParser

if __name__ ==  '__main__':
    parser = ArgumentParser()
    parser.add_argument('-o', '--output', help='output document name')
    parser.add_argument('-f', '--forum', default='trending', help='Dcard forum name (default: trending)')
    parser.add_argument('-a', '--article_id', type=int, default=160000, help='Article id (default: 160000)')
    parser.add_argument('-m', '--mode', type=int, default=0, help='Query mode (default:0)  0:Most popular articles, 1:Get NEWER articles, 2:get OLDER articles ')
    parser.add_argument('-c', '--count', type=int, default=10, help='Article count')
    parser.add_argument('-r', '--get_responses', type=int, default=0, help='Get response (default:0)  0:No responses, 1:With response')

    args = parser.parse_args()
    if args.output:
        print('output document name='+ args.output)

    data=[]
    article_id=0

    check=True

    if (args.mode not in [0, 1, 2]):
        print('[mode] can only be 0, 1, 2.')
        check=False

    if (args.get_responses not in [0, 1]):
        print('[get_responses] can only be 0, 1, 2.')


    if (check==True):
        if (args.mode in [0, 1, 2]):
            if (args.mode==0):
                article_id, data = dcard_crawl(args.forum, 'true', 1, 1, args.count, args.get_responses)
            else:
                if (args.mode==1):
                    article_id, data = dcard_crawl(args.forum, 'false', 1, args.article_id, args.count, args.get_responses)
                else:
                    article_id, data = dcard_crawl(args.forum, 'false', args.article_id, 1, args.count, args.get_responses)

        for item in data:
            print('--------------------------------------------------')
            print('['+ str(item.article_id) +'] '+item.title)
            if (args.get_responses==1):
                print('-----------------RESPONSES-----------------------')
                for r in item.responses:
                    print(r.content+'\n')
