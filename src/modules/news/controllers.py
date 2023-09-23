from src.main import app
from src.modules.news.dtos import RssReadderDTO
import feedparser
import simplejson
from newspaper import Article
from src.utils.html import clean_and_minify_html
import datetime
import logging
@app.post("/news/rss")
async def rss_reader(url: str):
    try:
        rss_parser = feedparser.parse(url)
        data = simplejson.dumps(dict(rss_parser), ignore_nan=True, default=str)
        return {
            "status": "success",
            "data": simplejson.loads(data)
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


@app.get("/news/article")
async def get_article(url: str):
    try:
        acticle = Article(url, keep_article_html=True)
        # #To download the article
        acticle.download()
        # #To parse the article
        acticle.parse()
        # #To perform natural language processing ie..nlp => keywords
        # acticle.nlp()

        dt = simplejson.dumps(acticle.__dict__, ignore_nan=True, default=str)
        dt_obj = simplejson.loads(dt)
        news_data = {
            "meta_keywords": dt_obj['meta_keywords'],
            'meta_data': dt_obj['meta_data'],
            "title": acticle.title,
            "link": url,
            "description": acticle.meta_description,
            "language": acticle.meta_lang,
            "image_url": acticle.top_image,
            "published_date": str(
                acticle.publish_date) if acticle.publish_date != None else str(datetime.datetime.now()),
            "article_html": clean_and_minify_html(acticle.article_html),
            "text": acticle.text,
            # "keywords": acticle.keywords,
            "summary": dt_obj['summary'],
            "source_url": dt_obj['source_url'],
        }
        return {
            "status": "success",
            "data": news_data
        }
        # return {
        #     "status": "success",
        #     "data": simplejson.loads(dt)
        # }
    except Exception as e:
        logging.error(e)
        return {
            "status": "error",
            "message": str(e)
        }
