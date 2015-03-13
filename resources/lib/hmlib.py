# -*- coding: utf-8 -*-
# hmlib.py

from pyquery import PyQuery as pq
from lxml import etree


def get_menu_level_first():
    

    url = 'http://www.weiqitv.com'
    d = pq(url)

    items = d("div.menu div li a.menu_one")
    

    print 'get_menu_level_first function'
