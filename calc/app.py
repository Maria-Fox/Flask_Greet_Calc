# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask (__name__) 

# -----------------------------------------------------

@app.route("/form")
def form():
  '''Template html for form submission'''

  form_html = '''
  <form>
  <h1> Submit Values to add A and B </h1>
  <input type = "text" name = "a" placeholder = "Value for A">
  <input type = "text" name = "b" placeholder = "Value for B">
  <button type="submit"> Submit </button>
  </form>
  '''
  return form_html

# -----------------------------------------------------

@app.route("/add", methods=["GET"])
def additiona():
  '''Add values a and B'''

  a = int(request.args("a"))
  b = int(request.args("b"))

  result = add(a,b)
  return str(result) 

# -----------------------------------------------------

@app.route("/sub", methods=["GET"])
def additiona():
  '''Subtract b from a'''

  a = int(request.args("a"))
  b = int(request.args("b"))

  result = sub(a,b)
  return str(result)

# -----------------------------------------------------

@app.route("/mult", methods=["GET"])
def additiona():
  '''Multiply a & b'''

  a = int(request.args("a"))
  b = int(request.args("b"))

  result = mult(a,b)
  return str(result)

# -----------------------------------------------------

@app.route("/div", methods=["GET"])
def additiona():
  '''Divide a by b'''

  a = int(request.args("a"))
  b = int(request.args("b"))

  result = div(a,b)
  return str(result)


# operators = {
#     "add": add,
#     "sub": sub,
#     "mult": mult,
#     "div": div,
# }

# @app.route("/math/<oper>")
# def do_math(oper):
#     """Do math on a and b."""

#     a_val = int(request.args.get("a-value"))
#     b_val = int(request.args.get("b-value"))
#     result = operators[oper](a, b)

#     return str(result)
