#/usr/bin/python3
from flask import *

app = Flask(__name__, template_folder="./")

@app.route("/")
def index():
	title = "Index Page"
	content = "Do you want to visit test page?"
	return render_template("index.html", title=title, content=content)

@app.route("/test", methods=['GET'])
def test():
	name = request.args.get("name")
	if name == None:
		return redirect(f'{url_for("test")}?name=guest')
	htmldoc = f"""
	<html>
	<body>
	<h1>Hello</h1>
	<a>Nice to see you {name}</a>
	</body>
	</html>
	"""
	return render_template_string(htmldoc)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
