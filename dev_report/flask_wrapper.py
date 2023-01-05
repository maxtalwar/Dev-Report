import requests

def update_progress(new_value):
    response = requests.post('http://localhost:5000/update_progress', data={'new_value': str(new_value)+"%"})

def update_row(new_value):
    response = requests.post('http://localhost:5000/update_row', data={'new_value': new_value})

def update_link(new_value):
    response = requests.post('http://localhost:5000/update_link', data={'new_value': new_value})

def update_function(new_value):
    response = requests.post('http://localhost:5000/update_function', data={'new_value': new_value})

def update_starttime(new_value):
    response = requests.post('http://localhost:5000/update_starttime', data={'new_value': new_value})