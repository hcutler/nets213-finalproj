import string
import sys
import csv
import operator
from operator import itemgetter
from numpy import *
# from itertools import islice

#This script takes input in form of answers/rankings associated with them. For each answer to a question, compute average rating score
#assuming input is like X (Answers / rankings associated with them - take averages and output stuff associated with them)

def aggregate(file):
    #create dictionary from data. keys will be usernames, values are questions asked by that user
    questions = {}
    for row in csv.DictReader(open(file)) :
        #get username and question field from data
        user = row['username']
        question = row['question']

        #append usernames and questions to dictionary
        average_rating = 0
        questions = {user : {question : average_rating}}
        #remove duplicate entries
        unique_q = []
        if questions not in unique_q:
            unique_q.append(questions)
        #print unique_q

        a1 = row['answer_1']
        a2 = row['answer_2']
        a3 = row['answer_3']
        a4 = row['answer_4']
        a5 = row['answer_5']

        a1_avg_rank = 0

        a1_rank = (row['answer_1_rank'])  #every fifth
        l = len(a1_rank)
        a1_rank_int = (int)(a1_rank)

        a = array(a1_rank_int)
        print a1_rank_int(range(0, len(a), 5))
        # for i in a1_rank(range(0, len(a1_rank), 5)):
        #     print i
            # a1_avg_rank += i
            # print a1_avg_rank




        a2_rank = row['answer_2_rank']
        a3_rank = row['answer_3_rank']
        a4_rank = row['answer_4_rank']
        a5_rank = row['answer_5_rank']









#compute average


#def quality_control(aggregated_list):
    #return top three answers for a question in form of {question : answer1, answer2, answer 3}

if __name__ == '__main__' :
    aggregate("rawdata.csv")








#########
#
# data = [line.strip().split('\t') for line in open("read.csv").readlines()]
# print data

# def get_data(filename):
#   data = [line.strip().split('\t') for line in open(filename).readlines()]
#
#
# if __name__ == '__main__' :
#   #raw_data = get_data(sys.argv[1])
#     raw_data = get_data("read.csv")
#     print raw_data
