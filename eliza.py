#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 10:04:41 2018

@author: te
"""
import re

class Rule:
    
    @classmethod
    def change_pronoun(cls, text):
        text = re.sub(' my ', ' your ', text)
        text = re.sub(' I ', ' you ', text)
        return text
    
class SimpleRule(Rule):
    
    def __init__(self, score):
        self.score = score
    
    def respond(self, text):
        return self.change_pronoun(text) + '?'

    def get_score(self, text):
        return 0.1
    

class RepeatPatternRule(Rule):
    
    def __init__(self, input_pattern,
                 output_pattern, score):
        self.input_pattern = input_pattern
        self.output_pattern = output_pattern
        self.score = score
        
    def get_score(self, text):
        if self.should_apply(text):
            return self.score
        return 0
        
    def should_apply(self, text):
        return re.match(self.input_pattern, text)
    
    def respond(self, text):
        text = self.change_pronoun(text)
        return re.sub(self.input_pattern, 
                      self.output_pattern, 
                      text)
        

if __name__ == '__main__':
    print ("What's on your mind?")
    input_text = input()
    
    # Write 3 kinds of rules
    # Rank them 
    # respond
