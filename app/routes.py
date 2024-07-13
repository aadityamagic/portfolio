from flask import render_template, current_app as app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/og-portfolio')
def og_portfolio():
    return render_template('og_portfolio.html')

@app.route('/modern-portfolio')
def modern_portfolio():
    return render_template('modern_portfolio.html')