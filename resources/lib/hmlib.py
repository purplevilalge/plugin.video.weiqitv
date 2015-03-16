# -*- coding: utf-8 -*-
# hmlib.py

from pyquery import PyQuery as pq
from lxml import etree


def get_menu_level_first():
    

    url = 'http://www.weiqitv.com'
    d = pq(url)

    #items = d("div.menu div li a.menu_one")

    return map(lambda x: [d(x).text(), d(x).attr("href")], d("div.menu div li a.menu_one"))
