from flask import Flask, render_template

app = Flask(__name__)

@app.route("/data_to")
def data_to():
  some_pars = {'user':'Ivan','color':'red'}
  some_str = 'Hello my dear friends!'
  some_value = 10

  return render_template('simple.html', some_str = some_str,
	 some_value = some_value, some_pars = some_pars)
