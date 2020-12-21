# AUTHOR'S NOTE: PLEASE DOWNLOAD THE MET DATA TO RUN THIS FILE.
# THE MET DATA IS NOT INCLUDED IN THE PROJECT DUE TO COPYRIGHT.
# YOU CAN DOWNLOAD THE DATA HERE:
# https://github.com/metmuseum/openaccess


# importing csv module
import csv
#
from collections import defaultdict

filename = "Met_Objects_list.csv"

# initializing the titles and rows list
fields = []
rows = []
artObj = []
ID_obj = []
Male_ID_obj = []
Male_Obj = []
FemObj = []
FemIDs = []
FemCount = []

wrong_date = []

Fem_centuries = defaultdict(list)
Male_centuries = defaultdict(list)
# Fem_centuries = {}
beginDate_Column = 30
endDate_Column = 29

with open(filename, 'r') as csvfile:
    # creating a csv reader object
    reader = csv.reader(csvfile)
    header = reader.__next__()
    for x in reader:
        if x[25] != 'Female':
            # begin date
            Male_Obj.append((x[30]))
            array_length = len(x[25])
            print("m length is", array_length)
            # if x[beginDate_Column].isdigit() == True:
            #     Male_Obj.append((x[beginDate_Column]))
            #
            #
            # elif x[29].isdigit():
            #     # add end date
            #     Male_Obj.append((x[29]))
            #
            # else:
            #     wrong_date.append((x[beginDate_Column]))
            #     wrong_date.append((x[29]))
        if x[25] == 'Female':
            FemObj.append((x[30]))
            fem_array_length = len(x[25])
            print("fem length is", fem_array_length)
            # begin date
            # if x[30].isdigit():
            #     FemObj.append((x[30]))
            #
            # elif x[29].isdigit():
            #     # add end date
            #     FemObj.append((x[29]))
            # else:
            #     wrong_date.append((x[beginDate_Column]))
            #     wrong_date.append((x[29]))
        # if x[25]:
        #     all_array_length = len(x[25])
        #     print("length is", all_array_length)

        else:
            continue
print("test thr 1")
print(fem_array_length+array_length, all_array_length)
# with open(filename, 'r') as csvfile:
#     # creating a csv reader object
#     reader = csv.reader(csvfile)
#     # header
#     header = reader.__next__()
#     for x in reader:
#         if x[25] == 'Female':
#             # begin date
#             if x[30].isdigit():
#                 FemObj.append((x[30]))
#
#             elif x[29].isdigit():
#                 # add end date
#                 FemObj.append((x[29]))
#             else:
#                 wrong_date.append((x[beginDate_Column]))
#                 wrong_date.append((x[29]))
#         else:
#             continue
#
# #
# # for all objects in femobj add to dict
# print(wrong_date)
# # for object in FemObj:
# #     century = int(object) // 100
# #
# #     # if 20 > century > 1:
# #     #     print(object)
# #     Fem_centuries[century].append(object)
# #
# # # for all objects inemobj  add to dict
# # for object in Male_Obj:
# #     male_century = int(object) // 100
# #     # x[4] is object ID >> give me
# #     #
# #     # if 10 > male_century > -1:
# #     #     print(object)
# #     Male_centuries[male_century].append(object)
# #
# # print("test 3")
# # key_file = open("fem_century.txt", 'w')
# # value_file = open("value_fem_century.txt", 'w')
# # male_file = open("m_century.txt", 'w')
# # male_value_file = open("value_m_century.txt", 'w')
# # # print(list(Fem_centuries.keys()))
# #
# # for key, value in Fem_centuries.items():
# #     # print(key, len(value))
# #     print(key, ",", file=key_file)
# #     print(len(value), ",", file=value_file)
# #     # open("fem_century", 'w')
# # for key, value in Male_centuries.items():
# #     # print(key, len(value))
# #     # print(key, ",", len(value), file=male_file)
# #     print(key, ",", file=male_file)
# #     print(len(value), ",", file=male_value_file)
# #     open("m_century.txt", 'w')
# # print("test4")
# # for object in Male_Obj:
# #     if 200 > int(object) > 0:
# #         print(object)
# # # for value in Fem_centuries [-12]:
# # #     print(value)
# #
# # # csv writer vs dict writer
# #
# # use grep to match?