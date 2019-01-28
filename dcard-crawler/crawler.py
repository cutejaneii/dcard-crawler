# -*- coding: utf-8 -*-

import requests
import json
import sys
from bs4 import BeautifulSoup
from model import dcard_article_model, dcard_response_model

headers = {'User-Agent':'Mozilla/5.0 (Windows NT10.0; Win64; rv:64.0)', 'charset':'utf-8'}

def get_dcard_article_soup(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def handleImg(mediaMeta):
    img_list=[]
    try:
        if (mediaMeta!=[]):
            mediaMeta2 = [data for data in mediaMeta if 'image' in data['type']]
            for media in mediaMeta2:
                if (media['url'] not in img_list):
                    img_list.append(media['url'])
    except:
        print('handleImg Error')

    return img_list

def get_article_content(board, article_id):
    content=''
    try:
        article_soup = get_dcard_article_soup('https://www.dcard.tw/f/'+ board +'/p/'+str(article_id))

        main_content = article_soup.find('div', {'class':'Post_content_NKEl9d'})

        remove_divs = main_content.find('div', {'class':'Post_topicList_2U8B7-'})

        if (remove_divs is not None):
            for r in remove_divs:
                r.extract()
        content = main_content.text
    except:
        print('get_article_content error')
    return content


def get_response(article_id):
    comments=[]
    try:

        result = []
        load_more=False
        crawl_url='https://www.dcard.tw/_api/posts/'+ str(article_id) +'/comments'
        result = json.loads(requests.get(crawl_url+'?limit=50', headers=headers).text)

        if (len(result)==50):
            load_more=True

        while (load_more==True):
            data = json.loads(requests.get(crawl_url+'?after='+str(len(result)), headers=headers).text)
            result.extend(data)
            if (len(data)<30):
                load_more=False

        for rep in result:
            if (rep['hidden']==False):

                response_model = dcard_response_model()
                response_model.content = rep['content']
                response_model.date = rep['createdAt']
                response_model.likeCount=rep['likeCount']
                if (rep['mediaMeta']!=[]):
                    response_model.image_urls.extend(handleImg(rep['mediaMeta']))
                    response_model.image_count = len(response_model.image_urls)
                comments.append(response_model)
    except:
        print('get_response error')
    return comments


def dcard_crawl(board, is_popular, before_article_id, after_article_id, limit, is_get_response):
    dcard_articles = []
    try:

        articles=[]
        article_id=0

        crawl_url='https://www.dcard.tw/_api/forums/'+ board +'/posts?popular='+ is_popular +'&limit='+str(limit)

        if (is_popular=='false'):
            if (before_article_id>0):
                crawl_url+='&before='+str(before_article_id)

            if (after_article_id>0):
                crawl_url+='&after='+str(after_article_id)

        result = requests.get(crawl_url, headers=headers)
        articles = json.loads(result.text)

        for article in articles:
            if (article_id==0):
                article_id=article['id']

            article_model = dcard_article_model()
            article_model.forum_name = article['forumName']
            article_model.article_id = article['id']
            article_model.title = article['title']
            article_model.content = get_article_content(board, article['id'])
            article_model.url = 'https://www.dcard.tw/f/' + board + '/p/'+str(article['id'])
            article_model.date = article['createdAt']
            article_model.image_urls.extend(handleImg(article['mediaMeta']))
            article_model.image_count = len(article_model.image_urls)
            if (is_get_response==1):
                article_model.responses.extend(get_response(article['id']))
            dcard_articles.append(article_model)


    except Exception as e1:
        print(str(e1))

    return article_id, dcard_articles
