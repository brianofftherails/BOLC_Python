#!/usr/bin/env python3

import re

def q1(sentence):
    '''
    Given a string of multiple words separated by single spaces,
    return a new string with the sentence reversed. The words
    themselves should remain as they are. For example, given
    'it is accepted as a masterpiece on strategy', the returned
    string should be 'strategy on masterpiece a as accepted is it'.
    '''
    return ' '.join(sentence.split(' ')[::-1])

def q2(n):
    '''
    Given a positive integer, return its string representation with
    commas seperating groups of 3 digits. For example, given 65535
    the returned string should be '65,535'.
    '''
    revparsed = list(str(n))[::-1]
    offset = 0
    for k in range(1,len(revparsed)):
        if not k%3:
            revparsed.insert(k+offset,',')
            offset+=1
    return ''.join(revparsed[::-1])
    

def q3(lst0, lst1):
    '''
    Given two lists of integers, return a sorted list that contains
    all integers from both lists in descending order. For example,
    given [3,4,9] and [8,1,5] the returned list should be [9,8,5,4,3,1].
    The returned list may contain duplicates.
    '''
    return sorted(lst0+lst1,reverse=True)

def q4(s1,s2,s3):
    '''
    Given 3 scores in the range [0-100] inclusive, return 'GO' if
    the average score is greater than 50. Otherwise return 'NOGO'.
    '''
    return 'GO' if sum([s1,s2,s3])/3>50 else 'NOGO'

def q5(integer, limit):
    '''
    Given an integer and limit, return a list of even multiples of the
    integer up to and including the limit. For example, if integer==3 and
    limit==30, the returned list should be [0,6,12,18,24,30]. Note, 0 is
    a multiple of any integer except 0 itself.
    '''
    returnedlist = [0]
    for i in range(integer,limit+1):
        if not i%integer and not i%2: #not (i%integer or i%2):
            returnedlist.append(i)
    return returnedlist

def q6(f0, f1):
    '''
    Given two filenames, return a list whose elements consist of line numbers
    for which the two files differ. The first line is considered line 0.
    '''
    try:
        fobj0 = open(f0,'r')
        fobj1 = open(f1,'r')
        difflist = list()
        f0conts = fobj0.readlines()
        f1conts = fobj1.readlines()
        fobj0.close()
        fobj1.close()
        for line in range(0,min(len(f0conts),len(f1conts))):
            if f0conts[line] != f1conts[line]:
                difflist.append(line)
        return difflist
    except OSError as e:
        print(e)

def q7(lst):
    '''
    Return the first duplicate value in the given list.
    For example, if given [5,7,9,1,3,7,9,5], the returned value should
    be 7.
    '''
    seen_before = list()
    for val in lst:
        if val not in seen_before:
            seen_before.append(val)
        else: return val

def q8(strng):
    '''
    Given a sentence as a string with words being separated by a single space,
    return the length of the shortest word.
    '''
    smallest = 99999
    for word in strng.split(' '):
        if len(word)<smallest:
            smallest = len(word)
    return smallest

def q9(strng):
    '''
    Given an alphanumeric string, return the character whose ascii value
    is that of the integer represenation of all of the digits in the string
    concatenated in the order in which they appear. For example, given
    'hell9oworld7', the returned character should be 'a' which has
    the ascii value of 97.
    '''
    return chr(int(''.join(re.findall(r'\d',strng))))

def q10(arr):
    '''
    Given a list of positive integers sorted in ascending order, return
    the first non-consecutive value. If all values are consecutive, return
    None. For example, given [1,2,3,4,6,7], the returned value should be 6. 
    '''
    currentval = arr[0]
    for val in arr:
        if currentval != val:
            return val
        else: currentval += 1
    return arr[-1]
