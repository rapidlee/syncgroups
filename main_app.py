# pylot - Johnny Lee
from flask import Flask, render_template, request
from testapp import test_domain_input, find_pattern
app = Flask(__name__)



@app.route('/')
def my_form():
    return render_template('my-form.html')

# fetch input, then pass vars to html and process
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['some_input']
    final_input = test_domain_input(text)
    final_output = find_pattern(final_input)
    return render_template('my-form-processed.html', final_output=final_output, final_input=final_input)

if __name__ == "__main__":
      app.run(debug=True)
 
