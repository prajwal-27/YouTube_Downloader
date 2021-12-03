import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog, messagebox
from pytube import YouTube, request
import os
 
class Window():
    # class contains member functions and data members
    def __init__(self, height, width, root): # Constructor
        self.height = height
        self.width = width
        self.root = root
    def set_geometry(self):
        self.root.geometry(str(self.width) + 'x' + str(self.height))
    def title(self, string):
        self.root.title(string)
#******************************************************************************************   
class Commands(Window):
    def __init__(self):
        self.root = root
 
    def download_video(self):
        download_button['state'] = 'disabled'
        #{key1 : value1, key2 : value2}
        try:
            url = url_link.get()
            print(url)
            yt = YouTube(url)
            #yt.author, yt.views, pytube documentation
            stream = yt.streams.first()
            filesize = stream.filesize
            os.chdir(download_path.get())
            print(download_path.get())
 
            with open("sample.mp4", "wb") as f:
                stream = request.stream(stream.url)
                self.downloaded = 0
                while True:
                    chunk = next(stream, None)
                    if(chunk):
                        f.write(chunk)
                        self.downloaded += len(chunk)
                        value = (self.downloaded / filesize) * 100
                        if((value > 25 and value < 30) or (value > 50 and value < 55) or (value > 75 and value < 80)):
                            progress_bar['value'] = value
                            self.root.update_idletasks()
                        progress_bar['value'] = value
                    else:
                        messagebox.showinfo("Info", "Download Completed !")
                        break
 
        except Exception as e:
            messagebox.showerror("Error Downloading", e)
        download_button['state'] = 'normal'
        progress_bar['value'] = 0
    def browse(self):
        download_directory = filedialog.askdirectory(initialdir = "Your current directory")
        download_path.set(download_directory)
 
#******************************************************************************************   
class Widgets(Window):
    def __init__(self):
        self.root = root
 
    def labels(self):
        #Url label
        self.url = tk.Label(self.root, text = "URL :", width = 10, height = 5)
        self.url.config(font = ("Courier", 15))
        self.url.grid(row = 0, column = 0, sticky = 'e')
 
        # Path label
        self.path = tk.Label(self.root, text = "Path :", width = 10, height = 5)
        self.path.config(font = ("Courier", 15))
        self.path.grid(row = 1, column = 0, sticky = 'e')
 
    def entry(self):
        global url_link
        self.url_entry = tk.Entry(self.root, width = 60, textvariable = url_link)
        self.url_entry.grid(row = 0, column = 1, columnspan = 2, padx =10, pady =10)
 
        global download_path
        self.path_entry = tk.Entry(self.root, width = 60, textvariable = download_path)
        self.path_entry.grid(row = 1, column = 1, columnspan = 2, padx =10, pady =10)
 
    def button(self):
        global download_button
        download_button = tk.Button(self.root, text = 'Download', width = 20, command = Commands().download_video)
        download_button.grid(row = 2, column = 2, sticky = 'e', padx = 10, pady =10)
 
        browse_button = tk.Button(self.root, text = 'Browse', width = 20, command = Commands().browse)
        browse_button.grid(row = 2, column = 1, sticky = 'w', padx = 10, pady =10)
 
    def progress(self):
        global progress_bar
        progress_bar = Progressbar(self.root, orient = HORIZONTAL, length = 300, mode = 'determinate')
        progress_bar.grid(row = 3, column = 1, columnspan = 2, padx =10, pady = 10)
#******************************************************************************************  
if __name__ == "__main__":
    root = tk.Tk()
    # Window object
    window = Window(400, 600, root)
    window.set_geometry()
    window.title("YouTube Downloader")
 
    # Widgets object
    widgets = Widgets()
    widgets.labels()
    url_link = StringVar()
    download_path = StringVar()
    widgets.entry()
    widgets.button()
    widgets.progress()
 
    root.mainloop()
