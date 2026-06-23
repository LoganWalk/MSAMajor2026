import flask 
from flask import request,jsonify
import student_generator_v2 as sg

app = flask.Flask(__name__)

app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def index():
    return "<h1>Student Data API</h1>"


def search_dicotnary_list(search_key, search_value):
    search_list = []
    for student in sg.get_student_dictonaries():
        if student[search_key] == search_value:
            search_list.append(student)
    return search_list



@app.route('/api/students/all', methods=['GET'])
def api_all():
    student_dictionaries = sg.get_student_dictonaries()
    return jsonify(student_dictionaries)

app.run(debug = True)