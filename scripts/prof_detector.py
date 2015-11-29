# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 00:20:45 2015

@author: Andrew

Functions search a text file for profanity and output prafinty warning
"""
import urllib


def read_text(my_file):
    with open(my_file) as f:
        contents = f.read()
        return contents


def check_profanity(my_text):
    '''
    Function excepts a string, queries What Do You Love profanity and returns
    a response.
    '''
    connection = urllib.urlopen('http://www.wdyl.com/profanity?q=' +
                                my_text)
    response = connection.read()
    if "true" in response:
        print("Patrick Swearsy")
    elif "false" in response:
        print("Patrick Swayze")
    else:
        print("A man, a plan, can't scan")

text = read_text('..\data\movie_quotes.txt')
result = check_profanity(text)
