# import tkinter as tk
# from tkinter import ttk , filedialog

# import requests

# class Downloader:
#     def __init__(self):
#         self.window = tk.Tk()
#         self.window.title("Python GUI Downloader")
#         self.url_label = tk.Label(text="Enter URL",bg="blue")
#         self.url_label.pack()
#         self.url_entry = tk.Entry(self.window)
#         self.url_entry.pack()
#         self.Browse_button = tk.Button(text="Browse", command=self.Browse_file)
#         self.Browse_button.pack()
#         self.download_button = tk.Button(text="Download",command=self.download)
#         self.download_button.pack()
#         self.progress_bar = ttk.Progressbar(self.window, orient="horizontal",maximum=100, length=100, mode="determinate")
#         self.progress_bar.pack()


#         self.window.geometry("720x480")
#         self.window.mainloop()





#     def Browse_file(self):
#         filename = filedialog.asksaveasfilename()
#         self.url_entry.insert(0,filename)

#     def download(self):
#         url = self.url_entry.get()
#         response = requests.get(url,stream=True)
#         total_sixe_in_bytes = int(response.headers.get("content-lenght"))
#         block_size= 10000
#         self.progress_bar["value"]=0
#         fileName=self.url_entry.get().split("/")[-1]
#         with open(fileName,"wb") as f:
#             for data in response.iter_content(block_size):
#                 self.progress_bar["value"]+= (100*block_size)/total_sixe_in_bytes
#                 print(self.progress_bar["value"])
#                 self.window.update()
#                 f.write(data)
# Downloader()

import tkinter as tk
from tkinter import ttk, filedialog
import requests
import threading

class Downloader:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Python GUI Downloader")

        # URL input
        self.url_label = tk.Label(self.window, text="Enter URL", bg="blue", fg="white")
        self.url_label.pack(pady=5)
        self.url_entry = tk.Entry(self.window, width=50)
        self.url_entry.pack(pady=5)

        # Save location
        self.save_button = tk.Button(self.window, text="Choose Save Location", command=self.browse_file)
        self.save_button.pack(pady=5)
        self.save_path = tk.Entry(self.window, width=50)
        self.save_path.pack(pady=5)

        # Download button
        self.download_button = tk.Button(self.window, text="Download", command=self.start_download)
        self.download_button.pack(pady=10)

        # Progress bar
        self.progress_bar = ttk.Progressbar(self.window, orient="horizontal", maximum=100, length=400, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.window.geometry("720x480")
        self.window.mainloop()

    def browse_file(self):
        filename = filedialog.asksaveasfilename(defaultextension=".bin")
        if filename:
            self.save_path.delete(0, tk.END)
            self.save_path.insert(0, filename)

    def start_download(self):
        # Run download in a separate thread to avoid GUI freezing
        threading.Thread(target=self.download).start()

    def download(self):
        url = self.url_entry.get()
        save_file = self.save_path.get()

        if not url or not save_file:
            print("URL or save path missing!")
            return

        response = requests.get(url, stream=True)
        total_size_in_bytes = int(response.headers.get("content-length", 0))
        block_size = 1024
        downloaded = 0

        self.progress_bar["value"] = 0

        with open(save_file, "wb") as f:
            for data in response.iter_content(block_size):
                downloaded += len(data)
                f.write(data)
                percent = (downloaded / total_size_in_bytes) * 100
                self.progress_bar["value"] = percent
                self.window.update_idletasks()

        print("Download complete!")

Downloader()