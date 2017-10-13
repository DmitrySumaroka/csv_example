from app import app
from flask import Flask, render_template, redirect, url_for, request
import json
import csv
import io
from .forms import SampleForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/upload', methods=['GET', 'POST'])
def home():
    filename = "None right now"
    lines = []
    if request.method == 'POST':
        print(request.data)
        if "file" not in request.files:
            print("No file")
            return render_template('upload.html')
        filename = request.files["file"].filename
        file_contents = io.StringIO(request.files["file"].stream.read().decode("UTF8"), newline=None)
        csv_contents = csv.reader(file_contents)
        for line in csv_contents:
            lines.append(line)

    """
        /home will go to after the user is logged in

        Returns
        -------
        home.html : template
    """
    return render_template('upload.html', filename=filename, contents=lines, url=url_for("upload_table"))

@app.route('/upload-table', methods=['POST'])
def upload_table():
    # my_form = SampleForm.SampleForm()
    if request.method == "POST":
        print(request.data)

    """
        /home will go to after the user is logged in

        Returns
        -------
        home.html : template
    """
    return redirect(url_for("home"))