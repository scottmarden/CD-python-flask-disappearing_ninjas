from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def ninja():
	return render_template('ninja.html')

@app.route('/ninja/<ninja_color>')
def ninja_color(ninja_color):
	color = ninja_color
	print color
	if color == "blue":
		image = "src=/static/images/leonardo.jpg alt=Leo!!"
	elif color == "purple":
		image = "src=/static/images/donatello.jpg alt=Donnie!!"
	elif color == "orange":
		image = "src=/static/images/michelangelo.jpg alt=Mikie!!!"
	elif color == "red":
		image = "src=/static/images/raphael.jpg alt=Raph!!"
	else:
		image = "src=/static/images/notapril.jpg alt=Nope!!"
	return render_template('ninja_color.html', image=image)


app.run(debug = True)
