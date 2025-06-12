import yt_dlp
import os

# Folder where videos will be saved
SAVE_FOLDER = "PATH TO YOUR DESIRED FOLDER"  # Change this to your desired path
os.makedirs(SAVE_FOLDER, exist_ok=True)  # Create the folder if it doesn't exist

# Updated YouTube Shorts links
urls = [
    
"enter the youtube shorts url here"

# Note: if you want to add multiple links 
# just add comma(,) after each lins 


]

# Download each video one by one to maintain sequence
for index, url in enumerate(urls, start=1):
    ydl_opts = {
        "format": "mp4",  # Download in MP4 format
        "outtmpl": os.path.join(SAVE_FOLDER, f"{index:02d}_%(title)s.%(ext)s"),  # Use two-digit index for clear sequence
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  # Download one video at a time

    print(f"Downloaded {index}/{len(urls)}: {url}")

print("All videos downloaded in sequence!")
