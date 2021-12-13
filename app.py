from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/portfolio-details.html')
def portfolio():
    return render_template('portfolio-details.html')

app.add_url_rule("/index.html", view_func=index_page)

if __name__=="__main__":
    app.run(debug=True)