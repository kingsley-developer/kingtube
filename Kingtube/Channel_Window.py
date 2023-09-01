import ttkbootstrap as tb
import KingTube_config
import threading
from pytube import Channel
from tkinter import messagebox

def new_Window():
    def getVA_or_A():
        return vandA_orA_codec.get()

    def getVorA():
        return v_A.get()

    def download_Youtube_Video():
        def thread_running():
            url = channel_url_youtube.get()
            path = output_Video_Location_Entry.get()
            va_a_codec = getVA_or_A()
            video_audio = getVorA()
            video_res = res_combo.get()
            video_res_index = res_combo.current()
            audio_res = res_combo_for_audio.get()
            audio_res_index = res_combo_for_audio.current()

            err_msg.config(text="")
            invalid_res_msg.config(text="")
            invalid_res_audio_msg.config(text="")

            try:
                if video_audio == 0:
                    if va_a_codec == 0:
                        if video_res_index == 0:
                            c = Channel(url)
                            download_progress_bar.start()
                            window.update_idletasks()
                            for videos in c.videos:
                                videos.streams.filter(only_video=True, file_extension="mp4",res=video_res, progressive=True)\
                                    .first().download(output_path=path)
                            download_progress_bar.stop()
                            download_progress_bar["value"] = 100
                            window.update_idletasks()
                            messagebox.showinfo(title="Channel videos", message="videos downloaded")

                        elif video_res_index == 1:
                            c = Channel(url)
                            download_progress_bar.start()
                            window.update_idletasks()
                            for videos in c.videos:
                                videos.streams.filter(only_video=True, file_extension="mp4",res=video_res, progressive=True)\
                                    .first().download(output_path=path)
                            download_progress_bar.stop()
                            download_progress_bar["value"] = 100
                            window.update_idletasks()
                            messagebox.showinfo(title="Channel videos", message="videos downloaded")

                        elif video_res_index == 2:
                            c = Channel(url)
                            download_progress_bar.start()
                            window.update_idletasks()
                            for videos in c.videos:
                                videos.streams.filter(only_video=True, file_extension="mp4",res=video_res, progressive=True)\
                                    .first().download(output_path=path)
                            download_progress_bar.stop()
                            download_progress_bar["value"] = 100
                            window.update_idletasks()
                            messagebox.showinfo(title="Channel videos", message="videos downloaded")

                        elif video_res_index == 3:
                            c = Channel(url)
                            download_progress_bar.start()
                            window.update_idletasks()
                            for videos in c.videos:
                                videos.streams.filter(only_video=True, file_extension="mp4",res=video_res, progressive=True)\
                                    .first().download(output_path=path)
                            download_progress_bar.stop()
                            download_progress_bar["value"] = 100
                            window.update_idletasks()
                            messagebox.showinfo(title="Channel videos", message="videos downloaded")

                        elif video_res_index == 4:
                            c = Channel(url)
                            download_progress_bar.start()
                            window.update_idletasks()
                            for videos in c.videos:
                                videos.streams.filter(only_video=True, file_extension="mp4",res=video_res, progressive=True)\
                                    .first().download(output_path=path)
                            download_progress_bar.stop()
                            download_progress_bar["value"] = 100
                            window.update_idletasks()
                            messagebox.showinfo(title="Channel videos", message="videos downloaded")

                        elif video_res_index == 5:
                            c = Channel(url)
                            download_progress_bar.start()
                            window.update_idletasks()
                            for videos in c.videos:
                                videos.streams.filter(only_video=True, file_extension="mp4",res=video_res, progressive=True)\
                                    .first().download(output_path=path)
                            download_progress_bar.stop()
                            download_progress_bar["value"] = 100
                            window.update_idletasks()
                            messagebox.showinfo(title="Channel videos", message="videos downloaded")
                        else:
                            invalid_res_msg.config(text="Invalid video resolution")
                    elif va_a_codec == 1:
                        if video_res_index == 0:
                            c = Channel(url)
                            download_progress_bar.start()
                            window.update_idletasks()
                            for videos in c.videos:
                                videos.streams.filter(only_video=True, file_extension="mp4",res=video_res, adaptive=True)\
                                    .first().download(output_path=path)
                            download_progress_bar.stop()
                            download_progress_bar["value"] = 100
                            window.update_idletasks()
                            messagebox.showinfo(title="Channel videos", message="videos downloaded")

                        elif video_res_index == 1:
                            c = Channel(url)
                            download_progress_bar.start()
                            window.update_idletasks()
                            for videos in c.videos:
                                videos.streams.filter(res=video_res, adaptive=True,only_video=True, file_extension="mp4")\
                                    .first().download(output_path=path)
                            download_progress_bar.stop()
                            download_progress_bar["value"] = 100
                            window.update_idletasks()
                            messagebox.showinfo(title="Channel videos", message="videos downloaded")

                        elif video_res_index == 2:
                            c = Channel(url)
                            download_progress_bar.start()
                            window.update_idletasks()
                            for videos in c.videos:
                                videos.streams.filter(res=video_res, adaptive=True,only_video=True, file_extension="mp4")\
                                    .first().download(output_path=path)
                            download_progress_bar.stop()
                            download_progress_bar["value"] = 100
                            window.update_idletasks()
                            messagebox.showinfo(title="Channel videos", message="videos downloaded")

                        elif video_res_index == 3:
                            c = Channel(url)
                            download_progress_bar.start()
                            window.update_idletasks()
                            for videos in c.videos:
                                videos.streams.filter(only_video=True, file_extension="mp4",res=video_res, adaptive=True)\
                                    .first().download(output_path=path)
                            download_progress_bar.stop()
                            download_progress_bar["value"] = 100
                            window.update_idletasks()
                            messagebox.showinfo(title="Channel videos", message="videos downloaded")

                        elif video_res_index == 4:
                            c = Channel(url)
                            download_progress_bar.start()
                            window.update_idletasks()
                            for videos in c.videos:
                                videos.streams.filter(only_video=True, file_extension="mp4",res=video_res, adaptive=True)\
                                    .first().download(output_path=path)
                            download_progress_bar.stop()
                            download_progress_bar["value"] = 100
                            window.update_idletasks()
                            messagebox.showinfo(title="Channel videos", message="videos downloaded")

                        elif video_res_index == 5:
                            c = Channel(url)
                            download_progress_bar.start()
                            window.update_idletasks()
                            for videos in c.videos:
                                videos.streams.filter(res=video_res, adaptive=True,only_video=True, file_extension="mp4")\
                                    .first().download(output_path=path)
                            download_progress_bar.stop()
                            download_progress_bar["value"] = 100
                            window.update_idletasks()
                            messagebox.showinfo(title="Channel videos", message="videos downloaded")
                        else:
                            invalid_res_msg.config(text="Invalid video resolution")
                else:
                    if audio_res_index == 0:
                        c = Channel(url)
                        download_progress_bar.start()
                        window.update_idletasks()
                        for videos in c.videos:
                            videos.streams.filter(only_audio=True, abr=audio_res).first().download(output_path=path)
                        download_progress_bar.stop()
                        download_progress_bar["value"] = 100
                        window.update_idletasks()
                        messagebox.showinfo(title="Channel audios", message="audios downloaded")

                    elif audio_res_index == 1:
                        c = Channel(url)
                        download_progress_bar.start()
                        window.update_idletasks()
                        for videos in c.videos:
                            videos.streams.filter(only_audio=True, abr=audio_res).first().download(output_path=path)
                        download_progress_bar.stop()
                        download_progress_bar["value"] = 100
                        window.update_idletasks()
                        messagebox.showinfo(title="Channel audios", message="audios downloaded")

                    elif audio_res_index == 2:
                        c = Channel(url)
                        download_progress_bar.start()
                        window.update_idletasks()
                        for videos in c.videos:
                            videos.streams.filter(only_audio=True, abr=audio_res).first().download(output_path=path)
                        download_progress_bar.stop()
                        download_progress_bar["value"] = 100
                        window.update_idletasks()
                        messagebox.showinfo(title="Channel audios", message="audios downloaded")

                    elif audio_res_index == 3:
                        c = Channel(url)
                        download_progress_bar.start()
                        window.update_idletasks()
                        for videos in c.videos:
                            videos.streams.filter(only_audio=True, abr=audio_res).first().download(output_path=path)
                        download_progress_bar.stop()
                        download_progress_bar["value"] = 100
                        window.update_idletasks()
                        messagebox.showinfo(title="Channel audios", message="audios downloaded")
                    else:
                        invalid_res_audio_msg.config(text="Invalid resolution")


            except Exception as error:
                err_msg.config(text=str(error))
                download_progress_bar.stop()
                download_progress_bar["value"] = 0
                window.update_idletasks()
                messagebox.showerror(title="Channel videos", message="videos/audios download failed")


        new_Thread = threading.Thread(target=thread_running, name="Channel_thread_running", daemon=True)
        new_Thread.start()


    window = tb.Toplevel()
    window.title("KingTube")

    #CENTER WINDOW
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
                     text="Download Your Channel Youtube Videos",
                     font=("Impact", 34),
                     bootstyle="white")
    title.pack()

    paste_url = tb.Label(master=window,
                         text="Enter or paste the url of the youtube channel",
                         font=("Impact", 23),
                         bootstyle="warning")
    paste_url.place(x=10, y=90)

    channel_url_youtube = tb.Entry(master=window,
                                 width=50, foreground="yellow",
                                 font=("Aerial", 18),
                                 bootstyle="primary")
    channel_url_youtube.place(x=0, y=150)

    choose_Resolution = tb.Label(master=window,
                                 text="Choose video resolution", font=("Impact", 17),
                                 bootstyle="warning")
    choose_Resolution.place(x=660, y=100)

    res_combo = tb.Combobox(master=window,
                            bootstyle="white",
                            foreground="white",
                            font=("Aerial", 16),
                            values=KingTube_config.video_resolutions,
                            width=15)
    res_combo.place(x=675, y=150)
    res_combo.current(0)

    invalid_res_msg = tb.Label(master=window, font=("Aerial", 15), bootstyle="danger")
    invalid_res_msg.place(x=677, y=200)

    choose_Res = tb.Label(master=window,
                                 text="Choose audio resolution", font=("Impact", 17),
                                 bootstyle="warning")
    choose_Res.place(x=890, y=200)

    res_combo_for_audio = tb.Combobox(master=window,
                            bootstyle="white",
                            foreground="white",
                            font=("Aerial", 16),
                            values=KingTube_config.audio_resolutions,
                            width=15)
    res_combo_for_audio.place(x=890, y=250)
    res_combo_for_audio.current(0)

    invalid_res_audio_msg = tb.Label(master=window,
                                     font=("Aerial", 15), bootstyle="danger")
    invalid_res_audio_msg.place(x=890, y=300)

    vandA_orA_codec = tb.IntVar()

    toggle_VA_A_Codec = tb.Checkbutton(window,
                                       bootstyle="primary, round-toggle",
                                       text="off for VandA codec or on for audio codec",
                                       variable=vandA_orA_codec,
                                       onvalue=1,
                                       offvalue=0,
                                       command=getVA_or_A)
    toggle_VA_A_Codec.place(x=940, y=80)

    v_A = tb.IntVar()

    toggle_VA_A_Codec = tb.Checkbutton(window,
                                       bootstyle="primary, round-toggle",
                                       text="off to download channel videos on to download audios",
                                       variable=v_A,
                                       onvalue=1,
                                       offvalue=0,
                                       command=getVorA)
    toggle_VA_A_Codec.place(x=940, y=100)

    output_Video_Location = tb.Label(master=window,
                                     text="Enter the destination location of videos/audios",
                                     font=("Impact", 18),
                                     bootstyle="warning")

    output_Video_Location.place(x=10, y=200)

    output_Video_Location_Entry = tb.Entry(master=window,
                                           width=50,
                                           foreground="yellow",
                                           font=("Aerial", 18),
                                           bootstyle="yellow")
    output_Video_Location_Entry.place(x=0, y=250)

    output_Video_Location_Entry_Msg = tb.Label(master=window,
                                               text="Make sure the path slash is double slash not single if it is backslash e.g D:\\\\Video not D:\\Video",
                                               font=("Aerial", 15),
                                               bootstyle="white")
    output_Video_Location_Entry_Msg.place(x=15, y=300)

    download_Style = tb.Style()
    download_Style.configure("success.TButton", font=("Impact", 19))

    download_Button = tb.Button(master=window, text="Download Channel Videos", bootstyle="success", style="success.TButton",
                                width=23,
                                command=download_Youtube_Video)
    download_Button.place(x=500, y=400)

    download_progress_bar = tb.Progressbar(window,
                                           maximum=100,
                                           value=0)
    download_progress_bar.place(x=285, y=500, width=700)

    err_msg = tb.Label(master=window,
                       font=("Aerial", 14),
                       bootstyle="danger")

    err_msg.place(x=15, y=600)




