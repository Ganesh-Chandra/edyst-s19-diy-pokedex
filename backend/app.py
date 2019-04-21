from flask import *
import ast
app=Flask(__name__)
@app.errorhandler(404)
def errfun(e):
    return render_template("404.html"),404
@app.route('/api/pokemon/<int:id>')
def fun(id):
    if(id<1 or id>151):
        return render_template("404.html"),404
    f=open("backend/data.txt",'r')
    data=f.read()
    data=ast.literal_eval(data)
    data=data[id]
    data={'id':data[0],'name':data[1],'sprites':data[2]}
    res=jsonify(pokemon=data)
    return res
if __name__ == "__main__":
    app.run(port=8006,debug=True)