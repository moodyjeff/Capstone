
'''Create a tool for unzipping zipped folders on amazon sagemaker'''

from zipfile import ZipFile

# receive filename to unzip
def unzip_file(file_name):

    with ZipFile(file_name, 'r') as zipObj:
       # Extract all the contents of zip file in current directory
       zipObj.extractall()

    return




'''Create process for seperating classes into train and test data'''

from subprocess import call
import os

def folder_to_train_test_split():
    print(f"The current working directory is {os.getcwd()}. Are you sure about this action?")
    response = input('are you sure?(y,n)')
    train_spit = input('what is your desired % of test data (out of 1)')
    if response == 'y':

        # create list of class names
        folder_names = os.listdir()
        classes = []
        for names in folder_names:
                if names != '.DS_Store':
                    classes.append(names)

        # print calss names
        print(classes)

        # make folder for test files
        call(['mkdir','test'])
        call(['mkdir','train'])
        # Create directory for all class names in test folder
        for i in classes:
            call(['mkdir',f'test/{i}'])

        # let's first calculate the length of the original class folders then calculate how many files to move
        # we want 10% of the files moved to the test folder
        for i in classes:
            # get number of files in the class folder
            num_files = len(os.listdir(i))
            # get the number of test files to move
            num_test = round(num_files*train_split)
            # print out the result
            print(f'{i} has {num_files} files and we will seperate {num_test} for test')

            # create list of files from the class directory to move
            # we will take the files from the end of the file
            files_to_move = os.listdir(f'{i}')[num_files-num_test:]
            # for the files in the above list we will move those files
            for file in files_to_move:
                file_path = f'{i}/{file}'
                new_path =f'test/{i}'
                call(['mv',file_path,new_path])

            call(['mv',i,'train'])

        return
