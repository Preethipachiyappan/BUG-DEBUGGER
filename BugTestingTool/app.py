from flask import Flask, request, render_template
import autopep8

app = Flask(__name__)
@app.route('/')
def upload_page():
    return render_template('upload.html')

@app.route('/fix', methods=['POST'])
def fix_code():
    if 'file' not in request.files:
        return "No file uploaded", 400
    file = request.files['file']
    code = file.read().decode('utf-8')
    
    fixed_code = autopep8.fix_code(code)  

    return render_template('result.html', fixed_code=fixed_code)

if __name__ == '__main__':
    app.run(debug=True)
