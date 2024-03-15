# Intelligent-Download-Section-Organizer


![GUI Application:1](https://github.com/Tiwarishashwat/Intelligent-Download-Section-Organizer-GUI-Application/blob/main/images/Picture1.png)

## Introduction
In the present scenario of pandemic, each and everyone is well known with the fact that everything has shifted to online. All the exchange of information between people working in different sectors is taking place through documents, pdfs, files and other soft copy formats. So, when all this reach to our system via emails or other modes it's almost impossible to organize all that downloaded documents and files in the system's downloads section. If someone is downloading files, documents etc. at the rate of 100-200 files or documents every now and then which will create a haphazard in the system. It will also lead to unnecessary consumption of the drivers present in the system and this can trouble the user in order to maintain the decorum of their documents and files. It is a time-consuming process to find out the desired files or documents from a huge number of clutter present in the downloads section.
So, this project brings an intelligent software which will automatically segregate and organize the files and documents present in downloads section of user's system on the basis of file type (that is .txt,.docx,.jpeg etc.). Not only this but it will also take care of user's desire of setting up the location of the specific document or file along with some other vibrant features.
Keywords: Intelligent, Organizer, File Extension


Step-1: Assembling GUI application
Create a GUI Application using the Tkinter Module, include various functionalities such as:
1.1	Organize Button: For performing sorting.
1.2	Check Button: For calculating the total number of different files.
1.3	Rename Button: For renaming an old file to a new file.
1.4	Delete Button: For deleting a file.
1.5	Size Button: For detecting the size of the application.
1.6	Automate Button: For enabling the background scripting.
1.7	Close Button: Close the GUI Application.
1.8	Message Box: For interacting with the user.

Step-2: Detecting when a new file enters in the downloads folder.
Total number of files is calculated and script calculates and compares the number of files after every fixed interval (10 minutes default) and run the source script in case of any change.

Step-3: Replacing the blank spaces of the file name with “-”.
Read the name of the newly added file, detect white spaces in the file name, replace the white space with “-”, in order to avoid No file found exception.

Step-4: Finding the file type using the Magic Number.
Read the header of the new file added, obtain the Magic number and hence find the appropriate file type using the fleep module.

Step-5: Finding the file type using the file extension.
Once the File type is recognized, another important task is to overcome the drawbacks of fleep module, hence find the extension of the unknown files if any.

Step-6: Segregating the file based on file type.
In this step the files/documents in the downloads section will be segregated on the basis of extension type i.e. files with .txt extension will be shifted to the directory created for text documents ,likewise for the files with other extensions.

Step-7: Creating Directories inside the downloads folder.
Directories will be created inside the downloads section for various file extensions separately and then files will be moved to their respective directories on the basis of extension type.

Step-8: Moving the files into the newly created sub directories.
Files will be moved to the newly created directories with respect to extension type.

Step-9: Sleep the program until a new file arrives.
In this step, the resources will set free with the help of sleep function (time module) until the new file arrives in the downloads section.

