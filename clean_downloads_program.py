import os
import shutil


extentions_dict = {
    "winrar_extentions" : (".zip", ".rar"),
    "document_extentions" : (".pdf", ".docx", ".doc", ".txt"),
    "audio_extentions" : (".mp3") ,
    "ppt_extentions" : (".ppt", ".pptx"),
    "image_extentions" : (".eps", ".png", ".gif", ".jpg", ".jpeg", ".ai", ".raw", ".cr2", ".nef", ".orf", ".sr2"),
    "video_extentions" : (".mp4", ".mkv"),
    }



path = input("Please enter the folder path you want to organise and clean: ")


def extract_in_list(folder_path, file_extentions):
    files_list = []
    for file in os.listdir(folder_path):
        for extention in file_extentions:
            if file.endswith(extention):
                files_list.append(file)
    return files_list


for type_extentions, type_tuple in extentions_dict.items():
    files_list = extract_in_list(path, type_tuple)

    # print(files_list)
    # print()

    directory_name = type_extentions.split("_")[0] + " " + "files"
    directory_path = os.path.join(path, directory_name)

    if len(files_list):
        if os.path.exists(directory_path) == False:
            os.mkdir(directory_path)

        for file in files_list:
            old_path = os.path.join(path, file)
            new_path = os.path.join(directory_path, file)

            shutil.move(old_path, new_path)


print("Program execution successfull")
print("Check your folder for organised files")



        



        

 
# for type_extention, type_tuple in extentions_dict.items():
#     for extention in type_tuple:
#         for file in os.listdir(path):
#             if file.endswith(extention):

#                 directory = type_extention.split("_")[0] + " " + "files"
#                 directory_path = os.path.join(path, directory)
#                 if os.path.exists(directory_path) == False:
#                     os.mkdir(directory_path)
                
#                 old_path = os.path.join(path, file)
#                 new_path = os.path.join(directory_path, file)

#                 shutil.move(old_path, new_path)







        
# image_list = extract_in_list(path, extentions_dict["image_extentions"])
# image_folder_path = os.path.join(path, "Images")
# if os.path.exists(image_folder_path) == False:
#     os.mkdir(image_folder_path)
# for image in image_list:
#     old_path = os.path.join(path, image)
#     new_path = os.path.join(image_folder_path, image)

#     shutil.move(old_path, new_path)








# print(extract_in_list(path, image_extentions))
#     # print(files_list)

# for file in os.listdir(path):
#     if file.endswith() in 