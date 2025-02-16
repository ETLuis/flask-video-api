from flask import Flask, request, jsonify
from video_script import generar_video

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "API funcionando!"

@app.route('/generar-video', methods=['POST'])
def recibir_datos():
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Datos no recibidos"}), 400

    # Aquí ejecutas tu script con los datos recibidos
    resultado_video = generar_video(datos)

    return jsonify({"mensaje": "Video generado correctamente", "ruta_video": resultado_video})

if __name__ == '__main__':
    app.run(debug=True)
