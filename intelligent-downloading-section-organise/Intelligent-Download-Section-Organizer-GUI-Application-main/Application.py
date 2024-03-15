from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog
import time
import os
import fleep
import shutil
from tkinter import messagebox
class App:
    def __init__(self,root):
        self.name_of_dir=""
        self.sub_dir=["image","audio","video","document","archive","executables","font","system","database"]
        self.root=root
        self.filename=""
        width_value=self.root.winfo_screenwidth()
        height_value=self.root.winfo_screenheight()
        self.root.title("Intelligent Download Section Organizer | Developed by Shashwat & Ayushi")
        self.root.geometry("%dx%d+0+0" % (width_value,height_value))
        self.root.config(bg="white")
        self.logo_icon=PhotoImage(file="images/pink_folder.png")
        title = Label(self.root,text="Intelligent Download Section Organizer",padx=10,image=self.logo_icon,compound=LEFT,font=("impact",40),bg="#023548",fg="white",anchor="w").place(x=0,y=0,relwidth=1)
        #---------Section-1---------#
        self.var_foldername=StringVar()
        lbl_select_folder=Label(self.root, text="Select File",font=("times new roman",25,"bold"),bg="white").place(x=50,y=150)
        txt_folder_name=Entry(self.root,textvariable=self.var_foldername,font=("times new roman",15,),state="readonly", bg="lightyellow").place(x=250,y=150,height=40,width=600)
        bttn_browse=Button(self.root,command=self.browse_function,text="Browse",font=("times new roman",15,"bold"),bd=4,relief=RAISED,bg="#262626", fg="white",activebackground="#262626",cursor="hand2",activeforeground="white").place(x=900,y=145,height=45,width=150)
        hr1=Label(self.root,bg="lightgray").place(x="50",y="200",height=2,width=0.9*width_value)
        hr2=Label(self.root,bg="lightgray").place(x=0.5*width_value,y="200",height=0.6*height_value,width=2)
        #---------Section-2---------#
        #---------All Extentions----#
        self.image_extentions=["Images",".png",".jpeg"]
        self.audio_extentions=["Audios",".amr",".mp3"]
        self.video_extentions=["Videos",".mp4",".avi",".mpeg4",".3gp"]
        self.document_extentions=["Documents",".docx",".xlsx",".ppt",".pptx",".xls","pdf",".zip",".rar",".csv",".doc",".txt"]
        lbl_support_extention=Label(self.root, text="Folder Status",font=("times new roman",20,"bold"),bg="white").place(x=50,y=210)
        self.image_box=ttk.Combobox(self.root,values=self.image_extentions,font=("times new roman",15),state="readonly",justify=CENTER)
        self.image_box.place(x=(0.5*width_value)+10,y=210,width=120,height=35)
        self.image_box.current(0)
        self.audio_box=ttk.Combobox(self.root,values=self.audio_extentions,font=("times new roman",15),state="readonly",justify=CENTER)
        self.audio_box.place(x=(0.5*width_value)+135,y=210,width=120,height=35)
        self.audio_box.current(0)
        self.video_box=ttk.Combobox(self.root,values=self.video_extentions,font=("times new roman",15),state="readonly",justify=CENTER)
        self.video_box.place(x=(0.5*width_value)+260,y=210,width=120,height=35)
        self.video_box.current(0)
        self.document_box=ttk.Combobox(self.root,values=self.document_extentions,font=("times new roman",15),state="readonly",justify=CENTER)
        self.document_box.place(x=(0.5*width_value)+385,y=210,width=120,height=35)
        self.document_box.current(0)
        #hr3=Label(self.root,bg="lightgray").place(x=0.5*width_value+1,y="200",height=2,width=0.4*width_value)
        #---------Section-3---------#
        #---------All Image Icons---#
        self.directory_icon=PhotoImage(file="images/folderr.png")
        self.image_icon=PhotoImage(file="images/gallery.png")
        self.audio_icon=PhotoImage(file="images/tunes.png")
        self.video_icon=PhotoImage(file="images/vid.png")
        self.document_icon=PhotoImage(file="images/docu.png")
        self.others_icon=PhotoImage(file="images/o.png")
        #Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        #Frame1.place(x=50,y=310,width=1250,height=300)
        #self.lbl_total_files=Label(Frame1, text="Total Files",font=("times new roman",20,"bold"),bg="white")
        #self.lbl_total_files.place(x=10,y=10)
        self.lbl_total_directories=Label(self.root,text="Total Directories",image=self.directory_icon,bd=2,relief=RAISED,compound=TOP,font=("times new roman",15,"bold"),bg="#008EA4",fg="white")
        self.lbl_total_directories.place(x=50,y=260,width=180,height=180)
        self.lbl_total_images=Label(self.root,text="Total Images",image=self.image_icon,bd=2,relief=RAISED,compound=TOP,font=("times new roman",15,"bold"),bg="#DF002A",fg="white")
        self.lbl_total_images.place(x=260,y=260,width=180,height=180)
        self.lbl_total_audio=Label(self.root,text="Total Audio",image=self.audio_icon,bd=2,relief=RAISED,compound=TOP,font=("times new roman",15,"bold"),bg="#008EA4",fg="white")
        self.lbl_total_audio.place(x=470,y=260,width=180,height=180)
        self.lbl_total_video=Label(self.root,text="Total Video",image=self.video_icon,bd=2,relief=RAISED,compound=TOP,font=("times new roman",15,"bold"),bg="#DF002A",fg="white")
        self.lbl_total_video.place(x=50,y=460,width=180,height=180)
        self.lbl_total_document=Label(self.root,text="Total Document",image=self.document_icon,bd=2,relief=RAISED,compound=TOP,font=("times new roman",15,"bold"),bg="#008EA4",fg="white")
        self.lbl_total_document.place(x=260,y=460,width=180,height=180)
        self.lbl_total_others=Label(self.root,text="Total other",image=self.others_icon,bd=2,relief=RAISED,compound=TOP,font=("times new roman",15,"bold"),bg="#DF002A",fg="white")
        self.lbl_total_others.place(x=470,y=460,width=180,height=180)
        #---------Section-4---------#
        #---------Button&Status-----#
        #self.lbl_status=Label(self.root, text="Console:",font=("times new roman",15,"bold"),bg="white")
        #self.lbl_status.place(x=(0.5*width_value)+10,y=510)
        #self.lbl_st_total=Label(self.root, text="Total:",font=("times new roman",15,"bold"),bg="white",fg="green")
        #self.lbl_st_total.place(x=(0.5*width_value)+10,y=560)
        #self.lbl_st_moved=Label(self.root, text="Moved:",font=("times new roman",15,"bold"),bg="white",fg="blue")
        #self.lbl_st_moved.place(x=(0.5*width_value)+10,y=610)
        #self.lbl_st_left=Label(self.root, text="Left:",font=("times new roman",15,"bold"),bg="white",fg="orange")
        #self.lbl_st_left.place(x=(0.5*width_value)+10,y=660)
        #self.bttn_clear=Button(self.root,text="Clear",font=("times new roman",15,"bold"),bd=4,relief=RAISED,bg="#262626", fg="white",activebackground="#262626",cursor="hand2",activeforeground="white")
        #self.bttn_clear.place(x=100,y=700,height=45,width=150)
        self.bttn_organize=Button(self.root,text="Organize",command=self.sorting,font=("times new roman",15,"bold"),bd=4,relief=RAISED,bg="#262626", fg="white",activebackground="#262626",cursor="hand2",activeforeground="white")
        self.bttn_organize.place(x=(0.5*width_value)+70,y=410,width=120,height=35)

        self.bttn_rename=Button(self.root,text="Rename",command=self.single_rename,font=("times new roman",15,"bold"),bd=4,relief=RAISED,bg="#262626", fg="white",activebackground="#262626",cursor="hand2",activeforeground="white")
        self.bttn_rename.place(x=(0.5*width_value)+210,y=410,width=120,height=35)

        self.bttn_delete=Button(self.root,text="Delete",command=self.delete_file,font=("times new roman",15,"bold"),bd=4,relief=RAISED,bg="#262626", fg="white",activebackground="#262626",cursor="hand2",activeforeground="white")
        self.bttn_delete.place(x=(0.5*width_value)+350,y=410,width=120,height=35)

        self.bttn_size=Button(self.root,text="Size",command=self.find_size,font=("times new roman",15,"bold"),bd=4,relief=RAISED,bg="#262626", fg="white",activebackground="#262626",cursor="hand2",activeforeground="white")
        self.bttn_size.place(x=(0.5*width_value)+70,y=460,width=120,height=35)

        self.bttn_automate=Button(self.root,text="Automate",command=self.automate_function,font=("times new roman",15,"bold"),bd=4,relief=RAISED,bg="#262626", fg="white",activebackground="#262626",cursor="hand2",activeforeground="white")
        self.bttn_automate.place(x=(0.5*width_value)+210,y=460,width=120,height=35)

        self.bttn_close=Button(self.root,text="Close",font=("times new roman",15,"bold"),command=self.root.destroy,bd=4,relief=RAISED,bg="#262626", fg="white",activebackground="#262626",cursor="hand2",activeforeground="white")
        self.bttn_close.place(x=(0.5*width_value)+350,y=460,width=120,height=35)

        self.bttn_check=Button(self.root,text="Check",command=self.total_count,font=("times new roman",15,"bold"),bd=4,relief=RAISED,bg="#262626", fg="white",activebackground="#262626",cursor="hand2",activeforeground="white")
        self.bttn_check.place(x=275,y=655,height=45,width=150)
        #---------Section-5-----------#
        """
        self.list1=Listbox(self.root)
        self.list1.place(x=(0.5*width_value)+10,y=510,height=10,width=35)
        self.list1.grid(row=12,column=8000,rowspan=6,columnspan=2)

        self.sb1=Scrollbar(self.root)
        self.sb1.grid(row=12,column=12,rowspan=6)

        self.list1.configure(yscrollcomman=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)
        """
        #list1.bind('<<ListboxSelect>>',get_selected_row)
        #---------Functionalities-----#
    def total_count(self):
        self.t_doc=0
        self.t_audio=0
        self.t_fol=0
        self.t_image=0
        self.t_other=0
        self.t_video=0
        with os.scandir('C:/Users/shash/Downloads/') as entries:
            for self.name_of_file in entries:
                print(self.name_of_file)
                path=os.path.join("C:/Users/shash/Downloads/",self.name_of_file)
                print(path)
                fname,fext = os.path.splitext(self.name_of_file)
                if os.path.isdir(path):
                    self.t_fol+=1
                else:
                    self.identify_file_type(self.name_of_file)
                    if self.name_of_dir=="image":
                        self.t_image+=1
                    elif self.name_of_dir=="audio":
                        self.t_audio+=1
                    elif self.name_of_dir=="video":
                        self.t_video+=1
                    elif self.name_of_dir=="document":
                        self.t_doc+=1
                    else:
                        self.t_other+=1
            self.lbl_total_directories.config(text="Total Directories\n"+str(self.t_fol))
            self.lbl_total_images.config(text="Total Image\n"+str(self.t_image))
            self.lbl_total_audio.config(text="Total Audio\n"+str(self.t_audio))
            self.lbl_total_video.config(text="Total Video\n"+str(self.t_video))
            self.lbl_total_others.config(text="Total Others\n"+str(self.t_other))
            self.lbl_total_document.config(text="Total Document\n"+str(self.t_doc))
    def automate_function(self):
        while True:
            totalfiles=len(os.listdir("C:/Users/shash/Downloads/"))
            print(totalfiles,":before sleep")
            OldNumber = totalfiles
            time.sleep(10)
            totalfiles=len(os.listdir("C:/Users/shash/Downloads/"))
            print(totalfiles,":after sleep")
            if totalfiles!=OldNumber:
                self.sorting()
            else:
                print("sleeping")
                time.sleep(10)
    def browse_function(self):
        path=r"C:\Users\shash\Downloads"
        #self.var_foldername.asksaveasfilename()
        self.filename = askopenfilename(initialdir=r"C:\Users\shash\Downloads", title="select a file")
        self.var_foldername.set(str(self.filename))
    def select_a_file(self):
        path=r"C:\Users\shash\Downloads"
        #self.var_foldername.set(self.filename)
    def find_size(self):
        total_size = 0
        start_path = r"C:\Users\shash\Downloads"  # To get size of current directory
        for path, dirs, files in os.walk(start_path):
            for f in files:
                fp = os.path.join(path, f)
                total_size += os.path.getsize(fp)
        msg="Directory size is: "+str(round((total_size)/(1073741824),2))+"GB"
        messagebox.showinfo(title="Prompt",message=msg)
    def delete_file(self):
        if self.filename=="":
            messagebox.showinfo(title="warning",message="Please select a file first using browse button")
        else:
            if os.path.exists(self.filename):
                os.remove(self.filename)
                messagebox.showinfo(title="Success",message="File deleted successfully")
            else:
                messagebox.showinfo(title="Warning",message="The file does not exist")
            self.var_foldername.set(str(""))
    def make_directories(self,name_of_dir):
        print("Hello Directory Function")
        print(self.name_of_dir)
        path="C:/Users/shash/Downloads/"+self.name_of_dir
        print(path)
        isExist = os.path.exists(path)
        print("You Exist?",isExist)
        if isExist:
            print("I Exist")
        else:
            os.mkdir(path)
        return 1

    def identify_file_type(self,name_of_file):
        fname,fext = os.path.splitext(self.name_of_file)
        print(fname)
        with open(self.name_of_file, "rb") as file:
            info = fleep.get(file.read(128))
            print(info)
            if(info.extension_matches(fext[1:])):
                for i in self.sub_dir:
                    flag=0
                    for j in info.mime:
                        if j.find(i)!=-1:
                            flag=1
                            self.name_of_dir=i
                            print("directory name is",self.name_of_dir)
                            break
                    if flag==1:
                        break
            else:
                print("name of dir is",self.name_of_dir)
                self.name_of_dir=fext[1:]

    def remove_spaces_from_filenames(self):
        try:
            filenames = os.listdir("C:/Users/shash/Downloads/")
            for filename in filenames:
                os.rename(os.path.join("C:/Users/shash/Downloads/", filename), os.path.join("C:/Users/shash/Downloads/", filename.replace(' ', '-')))
        except Exception:
            pass

    def move_to_dir(self,name_of_file,name_of_dir):
        try:
            #move=0;
            source=os.path.join("C:/Users/shash/Downloads/",self.name_of_file)
            dest =os.path.join("C:/Users/shash/Downloads/",self.name_of_dir+"/")
            shutil.move(source,dest)
            #move+=1
            print("Moved successfully")
        except Exception:
            pass
    #remove_spaces_from_filenames()
    def sorting(self):
        self.counter=0
        with os.scandir('C:/Users/shash/Downloads/') as entries:
            for self.name_of_file in entries:
                print(self.name_of_file)
                path=os.path.join("C:/Users/shash/Downloads/",self.name_of_file)
                print(path)
                fname,fext = os.path.splitext(self.name_of_file)
                n=fname[2:].strip()+".py"
                if n=="source.py" or n=="run_automatically.py":
                    continue
                if os.path.isdir(path):
                    continue
                else:
                    print(self.name_of_file)
                    self.identify_file_type(self.name_of_file)
                    self.make_directories(self.name_of_dir)
                    self.move_to_dir(self.name_of_file,self.name_of_dir)
                    self.counter+=1
                    #self.lbl_st_moved.set(counter)
                    print("done",self.counter)
                    #messagebox.showinfo(title="Success",message="Files moved successfully")
            if self.counter!=0:
                messagebox.showinfo(title="Success",message="Files segregated successfully")
            else:
                messagebox.showinfo(title="Prompt",message="No new files to be moved")
        return self.counter
    def multi_rename(self):
        with os.scandir('C:/Users/shash/Downloads/') as entries:
            count=0
            for self.name_of_file in entries:
                path=os.path.join("C:/Users/shash/Downloads/",self.name_of_file)
                fname,fext = os.path.splitext(self.name_of_file)
                n=fname[2:].strip()+".py"
                if n=="source.py":
                    continue
                dst ="Pattern"+str(count)+fext
                dst =os.path.join("C:/Users/shash/Downloads/",dst)
                #src =os.path.join("./",filename)
                os.rename(self.name_of_file, dst)
                count+=1
    def single_rename(self):
        if self.filename=="":
            messagebox.showinfo(title="warning",message="Please select a file first using browse button")
            #simpledialog.askstring(title="file name",prompt="Rename to?")
        else:
            fname,fext = os.path.splitext(self.filename)
            self.input=simpledialog.askstring(title="file name",prompt="Rename to?")
            dst=self.input+fext
            dst =os.path.join("C:/Users/shash/Downloads/",dst)
            os.rename(self.filename, dst)
            #self.filename=""
            self.var_foldername.set(str(""))
            messagebox.showinfo(title="Success",message="File renamed successfully")
root=Tk()
obj=App(root)
root.mainloop()
