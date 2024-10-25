from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/play/<video_id>')
def play(video_id):
    return render_template('play.html', video_id=video_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))