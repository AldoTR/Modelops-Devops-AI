import json
import streamlit as st
import requests
import numpy as np

SERVER_URL = 'https://linear-model-service-aldotr.cloud.okteto.net/v1/models/linear-model:predict'

def make_prediction(hours_worked):
    payload = {'instances': [hours_worked]}
    response = requests.post(SERVER_URL, json=payload)
    response.raise_for_status()
    prediction = response.json()
    return prediction['predictions'][0][0]

def calculate_efficiency(hours_worked):
    efficiency_metric = 3 * hours_worked + 2
    return efficiency_metric

def main():
    st.title('Calculadora de costo de viaje')

    hours_worked = st.number_input('Ingrese el número de horas estimadas:', min_value=0.0, step=1.0)

    if st.button('Calcular'):
        # Hacer la llamada al servidor externo para predecir la métrica
        predicted_efficiency = make_prediction(hours_worked)
        
        # Calcular la métrica relacionada con el costo de viaje
        efficiency_result = calculate_efficiency(hours_worked)
        
        st.write(f'Métrica de de costo de viaje {hours_worked} horas trabajadas: {efficiency_result}')
        st.write(f'Métrica predicha por el servidor externo: {predicted_efficiency}')

if __name__ == '__main__':
    main()
