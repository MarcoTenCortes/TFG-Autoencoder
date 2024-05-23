from flask import Flask, request, render_template, redirect, url_for
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from joblib import load
from werkzeug.utils import secure_filename
import os
from tensorflow.keras.metrics import MeanSquaredError
from tensorflow.keras.utils import get_custom_objects

get_custom_objects().update({'mse': MeanSquaredError()})
app = Flask(__name__)

# Configura un directorio para guardar archivos subidos
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Cargar el modelo y el normalizador
autoencoder = load_model('model/autoencoder55.h5')
normalizador = load('normalizador/normalizador1.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' in request.files and request.files['file'].filename != '':
        return predict_from_excel(request.files['file'])

    try:
        return predict_from_form(request.form)
    except Exception as e:
        # Si hay un error en el procesamiento del formulario, redireccionar a la página principal
        print(e)  # Es bueno registrar el error para depuración
        return redirect(url_for('index'))

def predict_from_excel(file):
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    data = pd.read_excel(filepath)
    return make_prediction(data)

def predict_from_form(form):
    # Asegurarse de que todos los campos requeridos están presentes
    feature_names = [
        'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
        'smoothness_mean', 'compactness_mean', 'concavity_mean',
        'concave_points_mean', 'symmetry_mean', 'radius_se', 'texture_se',
        'perimeter_se', 'area_se', 'smoothness_se', 'compactness_se',
        'concavity_se', 'concave_points_se', 'symmetry_se', 'fractal_dimension_se',
        'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst',
        'smoothness_worst', 'compactness_worst', 'concavity_worst',
        'concave_points_worst', 'symmetry_worst', 'fractal_dimension_worst'
    ]
    data = {feature: [float(form[feature])] for feature in feature_names if feature in form}
    df = pd.DataFrame(data)
    return make_prediction(df)

def make_prediction(data):
    if 'MEAN FRACTAL DIMENSION' in data.columns:
        data = data.drop(columns=['MEAN FRACTAL DIMENSION'])

    features = data[[
        'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
        'smoothness_mean', 'compactness_mean', 'concavity_mean',
        'concave_points_mean', 'symmetry_mean', 'radius_se', 'texture_se',
        'perimeter_se', 'area_se', 'smoothness_se', 'compactness_se',
        'concavity_se', 'concave_points_se', 'symmetry_se', 'fractal_dimension_se',
        'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst',
        'smoothness_worst', 'compactness_worst', 'concavity_worst',
        'concave_points_worst', 'symmetry_worst', 'fractal_dimension_worst'
    ]].values

    features_norm = normalizador.transform(features)
    predictions = autoencoder.predict(features_norm)
    reconstruction_errors = np.mean(np.power(features_norm - predictions, 2), axis=1)

    umbral_fijo = 0.3
    y_preds = [1 if e > umbral_fijo else 0 for e in reconstruction_errors]
    resultados = ['Maligno' if pred == 1 else 'Benigno' for pred in y_preds]

    return render_template('resultados.html', resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

