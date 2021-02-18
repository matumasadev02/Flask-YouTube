from Flask import *
@app.route("/"):
	def helloworld():
		return("Hello,World")
