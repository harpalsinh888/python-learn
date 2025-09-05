from flask import Flask, request, render_template_string
import instaloader

app = Flask(_name_)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Instagram Reel Downloader</title>
</head>
<body>
    <h1>Download Instagram Reel</h1>
    <form method="POST">
        <input type="text" name="url" placeholder="Enter Instagram Reel URL" required>
        <button type="submit">Download</button>
    </form>
    {% if error %}<p style="color:red;">{{ error }}</p>{% endif %}
    {% if message %}<p>{{ message }}</p>{% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    message = None
    if request.method == "POST":
        url = request.form.get("url")
        try:
            loader = instaloader.Instaloader()
            post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])
            loader.download_post(post, target="downloads")
            message = "Reel downloaded successfully to 'downloads/' folder!"
        except Exception as e:
            error = str(e)
    return render_template_string(HTML, error=error, message=message)

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
