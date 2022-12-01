#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
# open the text file:
f = open('relativity.txt')
# read the file and create a list of words (google split function in python):

##the split function converts a string into a list

words = f.read().split()
f.close() #this converts the relativity text file into a list and saves the list under the varaiable named words
# calculate how many time each word is repeated (using dictionary):
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1 #this makes a dictionary of all the words in the text file as the keys and the number of times they appear in the file as the values

# create a list of all words:
word_list = list(word_counts.keys()) #this convers the keys in the dictionary into a list

# sort the list of all words based on how many times they are repeated:
def dict_val(x):
    return word_counts[x] #this returns the value for the argument x
word_list.sort(key = dict_val, reverse = True) #this sorts the list by the values and puts the keys with the largest values first
# print the top 10 most frequently used words:
print("List of top 10 most frequently used words: ")
print(word_list[ : 10])
###this doesn't provide much information about the text because all of these are stop words


###second attempt###
#contents = open('relativity.txt').read()
#translation_table = {ord(ch) : None  for ch in string.punctuation}
#contents = contents.translate(translation_table)
#words = contents.split()

# create a list of all words in lower case:
lowercase_words = [word.lower() for word in words] #this makes a list of all the lowecase words int he file
# open the file containing all of the stop words in English language:
f = open('stopWords.txt') #this opens a new file
# read the file create the list of all stop words in English language:
stop_words = f.read().split() #this converts the stopwords file into a list


###remove stop words###
# create the list of non stop words by filtering out the stop words:
non_stop_words = [word for word in lowercase_words if word not in stop_words] #this creates a new list that is only the lowercase words in the relativity file that are not also in the stop words file
# now calculate the frequency of the non stop words:
word_counts = {}
for word in non_stop_words:
    word_counts[word] = word_counts.get(word, 0) + 1 #this clreates a dictionary with the words in the non_stop_words list as the keys and the frequency with which they show up as the values

word_list = list(word_counts.keys()) #this makes a list of all the words in the dictionary
# sort the words again:
word_list.sort(key = dict_val, reverse = True) #this sorts the keys in the list by their values with the highest values being first
# prin the top 10 most frequently used words:
print("\nList of top 10 most frequently used non stop words: ")
print(word_list[ : 10])
