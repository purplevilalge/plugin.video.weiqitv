# -*- coding: utf-8 -*-  
# weiqitv.py  
# 围棋TV的插件脚本
import sys
import xbmcgui  
import xbmcplugin

url_a='http://www.yunsp.com.cn:8080/dispatch/video/get/59651_265_0.ovp'
handle=int(sys.argv[1])  
listitem=xbmcgui.ListItem('WeiqiTV')  
xbmcplugin.addDirectoryItem(handle, url_a, listitem)  
xbmcplugin.endOfDirectory(handle)  
