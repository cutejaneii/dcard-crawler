# encoding=UTF-8
class dcard_article_model:
    def __init__(self):
        self.url=''
        self.title=''
        self.content=''
        self.article_id=0
        self.date=''
        self.image_urls=[]
        self.responses=[]
        self.image_count=0
        self.forum_name=''
        self.forum_alias=''

class dcard_response_model:
    def __init__(self):
        self.content=''
        self.date=''
        self.likeCount=0
        self.image_urls=[]
        self.image_count=0
        self.floor=0
