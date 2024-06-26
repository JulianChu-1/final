import datetime
from typing import List
from pydantic import BaseModel

class Weibo(BaseModel):
    # _id : str
    # user_id : str
    id : str
    screen_name : str
    text : str
    created_at : str
    topics : str
    category : str
    # spider_time : str = None
    # bid : str
    # article_url : str
    # pics : str
    # video_url : str
    # location : str
    # source : str
    # attitudes_count : str
    # comments_count : str
    # reposts_count: str
    # at_users : str
    # full_created_at : str

class WeiboUser(BaseModel):
    id : str

class User(BaseModel):
    id : str
    username : str
    nickname : str
    password : str
    sex : str
    status : str
    role : str
    created_at: str = None
    spider_time: str = None

class UserLogin(BaseModel):
    username : str
    password : str

class WeiboSpider(BaseModel):
    user_id_list : str
    since_date : int
    start_page : int
    cookie : str = None
    

    