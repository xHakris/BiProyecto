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
        caracteristica_6 = float(request.form['caracteristica_6'])
        caracteristica_7 = float(request.form['caracteristica_7'])
        caracteristica_8 = float(request.form['caracteristica_8'])
        caracteristica_9 = float(request.form['caracteristica_9'])
        caracteristica_10 = float(request.form['caracteristica_10'])
        caracteristica_11 = float(request.form['caracteristica_11'])
        caracteristica_12 = float(request.form['caracteristica_12'])
        caracteristica_13 = float(request.form['caracteristica_13'])
        caracteristica_14 = float(request.form['caracteristica_14'])
        caracteristica_15 = float(request.form['caracteristica_15'])

        # Realiza la predicción con las características recibidas

        # Aquí deberías utilizar tu lógica para cargar el modelo y hacer la predicción
        # Ejemplo: 
        # prediction = tu_funcion_de_prediccion(caracteristica_1, caracteristica_2)
        prediction = 0  # Reemplaza con la predicción real de tu modelo

        return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
