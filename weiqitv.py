# -*- coding: utf-8 -*-  
# weiqitv.py  
# 围棋TV的插件脚本
import sys
import xbmcgui  
import xbmcplugin

# Plugin constants 
__addonid__ = "plugin.video.hdpvod"
__addon__ = xbmcaddon.Addon(id=__addonid__)
__cwd__ = __addon__.getAddonInfo('path')
__resource__  = xbmc.translatePath( os.path.join( __cwd__, 'resources/lib' ) )
#__resource__ = "./resources/lib"
sys.path.append (__resource__)

import hmlib 

menus = hmlib.get_menu_level_first()



url_a='http://www.yunsp.com.cn:8080/dispatch/video/get/59651_265_0.ovp'
handle=int(sys.argv[1])  
listitem=xbmcgui.ListItem('WeiqiTV')  
xbmcplugin.addDirectoryItem(handle, url_a, listitem)  

map(lambda menu: xbmcplugin.addDirectoryItem(handle, menu[1], xbmcgui.ListItem(menu[0])))

xbmcplugin.endOfDirectory(handle)  


