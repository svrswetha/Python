from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

if __name__=="__main__":
  print "i am running as an independent program"
  app.run()
else:
  print "i am running as an imported module"
