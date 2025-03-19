<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VidSnatcher 🎥 - Video Downloader</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #121212;
            color: #ffffff;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
        }
        h1, h2 {
            text-align: center;
            color: #ffcc00;
        }
        .features, .installation, .usage, .dependencies, .acknowledgments {
            background: #1e1e1e;
            padding: 20px;
            margin: 10px 0;
            border-radius: 8px;
        }
        pre {
            background: #333;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            color: #ffcc00;
        }
        .screenshot, .screencast {
            display: flex;
            justify-content: center;
            margin: 20px 0;
        }
        img, video {
            max-width: 100%;
            border-radius: 8px;
        }
        .copy-btn {
            background: #ffcc00;
            color: #121212;
            padding: 5px 10px;
            border: none;
            cursor: pointer;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>VidSnatcher 🎥</h1>
        <p>A powerful and user-friendly video downloader built using <strong>Streamlit</strong> and <strong>yt_dlp</strong>. With VidSnatcher, you can effortlessly download videos from various online platforms.</p>
        
        <div class="screenshot">
            <img src="https://github.com/user-attachments/assets/fc173b0b-9298-473a-b965-1556afc3f6af" alt="VidSnatcher Screenshot">
        </div>

        <h2>Features</h2>
        <div class="features">
            <ul>
                <li><strong>Download Videos:</strong> Supports a wide range of online platforms.</li>
                <li><strong>Video Quality Options:</strong> 1080p, 720p, 480p, 360p, 240p, etc.</li>
                <li><strong>Progress Tracking:</strong> Real-time progress bar with speed tracking.</li>
                <li><strong>Cross-Platform:</strong> Works on Windows, macOS, Linux, and Android.</li>
            </ul>
        </div>
        
        <h2>Installation</h2>
        <div class="installation">
            <p>Ensure you have Python installed, then run the following commands:</p>
            <pre><code>git clone &lt;repository-url&gt;
cd &lt;repository-directory&gt;
pip install -r requirements.txt</code></pre>
        </div>
        
        <h2>How to Use</h2>
        <div class="usage">
            <p>Launch the application with:</p>
            <pre><code>streamlit run app.py</code></pre>
            <p>Steps:</p>
            <ol>
                <li>Open the app in your browser.</li>
                <li>Enter the video URL.</li>
                <li>Select video quality.</li>
                <li>Click "Fetch Video Details" to see video metadata.</li>
                <li>Click "Download Video" to start downloading.</li>
            </ol>
        </div>
        
        <div class="screencast">
            <video controls>
                <source src="https://github.com/user-attachments/assets/21c8d3ab-2137-44d0-9c6e-10c1d41b748d" type="video/webm">
                Your browser does not support the video tag.
            </video>
        </div>
        
        <h2>Dependencies</h2>
        <div class="dependencies">
            <ul>
                <li><strong>Streamlit:</strong> Web app framework for Python.</li>
                <li><strong>yt-dlp:</strong> Video downloading library.</li>
            </ul>
        </div>
        
        <h2>Acknowledgments</h2>
        <div class="acknowledgments">
            <p>Thanks to <strong>Streamlit</strong> and <strong>yt-dlp</strong> for making this project possible.</p>
        </div>
    </div>
</body>
</html>
