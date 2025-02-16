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

def get_download_folder():
    if os.name == 'nt':  # Windows
        return os.path.join(os.environ['USERPROFILE'], 'Downloads')
    elif os.name == 'posix':
        if 'ANDROID_DATA' in os.environ:  # Android
            return '/storage/emulated/0/Download'
        else:  # macOS and Linux
            return os.path.join(Path.home(), 'Downloads')
    else:
        return os.getcwd()  # Default to current working directory if unknown OS

def fetch_video_details(url):
    try:
        ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'merge_output_format': 'mp4',
    'outtmpl': os.path.join(download_folder, f'{video_title}.%(ext)s'),
    'progress_hooks': [progress_hook],
    'concurrent_fragment_downloads': 4,
}

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', None)
            video_views = info_dict.get('view_count', None)
            video_length = info_dict.get('duration', None)
            video_size_bytes = info_dict.get('filesize', None)

            video_details = {
                'title': video_title,
                'views': video_views,
                'length': video_length,
                'size_bytes': video_size_bytes
            }

            return video_details
    except yt_dlp.utils.DownloadError as e:
        st.error('An error occurred while fetching video details!')
        st.error(e)
        return None
    except Exception as e:
        st.error('An unexpected error occurred!')
        st.error(e)
        return None

def download_video(url, video_title):
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

        download_folder = get_download_folder()
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(download_folder, f'{video_title}.%(ext)s'),
            'progress_hooks': [progress_hook],
            'concurrent_fragment_downloads': 4  # Number of concurrent connections
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        video_path = os.path.join(download_folder, f'{video_title}.mp4')
        st.success('Video downloaded successfully! Check your Downloads folder.')
        st.balloons()

        return video_path
    except yt_dlp.utils.DownloadError as e:
        st.error('An error occurred while downloading the video!')
        st.error(e)
    except Exception as e:
        st.error('An unexpected error occurred!')
        st.error(e)

    return None

st.title('🎥 VidSnatcher')
st.markdown('Download any Online Video from a Link! 😱')
st.markdown('Made with love 💖🎥 by Ephraim Maina. [GitHub Account](https://github.com/cybercypherdev/cybercypherdev)')

url = st.text_input('Enter Video URL:', '')

if url:
    st.video(url)

    with st.spinner("Fetching video details..."):
        video_details = fetch_video_details(url)

    if video_details:
        if video_details['size_bytes']:
            size_mbs = video_details['size_bytes'] / 1048576
            st.write(f'Size: {size_mbs:.2f} MB')
        else:
            st.write('Size: Unknown')

        st.write(f'**Title:** {video_details["title"]}')
        st.write(f'**Views:** {video_details["views"]}')
        st.write(f'**Length:** {video_details["length"] / 60:.2f} minutes')

        if st.button('Download Video'):
            video_path = download_video(url, video_details['title'])
            if video_path:
                with open(video_path, 'rb') as file:
                    st.download_button('Save on Local Storage', file, file_name=f'{video_details["title"]}.mp4')
