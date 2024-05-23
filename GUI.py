import numpy as np
import pickle
import streamlit as st
import git
import os  # Import os module for directory operations

# Define the local repository path
local_repo_path = '/path/to/local/repo'  # Adjust this to the desired local directory

# Ensure the directory exists, if not, create it
if not os.path.exists(local_repo_path):
    os.makedirs(local_repo_path)

# Clone the GitHub repository
repo_url = 'https://github.com/elisabethlala123/tugasakhir01.git'
git.Repo.clone_from(repo_url, local_repo_path)

# Define the path to your pickled file
file_path = os.path.join(local_repo_path, 'data', 'trained_model.pkl')  # Adjust path based on your directory structure

# loading the saved model
loaded_model = pickle.load(open(file_path, 'rb'))

# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    
  
def main():
    
    
    # giving a title
    st.title('Diabetes Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
