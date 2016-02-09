#!/usr/bin/python

import string
import sys
import math
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
    
    #Find the magnitudes of each document vector and compute their dot product
    for word in freq_dict:
        word_freq = freq_dict[word]
        doc_1_magnitude += doc_1_freq(word_freq)**2
        doc_2_magnitude += doc_2_freq(word_freq)**2
        
        dot_product += doc_1_freq(word_freq)*doc_2_freq(word_freq)
        
    #Divide the dot product by the product of the magnitudes of each vector,
    #and then take the inverse cosine of this quantity to find the angle between
    #each document in radians
    product_of_magnitudes = doc_1_magnitude * doc_2_magnitude
    angle_between = math.acos(dot_product/product_of_magnitudes)
    
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
    #TODO
    pass

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
    #TODO
    pass