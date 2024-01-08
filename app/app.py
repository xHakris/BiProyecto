from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        caracteristica_1 = float(request.form['caracteristica_1'])
        caracteristica_2 = float(request.form['caracteristica_2'])
        caracteristica_3 = float(request.form['caracteristica_3'])
        caracteristica_4 = float(request.form['caracteristica_4'])
        caracteristica_5 = float(request.form['caracteristica_5'])
        # Realiza la predicción con las características recibidas

        # Aquí deberías utilizar tu lógica para cargar el modelo y hacer la predicción
        # Ejemplo: 
        # prediction = tu_funcion_de_prediccion(caracteristica_1, caracteristica_2)
        prediction = 0  # Reemplaza con la predicción real de tu modelo

        return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
