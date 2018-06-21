#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 14.3
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "find_duplicates" should take a string reprensentation of a
# directory to search, find all the duplicates, and returns a list of complete 
# paths for any duplicates in the form of tuples.
# 
# In a large collection of MP3 files, there may be more than one copy of the 
# same song, stored in different directories or with different file names. The 
# goal of this exercise is to search for duplicates.
# 
# 1. Write a function named "find_duplicates" that takes a string 
# reprensentation of a directory to search, searches that directory and 
# all of its subdirectories, recursively, and returns a list of complete 
# paths for any duplicates in the form of tuples.
# 
# 2. To recognize duplicates, you can use md5sum to compute a "checksum" for 
# each files. If two files have the same checksum, they probably have the same 
# contents.
#

def find_duplicates(directory):
    return

find_duplicates("./mp3")