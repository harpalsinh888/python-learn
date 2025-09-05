from flask import Flask, render_template, request
import instaloader

app = Flask(__name__)
L = instaloader.Instaloader()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    if not url or "instagram.com" not in url:
        return "❌ Please enter a valid Instagram Reel URL!"

    try:
        shortcode = url.split("/")[-2]  # Reel ID extract karo
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        if post.is_video:
            video_url = post.video_url
            return f'<h2>✅ Video Found!</h2><a href="{video_url}" target="_blank">📥 Download Now</a>'
        else:
            return "❌ This is not a reel or video!"
    except Exception as e:
        return f"❌ Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)

