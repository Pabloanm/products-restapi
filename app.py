'''Flask'''
from flask import Flask, jsonify

app = Flask(__name__) #my server app

from products import products #import product list form products.py

@app.route('/ping', methods=['GET']) #endpoint / GET default method 
def ping(): 
    #return "Follow The White Rabbit"
    return jsonify({"message":"pong!"})

@app.route('/products') #GET default method 
def getProducts():
    #return jsonify(products)
    #return jsonify({"products":products})
    return jsonify({"products":products, "message": "Product's List"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    print(product_name) #print in terminal
    return 'received' #print in browser


if __name__ == '__main__':
    app.run(debug=True, port=4000) #python app.py to run this server

