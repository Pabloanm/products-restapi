'''
Flask, simple REST API 
Use Insomnia or Postman to test endpoints
Methods: GET, POST; PUT, PATCH, DELETE
'''
from flask import Flask, jsonify, request

app = Flask(__name__) #my server app

from products import products #import product list form products.py

@app.route('/ping', methods = ['GET']) #endpoint / GET default method 
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
    #print(product_name) #print in terminal
    productsFound = [product for product in products if product['name'] == product_name]
    #return 'received' #print in browser
    if (len(productsFound)>0):
        return jsonify({"product": productsFound[0]}) #return Found value 
    return jsonify({"message": "Product not found"}) 

@app.route('/products', methods = ['POST'])
def addProduct():
    #print(request.json) #http request
    '''
    Test endpoint http://127.0.0.1:4000/products
    {
	"name": "mouse gaming",
	"price": 45.99,
	"quantity": 2
    }
    '''
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "Product Added Succesfully", "prodcuts": products})

    
@app.route('/products/<string:product_name>', methods = ['PUT'])
def editProduct(product_name):
    '''
    Test endpoint http://127.0.0.1:4000/products/monitor
    {
	"name": "TV",
	"price": 600,
	"quantity": 50
    }
    '''
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound)>0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Product Updated",
            "product": productFound[0]            
        })
    return jsonify({"message":"Product Not found"})

@app.route('/products/<string:product_name>', methods = ['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0]) #objet found to delete
        return jsonify({
            "message": "Product Deleted",
            "products": products
        })
    return jsonify({"message": "Product Not found"})

if __name__ == '__main__':
    app.run(debug=True, port=4000) #python app.py to run this server

