#!/usr/bin/python
# -*- coding: utf8 -*-
'''
----- STYLE -----------------
1 = BOLD
3 = ITALIC
4 = UNDER_LINE
8 = HIDDEN
----- FRONT GROUND COLOR ----
31 = RED
91 = LIGHT_RED
32 = GREEN
92 = LIGHT_GREEN
33 = YELLOW
93 = LIGHT_YELLOW
34 = BLUE
94 = LIGHT_BLUE
35 = PURPLE
95 = LIGHT_PURPLE
36 = TIFFANY_BLUE
96 = LIGHT_TIFFANY_BLUE
2 = LIGHT_GREY
90 = DARK_GREY
30 = BLACK
----- BACK GROUND COLOR -----
107 = BG_LIGHT_WHITE
47 = BG_WHITE
7 = BG_GREY
100 = BG_DARK_GREY
40 = BG_BLACK
41 = BG_RED
101 = BG_LIGHT_RED
42 = BG_GREEN
102 = BG_LIGHT_GREEN
43 = BG_YELLOW
103 = BG_LIGHT_YELLOW
44 = BG_BLUE
104 = BG_LIGHT_BLUE
45 = BG_PURPLE
105 = BG_LIGHT_PURPLE
46 = BG_TIFFANY_BLUE
106 = BG_LIGHT_TIFFANY_BLUE
'''
import os, sys
END = '\033[0m'
class __Style:
    BOLD = '\033[{}m'.format(1) ; ITALIC = '\033[{}m'.format(3) ; UNDER_LINE = '\033[{}m'.format(4) ; HIDDEN = '\033[{}m'.format(8)
    table = [BOLD,ITALIC,UNDER_LINE,HIDDEN]
    def TestingPrintOut(self):
        table = {1:"BOLD" , 3:"ITALIC" , 4:"UNDER LINE" , 8:"HIDDEN"}
        print '-------------- STYLE -----------------'
        for i in table.keys():
            print '{} -> {} -> \033[{}m{}{}'.format('\\033[{}m'.format(i) , table[i], i,'HELLO WORLD',END)
        print '--------------------------------------\n'
class __LOG_COLOR:
    RED = '\033[{}m'.format(31) ; LIGHT_RED = '\033[{}m'.format(91) ; GREEN = '\033[{}m'.format(32) ; LIGHT_GREEN = '\033[{}m'.format(92) ; YELLOW = '\033[{}m'.format(33)
    LIGHT_YELLOW = '\033[{}m'.format(93) ; BLUE = '\033[{}m'.format(34) ; LIGHT_BLUE = '\033[{}m'.format(94) ; PURPLE = '\033[{}m'.format(35); LIGHT_PURPLE = '\033[{}m'.format(95)
    TIFFANY_BLUE = '\033[{}m'.format(36) ; LIGHT_TIFFANY_BLUE = '\033[{}m'.format(96) ; LIGHT_GREY = '\033[{}m'.format(2) ; DARK_GREY = '\033[{}m'.format(90) ; BLACK = '\033[{}m'.format(30)
    table = [RED,LIGHT_RED,GREEN,LIGHT_GREEN,YELLOW,LIGHT_YELLOW,BLUE,LIGHT_BLUE,PURPLE,LIGHT_PURPLE,TIFFANY_BLUE,LIGHT_TIFFANY_BLUE,LIGHT_GREY,DARK_GREY,BLACK]
    def TestingPrintOut(self):
        table = {31:"RED", 91:"LIGHT RED", 32:"GREEN", 92:"LIGHT GREEN",  33:"YELLOW", 93:"LIGHT YELLOW",  34:"BLUE", 
        94:"LIGHT BLUE", 35:"PURPLE", 95:"LIGHT PURPLE", 36:"TIFFANY BLUE", 96:"LIGHT TIFFANY BLUE", 2:"LIGHT GREY", 90:"DARK GREY", 30:"BLACK" }
        print '-------------- LOG COLOR -----------------'
        for i in [31,91,32,92,33,93,34,94,35,95,36,96,2,90,30]:
            print '{} -> {} -> \033[{}m{}{}'.format('\\033[{}m'.format(i) , table[i], i,'HELLO WORLD',END)
        print '-----------------------------------------------------\n'
class __BG_Color:
    BG_LIGHT_WHITE = '\033[{}m'.format(107); BG_WHITE = '\033[{}m'.format(47) ;BG_GREY = '\033[{}m'.format(7) ;BG_DARK_GREY = '\033[{}m'.format(100)  ;BG_BLACK = '\033[{}m'.format(40)
    BG_RED = '\033[{}m'.format(41) ;BG_LIGHT_RED = '\033[{}m'.format(101) ;BG_GREEN = '\033[{}m'.format(42) ;BG_LIGHT_GREEN = '\033[{}m'.format(102); BG_YELLOW = '\033[{}m'.format(43)
    BG_LIGHT_YELLOW = '\033[{}m'.format(103) ;BG_BLUE = '\033[{}m'.format(44) ;BG_LIGHT_BLUE = '\033[{}m'.format(104) ;BG_PURPLE = '\033[{}m'.format(45) ;BG_LIGHT_PURPLE = '\033[{}m'.format(105)
    BG_TIFFANY_BLUE = '\033[{}m'.format(46) ;BG_LIGHT_TIFFANY_BLUE ='\033[{}m'.format(106)
    table = [BG_LIGHT_WHITE,BG_WHITE,BG_GREY,BG_DARK_GREY,BG_BLACK,BG_RED,BG_LIGHT_RED,BG_GREEN,BG_LIGHT_GREEN,BG_YELLOW,BG_LIGHT_YELLOW,BG_BLUE,BG_LIGHT_BLUE,BG_PURPLE,BG_LIGHT_PURPLE,BG_TIFFANY_BLUE,BG_LIGHT_TIFFANY_BLUE]
    def TestingPrintOut(self):
        table = {107:"BG LIGHT WHITE", 47:"BG WHITE", 7:"BG GREY", 100:"BG DARK GREY", 40:"BG BLACK", 41:"BG RED", 101:"BG LIGHT RED", 42:"BG GREEN", 102:"BG LIGHT GREEN",
        43:"BG YELLOW", 103:"BG LIGHT YELLOW",44:"BG BLUE", 104:"BG LIGHT BLUE", 45:"BG PURPLE", 105:"BG LIGHT PURPLE", 46:"BG TIFFANY BLUE", 106:"BG LIGHT TIFFANY BLUE"}
        print '-------------- FRONT GROUND COLOR -----------------'
        for i in [107,47,7,100,40,41,101,42,102,43,103,44,104,45,105,46,106]:
            print '{} -> {} -> \033[{}m{}{}'.format('\\033[{}m'.format(i) , table[i], i,'HELLO WORLD',END)
        print '-----------------------------------------------------\n'

# Init Class
LOG_COLOR = __LOG_COLOR()
STYLE = __Style()
BG_COLOR = __BG_Color()

# Functions
def HELP():
    STYLE.TestingPrintOut()
    LOG_COLOR.TestingPrintOut()
    BG_COLOR.TestingPrintOut()
# Example Call
# HELP()

def Log_Print(print_out, style = None, log_color = None, bg_color = None):
    style_code = ""; log_color_code = ""; bg_color_code = ""
    if style != None    and style != STYLE.table: style_code = style
    if log_color != None and log_color != LOG_COLOR.table: log_color_code = log_color
    if bg_color != None and bg_color != BG_COLOR.table: bg_color_code = bg_color
    print('{}{}{}{}{}'.format(style_code, log_color_code, bg_color_code, print_out, END))
def Log_Get(print_out, style = None, log_color = None, bg_color = None):
    style_code = ""; log_color_code = ""; bg_color_code = ""
    if style != None    and style != STYLE.table: style_code = style
    if log_color != None and log_color != LOG_COLOR.table: log_color_code = log_color
    if bg_color != None and bg_color != BG_COLOR.table: bg_color_code = bg_color
    return ('{}{}{}{}{}'.format(style_code, log_color_code, bg_color_code, print_out, END))


# Example Call  
# Log_Print('Hello World', style = STYLE.ITALIC, log_color = LOG_COLOR.BLACK, bg_color = BG_COLOR.BG_GREEN)
