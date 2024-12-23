from flask import Flask, jsonify
from flask_cors import CORS
from db_connection import Database

app = Flask(__name__)
# CORS(app, origins=["http://localhost:4200"])  # Permite 
# solicitudes desde Angular

CORS(app, origins=["*"])  # Permite solicitudes desde cualquier origen

print('ejecutando la aplicación')
# Instancia de la base de datos
db = Database()

@app.route('/', methods=['GET'])
def ping():
    return jsonify({"response": "app running...para probar railways"})

# Ruta para obtener los materiales
@app.route('/materiales', methods=['GET'])
def get_materiales():
    materiales = db.get_materiales()
    return jsonify(materiales)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)