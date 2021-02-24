from flask import Flask, render_template

templateDir = 'templates'

# __name__ : Name of the python script
# 
app = Flask(__name__)

@app.route('/about')
def about():
    # * Default to be under 'templates' directory
    return render_template('about.html')

@app.route('/')
def home():
    # * Default to be under 'templates' directory
    return render_template('home.html')

# Case 1: if script is being imported : __name__ = 'script1'
# Case 2: if script is being executed : __name__ = '__main__'
if __name__ == '__main__':
    app.run(debug=True)