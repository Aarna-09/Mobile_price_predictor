from flask import Flask, render_template, request
import pandas as pd
import pickle
import logging


app = Flask(__name__)
model = pickle.load(open('model_saved (2)' , 'rb'))


brands = pd.read_csv('Cleaned_price.csv')

@app.route('/')
def index1():
    return render_template('index1.html')

@app.route('/layout1')
def layout1():
    if brands.empty:
        return "Dataset not loaded. Please check the server logs."

    rating_values = brands['Ratings'].tolist()
    ram = brands['RAM'].tolist()
    rom = brands['ROM'].tolist()
    mobile_size = brands['Mobile_Size'].tolist()
    primary_cam = brands['Primary_Cam'].tolist()
    selfi_cam = brands['Selfi_Cam'].tolist()
    battery_power = brands['Battery_Power'].tolist()

    return render_template('layout1.html', ratings=rating_values, Ram=ram, Rom=rom, Mobile_size=mobile_size, Primary=primary_cam, Selfie=selfi_cam, battery=battery_power)

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        logging.error("Model not loaded. Please check the server logs.")
        return "Model not loaded. Please check the server logs."

   
       
    user_input = [request.form.get(key) for key in ['Ratings', 'RAM', 'ROM', 'Mobile_Size', 'Primary_Cam', 'Selfi_Cam', 'Battery_Power']]

    input_data = [float(i) for i in user_input]

        
    prediction = model.predict([input_data])

        
    rating_values = brands['Ratings'].tolist()
    ram = brands['RAM'].tolist()
    rom = brands['ROM'].tolist()
    mobile_size = brands['Mobile_Size'].tolist()
    primary_cam = brands['Primary_Cam'].tolist()
    selfi_cam = brands['Selfi_Cam'].tolist()
    battery_power = brands['Battery_Power'].tolist()

       
    return render_template('layout1.html', prediction=prediction[0], ratings=rating_values, Ram=ram, Rom=rom, Mobile_size=mobile_size, Primary=primary_cam, Selfie=selfi_cam, battery=battery_power)
    # except Exception as e:
    #     logging.error(f"An error occurred during prediction: {e}")
    #     return "An error occurred during prediction. Please check the server logs."

if __name__ == '__main__':
    
    app.run()
