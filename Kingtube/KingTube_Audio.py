from pytube import YouTube
import ttkbootstrap as tb
import KingTube_config
import threading
from tkinter import messagebox

def new_Window():
    def download_audio():
        def thread_running():
            output = str(output_Audio_Location_Entry.get())

            invalid_res_msg.config(text="")
            err_Message_While_Downloading.config(text="")
            display_Ds.set("")

            def get_Audio_bytes(stream, data, bytes):
                if bytes > 0:
                    download_progress_bar.start()
                    display_Ds.set("Downloading: "+str(bytes)+"bytes")
                    window.update_idletasks()
                else:
                    download_progress_bar.stop()
                    download_progress_bar["value"] = 100
                    window.update_idletasks()

            try:
                if(res_combo.current() == 0):
                    yt = YouTube(audio_url_youtube.get(),
                               on_progress_callback=get_Audio_bytes,
                               allow_oauth_cache=True,
                               use_oauth=False
                               )
                    yt.streams.filter(only_audio=True, abr=res_combo.get())\
                       .first()\
                       .download(output_path=output)
                    display_Ds.set("Downloaded")
                    messagebox.showinfo(title="KingTube", message="Youtube audio download successfully")
                elif (res_combo.current() == 1):
                    yt = YouTube(audio_url_youtube.get(),
                                 on_progress_callback=get_Audio_bytes,
                                 allow_oauth_cache=True,
                                 use_oauth=False
                                 )
                    yt.streams.filter(only_audio=True, abr=res_combo.get()) \
                        .first() \
                        .download(output_path=output)
                    display_Ds.set("Downloaded")
                    messagebox.showinfo(title="KingTube", message="Youtube audio download successfully")
                elif (res_combo.current() == 2):
                    yt = YouTube(audio_url_youtube.get(),
                                 on_progress_callback=get_Audio_bytes,
                                 allow_oauth_cache=True,
                                 use_oauth=False
                                 )
                    yt.streams.filter(only_audio=True, abr=res_combo.get()) \
                        .first() \
                        .download(output_path=output)
                    display_Ds.set("Downloaded")
                    messagebox.showinfo(title="KingTube", message="Youtube audio download successfully")
                elif (res_combo.current() == 3):
                    yt = YouTube(audio_url_youtube.get(),
                                 on_progress_callback=get_Audio_bytes,
                                 allow_oauth_cache=True,
                                 use_oauth=False
                                 )
                    yt.streams.filter(only_audio=True, abr=res_combo.get()) \
                        .first() \
                        .download(output_path=output)
                    display_Ds.set("Downloaded")
                    messagebox.showinfo(title="KingTube", message="Youtube audio download successfully")
                else:
                    invalid_res_msg.config(text="Invalid resolution")
            except Exception as error:
                err_Message_While_Downloading.config(text=str(error))
                download_progress_bar.stop()
                download_progress_bar["value"] = 0
                display_Ds.set("")
                window.update_idletasks()
                messagebox.showerror(title="KingTube", message="Download youtube audio failed")


        new_Thread = threading.Thread(target=thread_running, name="Audio_thread_running", daemon=True)
        new_Thread.start()


    window = tb.Toplevel()
    window.title("KingTube")

    # CENTER WINDOW
    win_width = 1270
    win_height = 550
    screen_width = window.winfo_screenwidth()
    ycreen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (win_width / 2))
    y = int((ycreen_height / 2) - (win_height / 2))
    window.geometry("{}x{}+{}+{}".format(win_width, win_height, x, y))

    version_number = tb.Label(master=window,
                              text=KingTube_config.version_number,
                              font=("Impact", 15),
                              bootstyle="success")

    version_number.place(x=5, y=5)

    title = tb.Label(master=window,
                     text="Download Your Youtube Audio",
                     font=("Impact", 38),
                     bootstyle="white")

    title.pack()

    paste_url = tb.Label(master=window,
                         text="Enter or paste the url of the youtube video",
                         font=("Aerial", 23),
                         bootstyle="warning")
    paste_url.place(x=10, y=90)

    audio_url_youtube = tb.Entry(master=window,
                                 width=50,
                                 foreground="yellow",
                                 font=("Aerial", 18),
                                 bootstyle="primary")
    audio_url_youtube.place(x=0, y=150)

    choose_Resolution = tb.Label(master=window, text="Choose audio resolution",
                                 font=("Aerial", 23),
                                 bootstyle="warning")
    choose_Resolution.place(x=650, y=90)

    res_combo = tb.Combobox(master=window, bootstyle="primary",
                            foreground="white",
                            font=("Aerial", 16),
                            values=KingTube_config.audio_resolutions)
    res_combo.place(x=675, y=150)
    res_combo.current(0)

    invalid_res_msg = tb.Label(master=window,
                               font=("Aerial", 15),
                               bootstyle="danger")
    invalid_res_msg.place(x=677, y=200)

    download_Style = tb.Style()
    download_Style.configure("success.TButton", font=("Impact", 18))

    download_Button = tb.Button(master=window, text="Download Audio",
                                bootstyle="success",
                                style="success.TButton",
                                command=download_audio)
    download_Button.place(x=1000, y=150)

    output_Audio_Location = tb.Label(master=window, text="Enter the destination location of audio",
                                     font=("Aerial", 18),
                                     bootstyle="warning")

    output_Audio_Location.place(x=10, y=200)

    output_Audio_Location_Entry = tb.Entry(master=window, width=50,
                                           foreground="yellow",
                                           font=("Aerial", 18),
                                           bootstyle="primary")
    output_Audio_Location_Entry.place(x=0, y=250)

    output_Video_Location_Entry_Msg = tb.Label(master=window,
                                               text="Make sure the path slash is double slash not single if it is backslash e.g D:\\\\Video not D:\\Video",
                                               font=("Aerial", 15),
                                               bootstyle="white")
    output_Video_Location_Entry_Msg.place(x=15, y=300)

    err_Message_While_Downloading = tb.Label(master=window,
                                             font=("Aerial", 15),
                                             bootstyle="danger")
    err_Message_While_Downloading.place(x=400, y=360)

    display_Ds = tb.StringVar()

    download_byte = tb.Label(master=window,
                             textvariable=display_Ds,
                             font=("Aerial", 17),
                             bootstyle="warning")
    download_byte.place(x=610, y=450)

    download_progress_bar = tb.Progressbar(master=window,
                                          maximum=100,
                                          value=0)
    download_progress_bar.place(x=330, y=400, width=700)

