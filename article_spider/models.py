#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 定义数据库模型实体
Desc :
"""
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from settings import DATABASE

Base = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**DATABASE))


def create_news_table(engine):
    """"""
    Base.metadata.create_all(engine)

class ArticleRule(Base):
    """自定义文章爬取规则"""
    __tablename__ = 'article_rule'

    id = Column(Integer, primary_key=True)
    # 规则名称
    name = Column(String(30))
    # 运行的域名列表，逗号隔开
    allow_domains = Column(String(100))
    # 开始URL列表，逗号隔开
    start_urls = Column(String(100))
    # 下一页的xpath
    next_page = Column(String(100))
    # 文章链接正则表达式(子串)
    allow_url = Column(String(200))
    # 文章链接提取区域xpath
    extract_from = Column(String(200))
    # 文章标题xpath
    title_xpath = Column(String(100))
    # 文章内容xpath
    body_xpath = Column(Text)
    # 发布时间xpath
    publish_time_xpath = Column(String(100))
    # 文章来源
    source_site = Column(String(30))
    # 规则是否生效
    enable = Column(Integer)


class Topic(Base):
    """主题"""
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    author = Column(String(255))
    created_at = Column(String(50))
    posts = relationship("Post", backref="topic")

class Post(Base):
    """帖子内容"""
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, ForeignKey('topics.id'))
    author = Column(String(255))
    content = Column(Text)
    created_at = Column(String(50))
