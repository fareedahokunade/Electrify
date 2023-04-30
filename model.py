
import xgboost as xgb
import streamlit as st
import pandas as pd
import sklearn

#Loading up the Regression model we created
model = xgb.XGBRegressor()
model.load_model('model.json')

#Caching the model for faster loading




def predict(Seville_temp_max, Madrid_pressure, Valencia_temp_max, Valencia_temp, Bilbao_weather_id,
             Seville_temp, Valencia_temp_min, Barcelona_temp_max, Madrid_temp_max, Barcelona_temp,
             Bilbao_temp_min, Bilbao_temp, Barcelona_temp_min, Bilbao_temp_max, Seville_temp_min,
             Madrid_temp, Madrid_temp_min):
    
    data = pd.DataFrame([[Seville_temp_max, Madrid_pressure, Valencia_temp_max, Valencia_temp, Bilbao_weather_id,
                          Seville_temp, Valencia_temp_min, Barcelona_temp_max, Madrid_temp_max, Barcelona_temp,
                          Bilbao_temp_min, Bilbao_temp, Barcelona_temp_min, Bilbao_temp_max, Seville_temp_min,
                          Madrid_temp, Madrid_temp_min]],
                        columns=['Seville_temp_max', 'Madrid_pressure', 'Valencia_temp_max', 'Valencia_temp',
                                 'Bilbao_weather_id', 'Seville_temp', 'Valencia_temp_min', 'Barcelona_temp_max',
                                 'Madrid_temp_max', 'Barcelona_temp', 'Bilbao_temp_min', 'Bilbao_temp',
                                 'Barcelona_temp_min', 'Bilbao_temp_max', 'Seville_temp_min', 'Madrid_temp',
                                 'Madrid_temp_min'])
    
    prediction = model.predict(data)
    return prediction


st.title('Electricity Shortage Predictor')
st.image("""https://t3.ftcdn.net/jpg/02/99/23/72/360_F_299237262_Cj3wYz3HK7Aak1qNW4biP268qL1wphOr.jpg""")
st.header('Enter the features:')


Seville_temp_max = st.number_input('Seville_temp_max:', min_value=272.063, max_value=320.4833333333, value=300.0)
Madrid_pressure = st.number_input('Madrid_pressure:', min_value=927.6666666667, max_value=1038.0)
Valencia_temp_max = st.number_input('Valencia_temp_max:', min_value=269.888, max_value=314.2633333333)
Valencia_temp = st.number_input('Valencia_temp:', min_value=269.888, max_value=310.4266666667)
Bilbao_weather_id = st.number_input('Bilbao_weather_id:', min_value=207.3333333333, max_value=804.0)
Seville_temp = st.number_input('Seville_temp:', min_value=272.063, max_value=314.9766666667)
Valencia_temp_min = st.number_input('Valencia_temp_min:', min_value=269.888, max_value=310.272)
Barcelona_temp_max = st.number_input('Barcelona_temp_max:', min_value=272.15, max_value=314.0766666667)
Madrid_temp_max = st.number_input('Madrid_temp_max:', min_value=264.9833333333, max_value=314.4833333333)
Barcelona_temp = st.number_input('Barcelona_temp:', min_value=270.8166666667, max_value=307.3166666667)
Bilbao_temp_min = st.number_input('Bilbao_temp_min:', min_value=264.4833333333, max_value=309.8166666667)
Bilbao_temp = st.number_input('Bilbao_temp:', min_value=267.4833333333, max_value=310.71)
Barcelona_temp_min = st.number_input('Barcelona_temp_min:', min_value=269.4833333333, max_value=304.8166666667)
Bilbao_temp_max = st.number_input('Bilbao_temp_max:', min_value=269.063, max_value=317.9666666667)
Seville_temp_min = st.number_input('Seville_temp_min:', min_value=270.15, max_value=314.8166666667)
Madrid_temp = st.number_input('Madrid_temp:', min_value=264.9833333333, max_value=313.1333333333)
Madrid_temp_min = st.number_input('Madrid_temp_min:', min_value=264.9833333333, max_value=310.3833333333)
load_shortfall_3h = st.number_input('load_shortfall_3h:', min_value=-6618.0, max_value=31904.0)


if st.button('Predict amount of shortage'):
    shortage = predict(Seville_temp_max, Madrid_pressure, Valencia_temp_max, Valencia_temp, Bilbao_weather_id,
             Seville_temp, Valencia_temp_min, Barcelona_temp_max, Madrid_temp_max, Barcelona_temp,
             Bilbao_temp_min, Bilbao_temp, Barcelona_temp_min, Bilbao_temp_max, Seville_temp_min,
             Madrid_temp, Madrid_temp_min)
    st.success(f'The predicted amount of shortage is {shortage[0]:.4f}')