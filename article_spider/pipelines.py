# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from models import Topic, Post, db_connect, create_news_table

class ArticleSpiderPipeline(object):
    def process_item(self, item, spider):
        return item

@contextmanager
def session_scope(Session):
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class ArticleDataBasePipeline(object):
    """保存文章到数据库"""

    def __init__(self):
        engine = db_connect()
        self.Session = sessionmaker(bind=engine)

    def open_spider(self, spider):
        """This method is called when the spider is opened."""
        pass

    def process_item(self, item, spider):
        topic = Topic(title=item["title"].encode("utf-8"),
                    created_at=item["publish_time"].encode("utf-8"))
        post = Post(content=item["body"].encode("utf-8"),
                    created_at=item["publish_time"].encode("utf-8"),
                    topic=topic)
        with session_scope(self.Session) as session:
            session.add(topic)
            session.add(post)

    def close_spider(self, spider):
        pass
