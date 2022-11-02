'''Flask'''
from flask import Flask

app = Flask(__name__) #my server app

from products import products #import product list form products.py

@app.route('/ping') #endpoint
def ping(): 
    return "Follow The White Rabbit"

if __name__ == '__main__':
    app.run(debug=True, port=4000) #python app.py to run this server

