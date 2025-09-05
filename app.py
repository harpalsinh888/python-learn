from flask import Flask, render_template_string, request
import requests

app = Flask(_name_)

# 🔹 Replace with your RapidAPI Key
RAPIDAPI_KEY = "YOUR_RAPIDAPI_KEY"
API_URL = "https://instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com/?url="

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Instagram Reel Downloader</title>
  <style>
    body { font-family: Arial; background:#f5f5f5; text-align:center; padding:20px; }
    input { padding:10px; width:60%; margin:10px 0; }
    button { padding:10px 20px; background:#007bff; color:white; border:none; cursor:pointer; }
    video { margin-top:20px; width:60%; }
  </style>
</head>
<body>
  <h1>📥 Instagram Reel Downloader</h1>
  <form method="POST">
    <input type="text" name="url" placeholder="Paste Instagram Reel Link" required>
    <br>
    <button type="submit">Download</button>
  </form>
  {% if error %}<p style="color:red;">{{ error }}</p>{% endif %}
  {% if video_url %}
    <h2>Preview</h2>
    <video controls>
      <source src="{{ video_url }}" type="video/mp4">
    </video>
    <p><a href="{{ video_url }}" download>Download Video</a></p>
  {% endif %}
</body>
</html>
"""

def get_instagram_video(url):
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com"
    }
    try:
        res = requests.get(API_URL + url, headers=headers)
        data = res.json()
        return data.get("media")
    except Exception:
        return None

@app.route("/", methods=["GET", "POST"])
def home():
    video_url = None
    error = None
    if request.method == "POST":
        link = request.form.get("url")
        video_url = get_instagram_video(link)
        if not video_url:
            error = "❌ Unable to fetch video. Check link or API key."
    return render_template_string(HTML, video_url=video_url, error=error)

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)

