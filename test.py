# -*- coding: utf-8 -*-
# test.py

#import xbmcplugin,xbmcgui,subprocess,sys,os,os.path,xbmcaddon

import sys


# Plugin constants 
#__addonid__ = "plugin.video.hdpvod"
#__addon__ = xbmcaddon.Addon(id=__addonid__)
#__cwd__ = __addon__.getAddonInfo('path')
#__resource__  = xbmc.translatePath( os.path.join( __cwd__, 'resources/lib' ) )
__resource__ = "./resources/lib"
sys.path.append (__resource__)

import hmlib 

hmlib.get_menu_level_first()
