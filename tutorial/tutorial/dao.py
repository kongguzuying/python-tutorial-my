from tutorial.models import Article, DBSession

import os
import urllib

class ArticleDao(object):

    def add_article(self, item):
        a = Article()
        a.name = item['name']
        a.href = item['link']
        a.title = item['title']

        session = DBSession()
        session.add(a)
        session.commit()
        session.close()

    def save_img(self, img_url, file_name, file_path='images'):
        try:
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            file_suffix = os.path.splitext(img_url)[0]
            filename = '{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
            urllib.urlretrieve(img_url, filename)
        except IOError as e:
            print('文件操作失败', e)