# Autoencoders y Error de Reconstrucción para Detectar Muestras de Cáncer

Este repositorio contiene el código y la documentación del Trabajo de Fin de Grado (TFG) titulado "Autoencoders y Error de Reconstrucción para Detectar Muestras de Cáncer" realizado por Marco Tenorio Cortés para obtener el título de Grado en Ingeniería Informática - Tecnologías Informáticas en la Universidad de Sevilla.

## Resumen

Este TFG se centra en el desarrollo y evaluación de un modelo avanzado de autoencoder para la detección de anomalías en muestras de cáncer de mama. Utilizando el conjunto de datos Breast Cancer Wisconsin, se ha implementado un autoencoder para clasificar las diferentes muestras en malignas y benignas, entrenando el modelo exclusivamente con muestras benignas, en un escenario donde hay una alta desproporción entre la cantidad de muestras de cada clase.

La metodología aplicada abarca desde la preparación y normalización de los datos hasta la implementación de arquitecturas de redes neuronales profundas, haciendo uso de técnicas como el ajuste de hiperparámetros para optimizar el modelo. El enfoque principal ha sido examinar cómo el error de reconstrucción del autoencoder puede servir como un indicador fiable de anomalías, potencialmente indicando presencia de tejido canceroso.

Los resultados obtenidos demuestran que los autoencoders son capaces de distinguir con una precisión significativa entre muestras normales y patológicas, superando en algunos casos a métodos tradicionales de aprendizaje automático. Además, se ha desarrollado una interfaz web para facilitar la visualización de los resultados del modelo, permitiendo una interpretación más intuitiva de los datos. Puedes acceder a ella en https://sanidad.mtcor.es.

## Estructura del Repositorio

- `notebooks/`: Contiene los notebooks de Jupyter utilizados durante el desarrollo del proyecto.
- `demo/`: Ficheros relevantes sobre la estructura del servicio Flask.
- `data/`: Fichero excel para su prueba en la predicción del autoencoder en la demo anteriormente mencionada.
- `models/`: Modelos entrenados preparados para su importación.
- `docs/`: Documentación del proyecto, incluyendo el informe final del TFG.
- `requirements.txt`: Fichero con las dependencias necesarias.

## Cómo Empezar

### Prerrequisitos

- Python 3.8+
- TensorFlow
- Keras
- Scikit-Learn
- Pandas
- Numpy
- Flask

### Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/MarcoTenCortes/TFG-Autoencoder.git
    cd TFG-Autoencoder
    ```

2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

### Uso

1. **Entrenamiento del Modelo**:
    Ejecuta el notebook de Jupyter `notebooks/train_autoencoder.ipynb` para entrenar el modelo de autoencoder con el conjunto de datos Breast Cancer Wisconsin.
2. **Analiza y modifica el Notebook**
   Realiza diferentes modificaciones que veas necesarias para comprobar como varia el modelo.
3. **Uso del autoencoder**
   En caso de que quieras utilizar el autoencoder de manera externa puedes importar el fichero que encontraras en /models
4. **Demo técnica**
   Usa el contenido de la carpeta "Demo" para iniciar el servicio Flask, donde puedes probar el modelo para realizar diferentes predicciones.

## Contribuciones

Si deseas contribuir a este proyecto, por favor crea un fork del repositorio y envía un pull request con tus cambios. Agradecemos cualquier tipo de contribución, desde reportes de errores hasta mejoras en la documentación y el código.

## Autor

**Marco Tenorio Cortés** - [marcotencortes@hotmail.com](mailto:marcotencortes@hotmail.com)

## Agradecimientos

Quiero agradecer a mi director de TFG, Juan Antonio Nepomuceno Chamorro, por su guía y apoyo a lo largo de este proyecto. También agradezco a mi familia y amigos por su constante motivación y apoyo.

---

*Para más información, por favor consulta la documentación completa en el directorio `docs/`.*
