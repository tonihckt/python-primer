from flask import Flask
#from gevent.pywsgi import WSGIServer

#instanciamos 
# primer parametro del consructor nombre del modulo
app = Flask(__name__)

#generamos una ruta
@app.route('/')

#definimos una funcion
def helloWorld():
    return 'Hola, mundo'


#generamos un punto de entrada
if __name__ == "__main__":

    # Debug/Development
    app.run(debug=True)
    
    app.run()
