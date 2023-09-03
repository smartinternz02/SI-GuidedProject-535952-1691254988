from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template(r"index.html")

@app.route('/dashboard')
def dashboard():
    return render_template(r'dashboard.html')

@app.route('/story')
def story():
    return render_template(r'story.html')

@app.route('/report')
def report():
    return render_template(r'report.html')

if __name__ == '__main__':
    app.run(debug=False, port=5000)