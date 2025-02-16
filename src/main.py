import streamlit as st
import yt_dlp
import time
import os
from pathlib import Path

# Set page configuration
st.set_page_config(
    page_title="VidSnatcher",
    page_icon="🎥",
    layout="centered",
    initial_sidebar_state="expanded",
)

video_title = ""
video_views = ""
video_length = ""
video_size_bytes = ""

def fetch_video_details(url, quality):
    global video_title, video_views, video_length, video_size_bytes
    try:
        ydl_opts = {
            'format': quality,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', None)
            video_views = info_dict.get('view_count', None)
            video_length = info_dict.get('duration', None)
            video_size_bytes = info_dict.get('filesize', None)

            if video_size_bytes:
                video_size_mbs = video_size_bytes / 1048576
                st.write(f'Size: {video_size_mbs:.2f} MB')
            else:
                st.write('Size: Unknown')

            st.write(f'**Title:** {video_title}')
            st.write(f'**Views:** {video_views}')
            st.write(f'**Length:** {video_length / 60:.2f} minutes')
    except yt_dlp.utils.DownloadError as e:
        st.error('An error occurred while fetching video details!')
        st.error(e)
        # Display available formats
        st.write("Available formats:")
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])
            for f in formats:
                st.write(f"Format code: {f['format_id']}, Extension: {f['ext']}, Resolution: {f.get('resolution', 'N/A')}")
    except Exception as e:
        st.error('An unexpected error occurred!')
        st.error(e)

def download_video(url, quality):
    global video_title, video_views, video_length, video_size_bytes
    try:
        progress_bar = st.progress(0)
        status_text = st.empty()
        speed_text = st.empty()
        start_time = time.time()

        def progress_hook(d):
            if d['status'] == 'downloading':
                downloaded_bytes = d.get('downloaded_bytes', 0)
                total_bytes = d.get('total_bytes', 1)
                if total_bytes is not None:
                    progress_percentage = downloaded_bytes / total_bytes
                    progress_bar.progress(progress_percentage)
                    status_text.text(f"Progress: {progress_percentage:.2%}")

                    elapsed_time = time.time() - start_time
                    download_speed = downloaded_bytes / (elapsed_time * 1024)  # in KB/s
                    speed_text.text(f"Speed: {download_speed:.2f} KB/s")

        download_folder = "./downloads"
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        ydl_opts = {
            'format': quality,
            'outtmpl': os.path.join(download_folder, f'{video_title}.%(ext)s'),
            'progress_hooks': [progress_hook],
            'concurrent_fragment_downloads': 4  # Number of concurrent connections
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        st.success('Video downloaded successfully! Check your Downloads folder.')
        st.balloons()

        video_file_path = os.path.join(download_folder, f'{video_title}.mp4')
        if os.path.exists(video_file_path):
            with open(video_file_path, "rb") as file:
                btn = st.download_button(
                    label="Save to Local Storage",
                    data=file,
                    file_name=f"{video_title}.mp4",
                    mime="video/mp4"
                )
                if btn:
                    st.experimental_rerun()  # Automatically trigger the download button
    except yt_dlp.utils.DownloadError as e:
        st.error('An error occurred while downloading the video!')
        st.error(e)
    except Exception as e:
        st.error('An unexpected error occurred!')
        st.error(e)

st.title('🎥 VidSnatcher')
st.markdown('Download any Online Video from a Link! 😱')
st.markdown('Made with love 💖🎥 by Ephraim Maina. [GitHub Account](https://github.com/cybercypherdev/cybercypherdev)')

url = st.text_input('Enter Video URL:', '')

if url:
    st.video(url)
    quality = st.selectbox('Select Video Quality:', ['best', 'worst', 'bestvideo', 'bestaudio','worstaudio'])
    with st.spinner("Fetching video details..."):
        fetch_video_details(url, quality)
    if st.button('Download Video'):
        download_video(url, quality)
