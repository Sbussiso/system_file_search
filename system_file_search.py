import os, subprocess, re
from pathlib import Path


def system_extension_search_tool():

    print('NOTE: This program searches the entire computer for files containing a user specified extension')
    user_input = input("Enter file extension: ")

    #finds all .exe files in local directory
    exe_files = []
    search =['C:\\']
    print(f'gathering {user_input} files.....')
    for i in search:
        for root, dirs, files in os.walk(i):
            for file in files:
                if file.endswith(user_input):
                    exe = os.path.join(root, file)
                    exe_files.append(exe)
    print( str(user_input) + ' files gathered!')



    #separates filepaths into base and tail and puts in dict
    print('sorting .exe files.........')
    headTail_dict = {}
    tail_exe = []
    for files in exe_files:
        head_tail = os.path.split(files)
        head = head_tail[0]
        tail = head_tail[1]
        headTail_dict.update({head : tail})
        tail_exe.append(tail)
        print(headTail_dict[head])
    print(f'{user_input} files sorted!')





    #grabs full file path of what user chooses
    #print(tail_exe)
    user_input = input('enter the name of .exe file: ')
    for i in tail_exe:

        if user_input == i:
            print(f'user selected to open {i}')
            #gather full file path
            print(headTail_dict[i])
            
            
        else:
            continue






system_extension_search_tool()