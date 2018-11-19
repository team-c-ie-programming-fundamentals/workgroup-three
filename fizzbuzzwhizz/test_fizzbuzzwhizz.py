# -*- coding: utf-8 -*-

#%%
from fizzbuzzwhizz import fizzbuzzwhiz


def test_fizzbuzzwhiz_returns_fizz():
    values = [ 6, 2358, 9]  
    for case in values :
        assert fizzbuzzwhiz(case) == "Fizz"

def test_fizzbuzzwhiz_returns_buzz():
    values = [10,1000, 50]
    for case in values:
        assert fizzbuzzwhiz(case) == "Buzz"
        
def test_fizzbuzzwhiz_returns_fizzbuzz():
    values = [15,30]
    for case in values:
        assert fizzbuzzwhiz(case) == "FizzBuzz"

def test_fizzbuzzwhiz_returns_num():
    values = [8,16]
    for case in values:
        assert fizzbuzzwhiz(case) == case
        
def test_fizzbuzzwhiz_returns_undefined():
    values = [0]
    for case in values:
        assert fizzbuzzwhiz(case) == "undefined"   

def test_fizzbuzzwhiz_returns_whiz():
    values = [2,11]
    for case in values:
        assert fizzbuzzwhiz(case) == "Whiz"     
        
def test_fizzbuzzwhiz_returns_notvalid():
    values = [-11,-8]
    for case in values:
        assert fizzbuzzwhiz(case) == "Not valid" 
        