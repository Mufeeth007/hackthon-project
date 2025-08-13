from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__, static_folder='.', template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        name = request.form.get('name')
        details = request.form.get('details')
        academic = request.form.get('academic')
        skills = request.form.get('skills')
        interests = request.form.get('interests')
        return f"""
        <h2>Profile Submitted</h2>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Details:</strong> {details}</p>
        <p><strong>Academic Info:</strong> {academic}</p>
        <p><strong>Skills:</strong> {skills}</p>
        <p><strong>Interests:</strong> {interests}</p>
        <a href='/'>Back to Login</a>
        """
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
