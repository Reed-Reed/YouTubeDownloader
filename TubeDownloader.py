"""
This program allows the user to paste a YouTube link and download a video. You can use the
keyword parameter 'output_path=' in the download function to change the destination path for the download.
"""

from tkinter import *   # GUI library
from pytube import YouTube  # YouTube API


def video_downloader():
    url = YouTube(str(video_link.get()))
    video = url.streams.first()     # select the audio/video stream(s)
    url.check_availability()    # raises exceptions if the video is unavailable
    video.download(output_path=r"C:\Users\reedm\Videos\YouTubeDL")  # Change this to your desired folder
    Label(display_win, text="DOWNLOADED",
          bg='medium turquoise',
          font='arial 12').pack(anchor='center', pady=5)


app_title = "_-* Reed's YouTube Downloader *-_"

display_win = Tk()
display_win.geometry('500x300')    # set the size of the window
display_win.resizable(True, True)     # set the window to not be resizeable
display_win.title(app_title)    # set the window's title
display_win.configure(bg='antique white')

Label(display_win,
      text=app_title,
      bg='antique white',
      font='arial 20 bold').pack(anchor='center', pady=15)

video_link = StringVar()    # string-type variable to store the user-input
Label(display_win,
      text="Paste YouTube video link here:",
      bg='antique white',
      font='arial 18 bold').pack(anchor='center', pady=5)

Entry(display_win,  # Create an empty text box for the user to input YouTube link
      width=75,
      textvariable=video_link).pack(anchor='center', padx=5, pady=5)

Button(display_win,     # Create a button to call video_downloader function
       text="DOWNLOAD",
       font="arial 18 bold",
       bg='dark turquoise',
       padx=5,
       command=video_downloader).pack(anchor='center', pady=25)

display_win.mainloop()  # executes the program loop

