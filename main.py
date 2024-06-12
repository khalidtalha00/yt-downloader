import tkinter
import customtkinter
from pytube import YouTube


def StartDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title)
        finishlabel.configure(text="")
        video.download()
        finishlabel.configure(text="Video Downloaded!", text_color="green")


    except:
        finishlabel.configure(text="Download Error", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(percentage_of_completion)
    per = str(int(percentage_of_completion))
    percentage.configure(text=per + '%')
    percentage.update()

    # update progress bar
    progressbar.set(float(percentage_of_completion)/100)


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# app frame

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# adding UI elements
title = customtkinter.CTkLabel(app, text="INSERT THE VIDEO LINK")
title.pack(padx=10, pady=10)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# download button

download = customtkinter.CTkButton(app, text="Download", command=StartDownload)
download.pack(padx=20, pady=20)

# download progress

percentage = customtkinter.CTkLabel(app, text="0%")
percentage.pack()

progressbar = customtkinter.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)

# download finish
finishlabel = customtkinter.CTkLabel(app, text="")
finishlabel.pack()

# run app
app.mainloop()
