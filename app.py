from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/investigaciones', methods=['GET'])
def obtener_investigaciones():
    datos = {
        'investigaciones': [
            {'titulo': 'Estudio sobre marketing digital', 'ano': 2023, 'citas': 15},
            {'titulo': 'Negocios internacionales en América Latina', 'ano': 2022, 'citas': 20},
            {'titulo': 'Innovación en mercados emergentes', 'ano': 2023, 'citas': 10},
            {'titulo': 'Tendencias de consumo', 'ano': 2021, 'citas': 25},
        ]
    }
    return jsonify(datos)

if __name__ == '__main__':
    app.run(debug=True)
