# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 01:33:16 2018

@author: natch
"""
import re

import os.path
from collections import Counter
save_path = 'C:/Users/natch/Desktop/SNproject/documents-nsc'
all_files = os.listdir(save_path)


article_file = open ('article_list.txt','w',encoding='utf-8')
file = open ('all_article.txt','r',encoding='utf-8')
raw_text = file.read()
article_list = re.findall('([ก-ํ]+)',raw_text)
article_id = re.findall('\'([0-9]+)\',\s\'[ก-ํ]+\'',raw_text)
stop_words = ['คือ','ของ','อะไร']
'''
for item in article_list :
    article_file.write(item + '\n')
article_file.close()
'''
print (article_id[:10])
print ( 'เฮโจเกียว' in article_list)


_article = {}


def find_article(question):
    prop_article_list = []
    for article in article_list:
        if article in question:
            prop_article_list.append(article)
    #for word in prop_article_list:
        
    
    return prop_article_list

print (find_article('เฮโจเกียวคือเมืองหลวงของประเทศอะไร'))
#วิธีสร้างคำให้ดุว่ามันเป้นคำทั่วไป ปรากฏบ่อย ใช้บ่อย ไม่สำคัญ 

def count_freq_word(doc,article):
    '''
    (str,str) => int
    นับความถี่ของคำ(article) ในไฟล์เอกสาร doc
    param:
        doc = file name
        article = word
    '''
    file = open(doc,'r',encoding ='utf-8')
    raw_text = file.read()
    file.close()
    return len (re.findall( '('+str(article)+')',raw_text))

def freq_article(all_doc , article_list):
    '''
    param:
        all_doc : list of file_name
        article_list : list of article
    '''
    print ('in freq_article')
    print (len(all_doc))
    n_file = 0
    freq = Counter()
    for doc in all_doc:
        print (n_file)
        n_file+=1
        completeName = save_path +"/"+doc+'.txt'
        for article in article_list:
            freq[article]+= count_freq_word(completeName,article)
        f = open('get_freq_word.txt','w',encoding = 'utf-8').write(str(freq))
    
    return freq

minimize_article_list = [item for item in article_list if len(item) >= 2]
print ('will do')
print (len(minimize_article))
get_freq_word = freq_article(article_id,minimize_article_list)
freq_file = open('freq_article_50.txt','x',encoding = 'utf-8')
freq_file.write(get_freq_word)
print (get_freq_word)
    