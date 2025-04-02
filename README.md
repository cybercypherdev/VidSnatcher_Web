VidSnatcher 🎥
VidSnatcher is a powerful and user-friendly video downloader built using Streamlit and yt_dlp. With VidSnatcher, you can effortlessly download videos from a variety of online platforms.

The site is live at https://vidsnatcher.streamlit.app/


![Screenshot from 2025-02-16 17-25-01](https://github.com/user-attachments/assets/fc173b0b-9298-473a-b965-1556afc3f6af)

Features
Download Videos: Download videos from a wide range of online platforms supported by yt_dlp.

Video Quality Options: Choose from multiple video quality options including best, worst, 1080p, 720p, 480p, 360p, and 240p.

Progress Tracking: Track download progress and speed with a real-time progress bar.

Cross-Platform Compatibility: Compatible with Windows, macOS, Linux, and Android.

Installation
To get started, you need to have Python installed on your system. Clone this repository and install the required dependencies:

bash
git clone <repository-url>
cd <repository-directory>
pip install -r requirements.txt
How to Use
Launch the Application: Run the Streamlit application using the following command:

bash
streamlit run app.py
Enter Video URL: Open the application in your browser and enter the URL of the video you want to download.

Select Video Quality: Choose your preferred video quality from the dropdown menu.

Fetch Video Details: Click the "Fetch Video Details" button to view details about the video such as title, views, length, and size.

Download Video: Click the "Download Video" button to start downloading the video. You can track the download progress and speed.


[Screencast from 2025-02-16 17-20-35.webm](https://github.com/user-attachments/assets/21c8d3ab-2137-44d0-9c6e-10c1d41b748d)

Code Overview
Streamlit Setup
The app.py script sets up the Streamlit application with a title, icon, layout, and sidebar state.

Functions
get_download_folder(): Determines the default download folder path based on the operating system.

fetch_video_details(url, quality): Fetches video details like title, views, length, and size without downloading the video.

download_video(url, quality): Downloads the video from the provided URL and displays a progress bar along with download speed.

Main Application
Displays an input field for the video URL.

Shows the video using st.video().

Allows users to select video quality.

Fetches and displays video details when a URL is provided.

Downloads the video when the "Download Video" button is clicked.

Dependencies
streamlit: Streamlit framework for creating the web application.

yt_dlp: Library for downloading videos from various online platforms.

Acknowledgments
Streamlit

yt-dlp
