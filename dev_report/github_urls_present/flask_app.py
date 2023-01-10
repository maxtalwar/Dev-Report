from flask import Flask, request, render_template

app = Flask(__name__)

# Initialize the variables with some default values
progress = "0%"
row = "n/a"
link = "n/a"
function = "n/a"
start_time = "n/a"

@app.route('/update_progress', methods=['POST'])
def update_progress():
    global progress
    new_value = request.form['new_value']
    progress = new_value
    return "progress updated successfully"

@app.route('/update_row', methods=['POST'])
def update_row():
    global row
    new_value = request.form['new_value']
    row = new_value
    return "row updated successfully"

@app.route('/update_link', methods=['POST'])
def update_link():
    global link
    new_value = request.form['new_value']
    link = new_value
    return "link updated successfully"

@app.route('/update_function', methods=['POST'])
def update_function():
    global function
    new_value = request.form['new_value']
    function = new_value
    return "function updated successfully"

@app.route('/update_starttime', methods=['POST'])
def update_starttime():
    global start_time
    new_value = request.form['new_value']
    start_time = new_value
    return "start time updated successfully"

@app.route('/display_variables')
def display_variables():
    return f"Progress: {progress}\nRow: {row}\nLink: {link}\nFunction: {function}\nStart Time: {start_time}"

@app.route('/')
def index():
    rendered = render_template('index.html', progress=progress, row=row, link=link, function=function, start_time=start_time)
    return rendered

if __name__ == "__main__":
    app.run(debug=True)