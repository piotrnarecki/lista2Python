def rename_files(folder_path, suffix):
    import os
    try:
        from os import listdir
        from os.path import isfile, join
        files_list = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]

        if len(files_list) > 0:
            for i in range(0, len(files_list)):
                file_name = files_list[i].split('.')[0]
                file_type = files_list[i].split('.')[1]

                file = folder_path + "/" + file_name + "." + file_type

                new_file_name = file_name + "_" + suffix
                new_file = folder_path + "/" + new_file_name + "." + file_type

                print (new_file)

                os.rename(file, new_file)
        else:
            print ("this folder is empty")

    except OSError:
        print "incorrect path"


def main():
    import sys
    import os
    from datetime import datetime

    # folder_path = "/Users/piotrnarecki/Desktop/test_folder"
    # suffix = ""

    if len(sys.argv) == 3:

        folder_path = sys.argv[1]
        suffix = sys.argv[2]
        rename_files(folder_path, suffix)

    elif len(sys.argv) == 2:
        folder_path = sys.argv[1]
        suffix = datetime.today().strftime('%Y-%m-%d')
        rename_files(folder_path, suffix)

    else:
        print("1st argument is folder path & 2nd is suffix")


if __name__ == '__main__':
    main()
