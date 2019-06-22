# pylot - Johnny Lee
from flask import Flask, render_template, request
from testapp import test_domain_input, find_pattern, find_dept, get_file_lastmod_date
app = Flask(__name__)

@app.route('/')
def my_form():
    file_last_modified = get_file_lastmod_date()
    return render_template('my-form.html', file_last_modified=file_last_modified)

# fetch input, then pass vars to html and process
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['some_input']
    final_input = test_domain_input(text)
    final_output = find_pattern(final_input)
    dept_output = find_dept(final_input)  
    return render_template('my-form-processed.html', final_output=final_output, final_input=final_input, dept_output=dept_output)

# read from open_grok.txt file and display it on screen
@app.route('/repo_content')
def read_file_contents():
    with open('open_grok.txt', 'r') as f:
        contents = f.read()
    return render_template('repo_content.html', contents=contents)


@app.route('/write_to_file')
def write_to_file():
    return render_template('write_to_file.html')

# write to the open_grok.txt file 
@app.route('/write_to_file', methods=['GET', 'POST'])
def write_to_file_post():
    # with open('open_grok.txt', 'w') as f:      
    new_content = request.form['file_contents']
    if request.method == 'POST':
        with open('open_grok.txt', 'w') as f:
            f.write(f"{new_content}")    
    return render_template('write_to_file_success.html', new_content=new_content)

      
      

if __name__ == "__main__":
      app.run(host='0.0.0.0', port=5005, debug=True)
 
