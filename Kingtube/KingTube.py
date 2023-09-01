from pytube import YouTube
import ttkbootstrap as tb
from tkinter import messagebox
import KingTube_config
import threading
import KingTube_Audio
import Playlist_Window
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter
import Channel_Window

def open_playlist():
    Playlist_Window.new_Window()

def open_channel():
    Channel_Window.new_Window()
def open_audio():
    KingTube_Audio.new_Window()

def getVA_or_A():
    return vandA_orA_codec.get()

def download_Youtube_Video():
    def start_Download():
        try:
            err_Message_While_Downloading.config(text="")
            display_D.set("")
            download_progress_bar._mask = "Download"
            invalid_res_msg.config(text="")
            srt_file_name_combo_err_msg.config(text="")

            output_path = str(output_Video_Location_Entry.get())
            video_resolution = res_combo.get()
            video_resolution_index = res_combo.current()
            language_srt = srt_file_name_combo.get()
            language_srt_index = srt_file_name_combo.current()
            video_or_audio_video_codec = getVA_or_A()
            error_srt_combo = srt_file_name_combo_err_msg

            def get_Video_bytes(stream, data, bytes):
                if bytes > 0:
                    download_progress_bar.start()
                    display_D.set("Downloading: "+str(bytes)+"bytes")
                    window.update_idletasks()
                else:
                    download_progress_bar.stop()
                    download_progress_bar["value"] = 100
                    display_D.set("Downloaded")
                    window.update_idletasks()

            if video_or_audio_video_codec == 0:
                if (video_resolution_index == 0):
                    yt = YouTube(video_url_youtube.get(),
                                 on_progress_callback=get_Video_bytes,
                                 allow_oauth_cache=True,
                                 use_oauth=False
                                 )
                    yt.streams.filter(res=video_resolution, progressive=True, file_extension="mp4",only_video=True)\
                        .first()\
                        .download(output_path=output_path)

                    display_D.set("video downloaded")
                    messagebox.showinfo(title="KingTube", message="Video downloaded")
                    messagebox.showinfo(title="KingTube", message="Wait for srt to be downloaded")

                    if language_srt_index == 0:
                       transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                       formatter = SRTFormatter()
                       srt_formatted = formatter.format_transcript(transcript)
                       srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                       with open(srt_Path_File, 'w') as srt_file:
                           srt_file.write(srt_formatted)
                       display_D.set("srt downloaded")
                       messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 1:
                       transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                       formatter = SRTFormatter()
                       srt_formatted = formatter.format_transcript(transcript)
                       srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                       with open(srt_Path_File, 'w') as srt_file:
                           srt_file.write(srt_formatted)
                       display_D.set("srt downloaded")
                       messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 2:
                       transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                       formatter = SRTFormatter()
                       srt_formatted = formatter.format_transcript(transcript)
                       srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                       with open(srt_Path_File, 'w') as srt_file:
                           srt_file.write(srt_formatted)
                       display_D.set("srt downloaded")
                       messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 3:
                       transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                       formatter = SRTFormatter()
                       srt_formatted = formatter.format_transcript(transcript)
                       srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                       with open(srt_Path_File, 'w') as srt_file:
                           srt_file.write(srt_formatted)
                       display_D.set("srt downloaded")
                       messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 4:
                       transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                       formatter = SRTFormatter()
                       srt_formatted = formatter.format_transcript(transcript)
                       srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                       with open(srt_Path_File, 'w') as srt_file:
                           srt_file.write(srt_formatted)
                       display_D.set("srt downloaded")
                       messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 5:
                       transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                       formatter = SRTFormatter()
                       srt_formatted = formatter.format_transcript(transcript)
                       srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                       with open(srt_Path_File, 'w') as srt_file:
                           srt_file.write(srt_formatted)
                       display_D.set("srt downloaded")
                       messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 6:
                       transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                       formatter = SRTFormatter()
                       srt_formatted = formatter.format_transcript(transcript)
                       srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                       with open(srt_Path_File, 'w') as srt_file:
                           srt_file.write(srt_formatted)
                       display_D.set("srt downloaded")
                       messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 7:
                       transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                       formatter = SRTFormatter()
                       srt_formatted = formatter.format_transcript(transcript)
                       srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                       with open(srt_Path_File, 'w') as srt_file:
                           srt_file.write(srt_formatted)
                       display_D.set("srt downloaded")
                       messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 8:
                       transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                       formatter = SRTFormatter()
                       srt_formatted = formatter.format_transcript(transcript)
                       srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                       with open(srt_Path_File, 'w') as srt_file:
                           srt_file.write(srt_formatted)
                       display_D.set("srt downloaded")
                       messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 9:
                       transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                       formatter = SRTFormatter()
                       srt_formatted = formatter.format_transcript(transcript)
                       srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                       with open(srt_Path_File, 'w') as srt_file:
                           srt_file.write(srt_formatted)
                       display_D.set("srt downloaded")
                       messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    else:
                        error_srt_combo.config("Not part of the options")

                elif (video_resolution_index == 1):
                    yt = YouTube(video_url_youtube.get(),
                                 on_progress_callback=get_Video_bytes,
                                 allow_oauth_cache=True,
                                 use_oauth=False
                                 )
                    yt.streams.filter(only_video=True,res=video_resolution, progressive=True, file_extension="mp4")\
                        .first()\
                        .download(output_path=output_path)

                    display_D.set("video downloaded")
                    messagebox.showinfo(title="KingTube", message="Video downloaded")
                    messagebox.showinfo(title="KingTube", message="Wait for srt to be downloaded")

                    if language_srt_index == 0:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 1:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 2:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 3:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 4:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 5:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 6:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 7:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 8:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 9:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    else:
                        error_srt_combo.config("Not part of the options")

                elif (video_resolution_index == 2):
                    yt = YouTube(video_url_youtube.get(),
                                 on_progress_callback=get_Video_bytes,
                                 allow_oauth_cache=True,
                                 use_oauth=False
                                 )
                    yt.streams.filter(only_video=True,res=video_resolution, progressive=True, file_extension="mp4")\
                        .first()\
                        .download(output_path=output_path)

                    display_D.set("video downloaded")
                    messagebox.showinfo(title="KingTube", message="Video downloaded")
                    messagebox.showinfo(title="KingTube", message="Wait for srt to be downloaded")

                    if language_srt_index == 0:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 1:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 2:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 3:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 4:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 5:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 6:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 7:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 8:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 9:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    else:
                        error_srt_combo.config("Not part of the options")

                elif (video_resolution_index == 3):
                    yt = YouTube(video_url_youtube.get(),
                                 on_progress_callback=get_Video_bytes,
                                 allow_oauth_cache=True,
                                 use_oauth=False
                                 )
                    yt.streams.filter(only_video=True,res=video_resolution, progressive=True, file_extension="mp4")\
                        .first()\
                        .download(output_path=output_path)

                    display_D.set("video downloaded")
                    messagebox.showinfo(title="KingTube", message="Video downloaded")
                    messagebox.showinfo(title="KingTube", message="Wait for srt to be downloaded")

                    if language_srt_index == 0:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 1:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 2:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 3:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 4:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 5:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 6:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 7:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 8:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 9:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    else:
                        error_srt_combo.config("Not part of the options")
                elif (video_resolution_index == 4):
                    yt = YouTube(video_url_youtube.get(),
                                 on_progress_callback=get_Video_bytes,
                                 allow_oauth_cache=True,
                                 use_oauth=False
                                 )
                    yt.streams.filter(only_video=True,res=video_resolution, progressive=True, file_extension="mp4")\
                        .first()\
                        .download(output_path=output_path)

                    display_D.set("video downloaded")
                    messagebox.showinfo(title="KingTube", message="Video downloaded")
                    messagebox.showinfo(title="KingTube", message="Wait for srt to be downloaded")

                    if language_srt_index == 0:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 1:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 2:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 3:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 4:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 5:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 6:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 7:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 8:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 9:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    else:
                        error_srt_combo.config("Not part of the options")
                elif (video_resolution_index == 5):
                    yt = YouTube(video_url_youtube.get(),
                                 on_progress_callback=get_Video_bytes,
                                 allow_oauth_cache=True,
                                 use_oauth=False
                                 )
                    yt.streams.filter(only_video=True,res=video_resolution, progressive=True, file_extension="mp4")\
                        .first()\
                        .download(output_path=output_path)

                    display_D.set("video downloaded")
                    messagebox.showinfo(title="KingTube", message="Video downloaded")
                    messagebox.showinfo(title="KingTube", message="Wait for srt to be downloaded")

                    if language_srt_index == 0:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 1:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 2:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 3:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 4:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 5:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 6:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 7:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 8:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 9:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    else:
                        error_srt_combo.config("Not part of the options")

                else:
                    invalid_res_msg.configure(text="Invalid video resolution")
                    messagebox.showerror(title="KingTube", message="Invalid video resolution")

            else:
                if (video_resolution_index == 0):
                    yt = YouTube(video_url_youtube.get(),
                                 on_progress_callback=get_Video_bytes,
                                 allow_oauth_cache=True,
                                 use_oauth=False
                                 )
                    yt.streams.filter(only_video=True,res=video_resolution, adaptive=True, file_extension="mp4")\
                        .first()\
                        .download(output_path=output_path)

                    display_D.set("video downloaded")
                    messagebox.showinfo(title="KingTube", message="Video downloaded")
                    messagebox.showinfo(title="KingTube", message="Wait for srt to be downloaded")

                    if language_srt_index == 0:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 1:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 2:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 3:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 4:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 5:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 6:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 7:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 8:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 9:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    else:
                        error_srt_combo.config("Not part of the options")
                elif (video_resolution_index == 1):
                    yt = YouTube(video_url_youtube.get(),
                                 on_progress_callback=get_Video_bytes,
                                 allow_oauth_cache=True,
                                 use_oauth=False
                                 )
                    yt.streams.filter(only_video=True,res=video_resolution, adaptive=True, file_extension="mp4")\
                        .first()\
                        .download(output_path=output_path)

                    display_D.set("video downloaded")
                    messagebox.showinfo(title="KingTube", message="Video downloaded")
                    messagebox.showinfo(title="KingTube", message="Wait for srt to be downloaded")

                    if language_srt_index == 0:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 1:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 2:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 3:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 4:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 5:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 6:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 7:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 8:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 9:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    else:
                        error_srt_combo.config("Not part of the options")
                elif (video_resolution_index == 2):
                    yt = YouTube(video_url_youtube.get(),
                                 on_progress_callback=get_Video_bytes,
                                 allow_oauth_cache=True,
                                 use_oauth=False
                                 )
                    yt.streams.filter(only_video=True,res=video_resolution, adaptive=True, file_extension="mp4")\
                        .first()\
                        .download(output_path=output_path)

                    display_D.set("video downloaded")
                    messagebox.showinfo(title="KingTube", message="Video downloaded")
                    messagebox.showinfo(title="KingTube", message="Wait for srt to be downloaded")

                    if language_srt_index == 0:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 1:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 2:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 3:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 4:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 5:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 6:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 7:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 8:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 9:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    else:
                        error_srt_combo.config("Not part of the options")
                elif (video_resolution_index == 3):
                    yt = YouTube(video_url_youtube.get(),
                                 on_progress_callback=get_Video_bytes,
                                 allow_oauth_cache=True,
                                 use_oauth=False
                                 )
                    yt.streams.filter(only_video=True,res=video_resolution, adaptive=True, file_extension="mp4")\
                        .first()\
                        .download(output_path=output_path)

                    display_D.set("video downloaded")
                    messagebox.showinfo(title="KingTube", message="Video downloaded")
                    messagebox.showinfo(title="KingTube", message="Wait for srt to be downloaded")

                    if language_srt_index == 0:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 1:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 2:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 3:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 4:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 5:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 6:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 7:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 8:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 9:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    else:
                        error_srt_combo.config("Not part of the options")
                elif (video_resolution_index == 4):
                    yt = YouTube(video_url_youtube.get(),
                                 on_progress_callback=get_Video_bytes,
                                 allow_oauth_cache=True,
                                 use_oauth=False
                                 )
                    yt.streams.filter(only_video=True,res=video_resolution, adaptive=True, file_extension="mp4")\
                        .first()\
                        .download(output_path=output_path)

                    display_D.set("video downloaded")
                    messagebox.showinfo(title="KingTube", message="Video downloaded")
                    messagebox.showinfo(title="KingTube", message="Wait for srt to be downloaded")

                    if language_srt_index == 0:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 1:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 2:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 3:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 4:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 5:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 6:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 7:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 8:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 9:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    else:
                        error_srt_combo.config("Not part of the options")
                elif (video_resolution_index == 5):
                    yt = YouTube(video_url_youtube.get(),
                                 on_progress_callback=get_Video_bytes,
                                 allow_oauth_cache=True,
                                 use_oauth=False
                                 )
                    yt.streams.filter(only_video=True,res=video_resolution, adaptive=True, file_extension="mp4")\
                        .first()\
                        .download(output_path=output_path)

                    display_D.set("video downloaded")
                    messagebox.showinfo(title="KingTube", message="Video downloaded")
                    messagebox.showinfo(title="KingTube", message="Wait for srt to be downloaded")

                    if language_srt_index == 0:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 1:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 2:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 3:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 4:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 5:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 6:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 7:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 8:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    elif language_srt_index == 9:
                        transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=[language_srt])
                        formatter = SRTFormatter()
                        srt_formatted = formatter.format_transcript(transcript)
                        srt_Path_File = f"{output_path}{srt_file_name.get()}.srt"

                        with open(srt_Path_File, 'w') as srt_file:
                            srt_file.write(srt_formatted)
                        display_D.set("srt downloaded")
                        messagebox.showinfo(title="KingTube", message="Srt downloaded")
                    else:
                        error_srt_combo.config("Not part of the options")
                else:
                    invalid_res_msg.configure(text="Invalid video resolution")
                    messagebox.showerror(title="KingTube", message="Invalid video resolution")
        except Exception as err:
            err_Message_While_Downloading.config(text="error: "+str(err))
            download_progress_bar.stop()
            download_progress_bar["value"] = 0
            display_D.set("")
            window.update_idletasks()
            messagebox.showerror(title="KingTube", message="Error: Download failed")

    new_Thread = threading.Thread(target=start_Download, name="Download_Videos_Running", daemon=True)
    new_Thread.start()


window = tb.Window(themename="superhero")
window.title("KingTube")

#CENTER WINDOW
win_width = 1270
win_height = 700
screen_width = window.winfo_screenwidth()
ycreen_height = window.winfo_screenheight()
x = int((screen_width / 2)-(win_width / 2))
y = int((ycreen_height / 2)-(win_height / 2))
window.geometry("{}x{}+{}+{}".format(win_width, win_height, x, y))

version_number = tb.Label(master=window, text=KingTube_config.version_number,font=("Impact", 15),
                          bootstyle="success")

version_number.place(x=5, y=5)


title = tb.Label(master=window,text="Download Your Youtube Videos",font=("Impact", 38),bootstyle="white")

title.pack()

paste_url = tb.Label(master=window,text="Enter or paste the url of the youtube video",font=("Impact", 23),bootstyle="warning")
paste_url.place(x=10, y=90)

video_url_youtube = tb.Entry(master=window,width=50,foreground="yellow",font=("Aerial", 18),bootstyle="primary")
video_url_youtube.place(x=0, y=150)

choose_Resolution = tb.Label(master=window,text="Choose video resolution",font=("Impact", 17),bootstyle="warning")
choose_Resolution.place(x=660, y=100)

res_combo = tb.Combobox(master=window,bootstyle="white",foreground="white",font=("Aerial", 16),
                        values=KingTube_config.video_resolutions,
                        width=15)
res_combo.place(x=675, y=150)
res_combo.current(0)

invalid_res_msg = tb.Label(master=window,font=("Aerial", 15),bootstyle="danger")
invalid_res_msg.place(x=677, y=200)

vandA_orA_codec = tb.IntVar()

toggle_VA_A_Codec = tb.Checkbutton(bootstyle="primary, round-toggle",
                                   text="off for VandA codec or on for audio codec",
                                   variable=vandA_orA_codec,
                                   onvalue=1,
                                   offvalue=0,
                                   command=getVA_or_A)
toggle_VA_A_Codec.place(x=1000, y=80)

download_Style = tb.Style()
download_Style.configure("success.TButton", font=("Impact",19))

download_Button = tb.Button(master=window, text="Download Video",bootstyle="success",style="success.TButton",
                            width=15,
                            command=download_Youtube_Video)
download_Button.place(x=930, y=150)

output_Video_Location = tb.Label(master=window, text="Enter the destination location of video",
                 font=("Impact", 18),
                 bootstyle="warning")

output_Video_Location.place(x=10, y=200)

output_Video_Location_Entry = tb.Entry(master=window, width=50,foreground="yellow",font=("Aerial", 18),
                             bootstyle="yellow")
output_Video_Location_Entry.place(x=0, y=250)

output_Video_Location_Entry_Msg = tb.Label(master=window,
                         text="Make sure the path slash is double slash not single if it is backslash e.g D:\\\\Video not D:\\Video",
                         font=("Aerial", 15),
                         bootstyle="white")
output_Video_Location_Entry_Msg.place(x=15, y=300)

err_Message_While_Downloading = tb.Label(master=window,font=("Aerial", 15),bootstyle="danger")
err_Message_While_Downloading.place(x=15, y=340)

display_D = tb.StringVar()

download_byte = tb.Label(master=window,textvariable=display_D,font=("Impact", 17),bootstyle="warning")
download_byte.place(x=580, y=560)

srt_label = tb.Label(master=window,text="Enter the subtitle name",font=("Impact", 17),bootstyle="warning")
srt_label.place(x=15, y=380)

srt_file_name = tb.Entry(master=window,width=30,foreground="yellow",font=("Aerial", 18),bootstyle="yellow")
srt_file_name.place(x=0, y=410)

srt_file_name_combo_label = tb.Label(master=window,text="Choose the language for srt file",font=("Impact", 17),bootstyle="warning")
srt_file_name_combo_label.place(x=390, y=380)


srt_file_name_combo = tb.Combobox(master=window, bootstyle="white",foreground="white",
                                  font=("Aerial", 16),
                                  width=10,
                                   values=KingTube_config.language_srt)
srt_file_name_combo.place(x=420, y=410)
srt_file_name_combo.current(0)

srt_file_name_combo_err_msg = tb.Label(master=window,text="",font=("Aerial", 13),bootstyle="danger")
srt_file_name_combo_err_msg.place(x=420, y=460)

srt_label_msg = tb.Label(master=window,text="No ( *, /) is not allowed",font=("Aerial", 15),bootstyle="white")
srt_label_msg.place(x=15, y=470)

download_progress_bar = tb.Progressbar(master=window,maximum=100, value=0)
download_progress_bar.place(x=285, y=500, width=700)

new_Window_Style = tb.Style()
new_Window_Style.configure("primary.TButton", font=("Impact",20))

new_Audio_Window = tb.Button(master=window, text="Download Youtube Audio",bootstyle="primary",
                            style="primary.TButton",
                             command=open_audio)
new_Audio_Window.place(x=215, y=600)

new_Window_Playlist = tb.Button(master=window, text="Open Playlist Window",
                            bootstyle="primary",
                            style="primary.TButton",
                            command=open_playlist)
new_Window_Playlist.place(x=545, y=600)

new_Window_Channel = tb.Button(master=window, text="Open Channel Window",
                            bootstyle="primary",
                            style="primary.TButton",
                            command=open_channel)
new_Window_Channel.place(x=865, y=600)

window.mainloop()
