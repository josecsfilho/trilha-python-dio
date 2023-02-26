import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Ler a planilha JSON e armazenar os dados em uma lista de dicionários
df = pd.read_json('/content/dados.json')
dados = df.to_dict('records')

# Endpoint para retornar todos os dados da planilha
@app.route('/dados', methods=['GET'])
def get_dados():
    return jsonify(dados)

# Endpoint para retornar os dados de um registro específico com base no valor da coluna "Number"
@app.route('/dados/<int:number>', methods=['GET'])
def get_dados_by_number(number):
    for dado in dados:
        if dado['Number'] == number:
            return jsonify(dado)
    return jsonify({'message': 'Dado não encontrado'})

# Endpoint para retornar os dados de um conjunto de registros com base no valor da coluna "City"
@app.route('/dados/city/<city>', methods=['GET'])
def get_dados_by_city(city):
    result = [dado for dado in dados if dado['City'].lower() == city.lower()]
    return jsonify(result)

if __name__ == '__main__':
    app.run()
