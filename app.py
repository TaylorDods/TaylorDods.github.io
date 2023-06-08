from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='.')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/qualifications')
def qualifications():
    return render_template('qualifications.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/LLM_File_Integration')
def LLM_File_Integration():
    return render_template('LLM_File_Integration.html')

@app.route('/Shell_Eco_Chassis')
def Shell_Eco_Chassis():
    return render_template('Shell_Eco_Chassis.html')

@app.route('/BB_Together')
def BB_Together():
    return render_template('BB_Together.html')

if __name__ == '__main__':
    app.run(debug=True)