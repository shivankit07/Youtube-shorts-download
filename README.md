
# 🎬 YouTube Shorts Downloader (Sequential)

This Python script downloads a list of YouTube Shorts videos in **sequence**, saving each video with a filename that includes its order number and original title. It uses [`yt-dlp`](https://github.com/yt-dlp/yt-dlp), a powerful YouTube downloader forked from `youtube-dl`.

---

## 📁 Features

- Downloads **YouTube Shorts** videos in MP4 format.
- Videos are saved in a specified folder.
- Each video is saved with a filename like `01_Title.mp4`, `02_Title.mp4`, etc.
- Ensures proper download sequence.

---

## 📦 Requirements

- Python 3.7+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)

### 🔧 Installation

```bash
pip install yt-dlp
```

---

## 🧠 Usage

1. Clone this repository or copy the script.
2. Modify the following in the script:
   - `SAVE_FOLDER` — the destination folder on your system.
   - `urls` — replace the placeholder with your list of YouTube Shorts URLs.

```python
urls = [
    "https://www.youtube.com/shorts/abc123",
    "https://www.youtube.com/shorts/xyz456",
    # Add more Shorts URLs here
]
```

3. Run the script:

```bash
python download_shorts.py
```

---

## 📂 Output Example

If you download 3 videos, you will get:

```
/your/folder/path/
├── 01_First_Short_Title.mp4
├── 02_Second_Short_Title.mp4
├── 03_Third_Short_Title.mp4
```

---

## 🚨 Notes

- Make sure the destination path (`SAVE_FOLDER`) exists or is writeable by the script.
- yt-dlp handles downloading and video metadata parsing.
- This is for educational and personal use only. Please respect YouTube's [Terms of Service](https://www.youtube.com/t/terms).

---

## 🛠️ Troubleshooting

- **Permission denied?** Try running the script with elevated privileges or choose a different folder.
- **Video unavailable or private?** Ensure the URLs are accessible publicly.
- **Unsupported URL?** Make sure you’re using **YouTube Shorts** links (format: `https://www.youtube.com/shorts/<ID>`).

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Credits

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — core downloading functionality
