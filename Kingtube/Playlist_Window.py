import ttkbootstrap as tb
import KingTube_config
import threading
from automateYT import Automate
from pytube import Playlist
from tkinter import messagebox

def new_Window():

    def get_Vs_As():
        return videos_audios.get()

    def get_H_L():
        return videos_h_l.get()

    def download_playlist_videos():
        def thread_running():
            url = playlist_url_youtube.get()
            path = output_Playlist_Location_Entry.get()
            toggle_Value = get_Vs_As()
            videos_res = get_H_L()

            err_msg.config(text="")
            try:
                if toggle_Value == 0:
                    if videos_res == 0:
                        download_progress_bar.start()
                        window.update_idletasks()

                        Automate(url).download_playlist(
                            limit=1000000,
                            location=path,
                            lowest_res=True,
                            subtitle=True
                        )
                        download_progress_bar.stop()
                        download_progress_bar["value"] = 100
                        window.update_idletasks()
                        messagebox.showinfo(title="Playlist Videos", message="Playlist videos downloaded")
                    else:
                        download_progress_bar.start()
                        window.update_idletasks()
                        Automate(url).download_playlist(
                            limit=1000000,
                            location=path,
                            highest_res=True,
                            subtitle=True
                        )
                        download_progress_bar.stop()
                        download_progress_bar["value"] = 100
                        window.update_idletasks()
                        messagebox.showinfo(title="Playlist Videos", message="Playlist videos downloaded")
                else:
                    pl = Playlist(url=url)
                    download_progress_bar.start()
                    window.update_idletasks()
                    for video in pl.videos:
                        video.streams.filter(only_audio=True).first().download(output_path=path)
                    download_progress_bar.stop()
                    download_progress_bar["value"] = 100
                    window.update_idletasks()
                    messagebox.showinfo(title="Playlist Audios", message="Playlist audios downloaded")

            except Exception as err:
                err_msg.config(text=str(err))
                download_progress_bar.stop()
                download_progress_bar["value"] = 0
                window.update_idletasks()
                messagebox.showerror(title="Playlist Videos/audios", message="download failed")

        new_Thread = threading.Thread(target=thread_running, name="Playlist_thread_running", daemon=True)
        new_Thread.start()

    window = tb.Toplevel()
    window.title("KingTube")

    # CENTER WINDOW
    win_width = 1270
    win_height = 700
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
                     text="Download Your Youtube Playlist Videos",
                     font=("Impact", 38),
                     bootstyle="white")

    title.pack()

    videos_h_l = tb.IntVar()

    toggle_h_l = tb.Checkbutton(master=window,
                                  bootstyle="primary, round-toggle",
                                  text="Select low/high for downloading playlist videos",
                                  variable=videos_h_l,
                                  onvalue=1,
                                  offvalue=0,
                                  command=get_H_L)
    toggle_h_l.place(x=15, y=87)

    paste_url = tb.Label(master=window,
                         text="Enter or paste the url of the youtube playlist",
                         font=("Impact", 18),
                         bootstyle="warning")
    paste_url.pack(pady=40)

    videos_audios = tb.IntVar()

    toggle_Vs_As = tb.Checkbutton(master=window,
                                       bootstyle="primary, round-toggle",
                                       text="Download Playlist videos/audios",
                                       variable=videos_audios,
                                       onvalue=1,
                                       offvalue=0,
                                       command=get_Vs_As)
    toggle_Vs_As.place(x=1000, y=80)

    playlist_url_youtube = tb.Entry(master=window, width=40, foreground="yellow", font=("Aerial", 18), bootstyle="primary")
    playlist_url_youtube.pack()

    output_Video_Location = tb.Label(master=window, text="Enter the destination location of playlist videos/audios",
                                     font=("Impact", 18),
                                     bootstyle="warning")

    output_Video_Location.pack(pady=40)

    output_Playlist_Location_Entry = tb.Entry(master=window, width=40, foreground="yellow", font=("Aerial", 18),
                                           bootstyle="yellow")
    output_Playlist_Location_Entry.pack()

    output_Playlist_Location_Entry_Msg = tb.Label(master=window,
                                               text="Make sure the path slash is double slash not single if it is backslash e.g D:\\\\Video not D:\\Video",
                                               font=("Aerial", 13),
                                               bootstyle="white")
    output_Playlist_Location_Entry_Msg.pack()

    download_Style = tb.Style()
    download_Style.configure("success.TButton", font=("Impact", 19))

    download_Button = tb.Button(master=window, text="Download Playlist Videos", bootstyle="success",
                                style="success.TButton",
                                width=25,
                                command=download_playlist_videos)
    download_Button.pack(pady=40)

    download_progress_bar = tb.Progressbar(window,
                                          maximum=100,
                                          value=0)
    download_progress_bar.pack(fill=tb.X, padx=230)

    err_msg = tb.Label(master=window,
                     font=("Aerial", 14),
                     bootstyle="danger")

    err_msg.place(x=15, y=640)



