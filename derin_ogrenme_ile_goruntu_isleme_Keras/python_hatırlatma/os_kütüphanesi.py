import os 

#işletim sistemi ismi
print(os.name)

#bulunduğumuz klasörü gösterir
currentDir = os.getcwd()
print(currentDir)

#new folder
foldername = "new_folder"
os.mkdir(foldername)

new_folder_name = "new_folder_2"
os.rename(foldername, new_folder_name)

os.dir(currentDir+"\\"+new_folder_name)
print(os.getcwd)

os.dir(currentDir)
print(os.getcwd)

#dosyaları listeler
files = os.listdir() 

for f in files:
    if f.endswith(".py"):
        print(f)

os.rmdir(new_folder_name) #remove



