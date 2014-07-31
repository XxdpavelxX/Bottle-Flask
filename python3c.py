from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/echo/')
def echo():
    kwargs = {}
    kwargs['thing'] = request.args.get('thing')
    kwargs['place'] = request.args.get('place')
    return render_template('flask3.html', **kwargs)
	
@app.route('/ufc/')
def ufc():
	kwargs = {}
	#select name from persons where age=17
	name='David'
	kwargs['name'] = name
	return render_template('ufc.html', **kwargs)


app.run(port=9999, debug=True)