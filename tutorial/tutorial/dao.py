from tutorial.models import Article, DBSession
from urllib3.exceptions import InsecureRequestWarning

import os
import urllib3


class ArticleDao(object):
    urllib3.disable_warnings(InsecureRequestWarning)

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

            http = urllib3.PoolManager()
            response = http.request('GET', img_url)
            with open(filename, 'wb') as f:
                f.write(response.data)
        except IOError as e:
            print('文件操作失败', e)
