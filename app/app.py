from flask import Flask, render_template, request
from diff_match_patch import diff_match_patch

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare_text():
    text_a = request.form['text_a']
    text_b = request.form['text_b']
    
    dmp = diff_match_patch()
    diffs = dmp.diff_main(text_a, text_b)
    dmp.diff_cleanupSemantic(diffs)
    html_diffs = dmp.diff_prettyHtml(diffs)
    
    return render_template('result.html', html_diffs=html_diffs)

@app.route('/user_agreements')
def user_agreements():
    return render_template('user_agreements.html')

if __name__ == '__main__':
    app.run(debug=True)