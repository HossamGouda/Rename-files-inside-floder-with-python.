import os

def rename_file():
    #get the file path 
    file_list=os.listdir(r'C:\Users\hosgo\Desktop\New folder')  
    path=os.getcwd() 
    print('current directory is '+path)
    os.chdir(r'C:\Users\hosgo\Desktop\New folder') 
    #renam files
    for file_name in file_list:
        new_name=file_name.strip('0123456789') 
        os.rename(file_name,new_name) 
        print("New file Name " + new_name)
    os.chdir(path)


rename_file() 


