#!/usr/bin/python

import string
import sys
import math
from _heapq import heapify
    # math.acos(x) is the arccosine of x.
    # math.sqrt(x) is the square root of x.

# global variables needed for fast parsing
# translation table maps upper case to lower case and punctuation to spaces
translation_table = string.maketrans(string.punctuation+string.uppercase[0:26],
                                     " "*len(string.punctuation)+string.lowercase[0:26])

def extract_words(filename):
    """
    Return a list of words from a file
    """
    try:
        f = open(filename, 'r')
        doc = f.read()
        lines = doc.translate(translation_table)
        return lines.split()
    except IOError:
        print "Error opening or reading input file: ",filename
        sys.exit()

##############################################
## Part a. Count the frequency of each word ##
##############################################
def doc_dist(word_list1, word_list2):
    """
    Returns a float representing the document distance 
    in radians between two files when given the list of
    words from both files
    """
#    #TODO
#    pass
#    
    #Creates a frequency dictionary with the following format:
    #   freq_dict[word] = [freq_word_in_doc1, freq_word_in_doc2]
    
    freq_dict = {}
    
    #Add words and their frequency in doc1 to the frequency dictionary
    for word in word_list1:
        if word not in freq_dict:
            freq_dict[word] = [1.0,0.0]
        else:
            freq_dict[word][0] += 1.0
            
    #Add words and their frequency in doc2 to the frequency dictionary
    for word in word_list2:
        if word not in freq_dict:
            freq_dict[word] = [0.0,1.0]
        else:
            freq_dict[word][1] += 1.0
            
    #Create variables for the magnitudes of each document vector
    doc_1_magnitude = 0.0
    doc_2_magnitude = 0.0
    
    dot_product = 0.0
    
    #Find the square of the magnitude of each document vector and compute the dot product of
    #the two vectors
    for word in freq_dict:
        word_freq = freq_dict[word]
        doc_1_magnitude += doc_1_freq(word_freq)**2
        doc_2_magnitude += doc_2_freq(word_freq)**2
        
        dot_product += doc_1_freq(word_freq)*doc_2_freq(word_freq)
        
    #Square root to get the actual magnitudes
    doc_1_magnitude = math.sqrt(doc_1_magnitude)
    doc_2_magnitude = math.sqrt(doc_2_magnitude)
    
    
    #Divide the dot product by the product of the magnitudes of each vector,
    #and then take the inverse cosine of this quantity to find the angle between
    #each document in radians
    product_of_magnitudes = doc_1_magnitude * doc_2_magnitude
    angle_between = math.acos(dot_product/product_of_magnitudes)
    
    print angle_between
    return angle_between
    

#Takes a two-element list where the fist element is the frequency that a word
#appears in the first document and returns that frequency
def doc_1_freq(word_freq):
    return word_freq[0]

#Takes a two-element list where the second element is the frequency that a word
#appears in the the second document and returns that freqeuency
def doc_2_freq(word_freq):
    return word_freq[1]
##############################################
## Part b. Count the frequency of each pair ##
##############################################
def doc_dist_pairs(word_list1, word_list2):
    """
    Returns a float representing the document distance
    in radians between two files based on unique 
    consecutive pairs of words when given the list of
    words from both files
    """
#     #TODO
#     pass
    
    #This time the keys of the dictionary will be tuples of words in the order that
    #they appear in the document. Creates a dictionary with the following format:
    #    freq_dict[(word1, word2)] = [freq_word_pair_in_doc1, freq_word_pair_in_doc2]
    freq_dict = {}
    
    word_list1_len = len(word_list1)
    word_list2_len = len(word_list2)
    
    #Since we are dealing with pairs of words, we don't want to try to reference
    #an element outside of the range of the list, so rather than having the range
    #going from 0 to the length of the list, we have the list going from 0 to the 
    #length of the list minus 1
    
    #Add the word pairs and their frequency in doc1 to the frequency dict
    for i in range(0,word_list1_len-1):
        word_pair = (word_list1[i], word_list1[i+1])
        if word_pair not in freq_dict:
            freq_dict[word_pair] = [1.0, 0.0]
        else:
            freq_dict[word_pair][0] += 1.0
    
            
    #Add the word pairs and their frequency in doc2 to the frequency dict
    for i in range(0, word_list2_len-1):
        word_pair = (word_list2[i], word_list2[i+1])
        if word_pair not in freq_dict:
            freq_dict[word_pair] = [0.0, 1.0]
        else:
            freq_dict[word_pair][1] += 1.0   

    
    #Create variables for the magnitudes of each document vector
    doc_1_magnitude = 0.0
    doc_2_magnitude = 0.0
    
    dot_product = 0.0
    
    #Find the square of the magnitude of each document vector and compute the dot product of
    #the two vectors
    for word_pair in freq_dict:
        word_freq = freq_dict[word_pair]
        doc_1_magnitude += doc_1_freq(word_freq)**2
        doc_2_magnitude += doc_2_freq(word_freq)**2
        
        dot_product += doc_1_freq(word_freq)*doc_2_freq(word_freq)
        
    #Square root to get the actual magnitudes
    doc_1_magnitude = math.sqrt(doc_1_magnitude)
    doc_2_magnitude = math.sqrt(doc_2_magnitude)
    
    
    #Divide the dot product by the product of the magnitudes of each vector,
    #and then take the inverse cosine of this quantity to find the angle between
    #each document in radians
    product_of_magnitudes = doc_1_magnitude * doc_2_magnitude
    angle_between = math.acos(dot_product/product_of_magnitudes)
    
    print angle_between
    return angle_between
#############################################################
## Part c. Count the frequency of the 50 most common words ##
#############################################################
def doc_dist_50(word_list1, word_list2):
    """
    Returns a float representing the document distance
    in radians between two files based on the 
    50 most common unique words when given the list of
    words from both files
    """
#     #TODO
#     pass

    #The main dictionary that will store words as keys and the frequency that the word
    #appears in each document as a list:
    #    freq_dict[word] = [freq_word_in_doc1, freq_word_in_doc2]
    freq_dict = {}
    
    #Individual dictionaries for storing the words from each document and
    #the corresponding frequency that the word appears in each document
    word_freq1 = {}
    word_freq2 = {}
    
    #I wanted to use tuples, but then I found that I would already have to make
    #new tuples (immutable) and I wouldn't be able to check whether the tuple was
    #already in the list
    
    #Create a dictionary where the keys are the words from doc1 and the values are the
    #corresponding frequencies with which each element appears in doc1
    for word in word_list1:
        if word not in word_freq1.keys():
            word_freq1[word] = 1.0
        else:
            word_freq1[word] += 1.0
            
    #Create a dictionary where the keys are the words from doc2 and the values are the
    #corresponding frequencies with which each element appears in doc2
    for word in word_list2:
        if word not in word_freq2.keys():
            word_freq2[word] = 1.0
        else:
            word_freq2[word] += 1.0
            
    word_freq_tuple_list1 = []
    word_freq_tuple_list2 = []
    
    #Turn the key-value pairs of the dictionary into tuples
    #TODO: figure out if there is a way to avoid the creation of the dictionaries in the
    #first place to save time and effort        
    for word in word_freq1.keys():
        word_and_freq = (word, word_freq1[word])
        if len(word_freq_tuple_list1) == 0:
            word_freq_tuple_list1.append(word_and_freq)
        else:
            add_sorted(word_freq_tuple_list1, word_and_freq, 0)
            
    for word in word_freq2.keys():
        word_and_freq = (word, word_freq2[word])
        if len(word_freq_tuple_list2) == 0:
            word_freq_tuple_list2.append(word_and_freq)
        else:
            add_sorted(word_freq_tuple_list2, word_and_freq, 0)
            
            
    #Now to add the elements from the sorted lists to the dictionary choosing only the
    #first 50 elements of each list
    
    for i in range(0, min(50, len(word_freq_tuple_list1))):
        word_and_freq1 = word_freq_tuple_list1[i]
        
        doc1_word = word_and_freq1[0]
        doc1_word_freq = word_and_freq1[1]
        
        if doc1_word not in freq_dict.keys():
            freq_dict[doc1_word] = [doc1_word_freq, 0.0]
        else:
            freq_dict[doc1_word][0] = doc1_word_freq
            
    for i in range(0, min(50, len(word_freq_tuple_list2))):
        word_and_freq2 = word_freq_tuple_list2[i]
        
        doc2_word = word_and_freq2[0]
        doc2_word_freq = word_and_freq2[1]
        
        if doc2_word not in freq_dict.keys():
            freq_dict[doc2_word] = [0.0, doc2_word_freq]
        else:
            freq_dict[doc2_word][1] = doc2_word_freq
    #Create variables for the magnitudes of each document vector
    doc_1_magnitude = 0.0
    doc_2_magnitude = 0.0
    
    dot_product = 0.0
    
    #Find the square of the magnitude of each document vector and compute the dot product of
    #the two vectors
    for word in freq_dict:
        word_freq = freq_dict[word]
        doc_1_magnitude += doc_1_freq(word_freq)**2
        doc_2_magnitude += doc_2_freq(word_freq)**2
        
        dot_product += doc_1_freq(word_freq)*doc_2_freq(word_freq)
        
    #Square root to get the actual magnitudes
    doc_1_magnitude = math.sqrt(doc_1_magnitude)
    doc_2_magnitude = math.sqrt(doc_2_magnitude)
    
    
    #Divide the dot product by the product of the magnitudes of each vector,
    #and then take the inverse cosine of this quantity to find the angle between
    #each document in radians
    product_of_magnitudes = doc_1_magnitude * doc_2_magnitude
    angle_between = math.acos(dot_product/product_of_magnitudes)
    
    print angle_between
    return angle_between
            
            
#Creating this method to be able to add tuples to a list, sorted in decreasing order
#based on the second element of the tuple. Assumes that there is at least one element in the list
def add_sorted(tuple_list, tup, index):
    #Each element of the list is a tuple
    if tup[1] > tuple_list[index][1]:
        tuple_list.insert(index, tup)
    #Else if adding 1 to the index would take us out of range of the list,
    #just append the tuple to the end of the list
    
    #I chose >= rather than just == because it's possible that an index value larger than the size
    #of the list is inputed into the function
    elif index + 1 >= len(tuple_list):
        tuple_list.append(tup)
    
    #Else if there are still more elements in the list that can be compared, recurse
    else:
        add_sorted(tuple_list, tup, index + 1)
    
    