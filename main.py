import pickle
import streamlit  as st
import numpy as np

#load the training model

pickl_in = open("Heart_classifier.pkl",'rb')
heart_classify = pickle.load(pickl_in)


def prediction(Age,Gender,chest_pain_type,rest_blood_pressure,serum_chol,Fast_blood_sugar,ecg,heart_rate,e_angina,st_depr_val,peak_ST_segment,num_vessels,thal):

    if Gender == 'Male':
        Gender =1
    else:
        Gender =0
    
    if chest_pain_type == "Typical angina":
        chest_pain_type = 1
    elif chest_pain_type == "Atypical angina":
        chest_pain_type = 2
    elif chest_pain_type == "Non — anginal pain":
        chest_pain_type = 3
    else:
        chest_pain_type = 4

    if Fast_blood_sugar > 120:
        Fast_blood_sugar =1
    else:
        Fast_blood_sugar =0

    if ecg == "Normal":
        ecg = 0
    elif ecg == "ST-T wave abnormality":
        ecg=1

    else:
          ecg= 2


    if e_angina == "YES":
        e_angina=0

    else:
        e_angina =1

    if peak_ST_segment == "upsloping":
        peak_ST_segment=1

    elif peak_ST_segment == "flat":
        peak_ST_segment =2

    else:
        peak_ST_segment =3

    if thal == "normal":
        thal =3
    elif thal == "fixed defect":
        thal = 6
    else:
        thal = 7

    result =''
    pred_array = np.array([[Age,Gender,chest_pain_type,rest_blood_pressure,serum_chol,Fast_blood_sugar,ecg,heart_rate,e_angina,st_depr_val,peak_ST_segment,num_vessels,thal]])

    pred_val = heart_classify.predict(pred_array)
    if pred_val == 0:
        result = "No heart Disease"
    else:
        result = "Have heart disease"

    
    return result
    
def main():

    st.set_page_config(
     page_title="ML APP",
     page_icon="heart",
     layout="wide",
     initial_sidebar_state="expanded",)
    html_style = """ 
    <div style ="background-color:orange;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Heart Disease Prediction  ML App</h1> 
    </div>
    """

    st.markdown(html_style,unsafe_allow_html=True)


    Age = st.number_input("Enter you Age")

    Gender = st.selectbox("Enter your Gender",("Male","Female"))

    chest_pain_type = st.selectbox("Enter the type of chest pain",("Typical angina","Atypical angina","Non — anginal pain","Asymptotic"))

    rest_blood_pressure = st.number_input("Enter your resting blood pressure value in in mmHg (unit)")

    serum_chol = st.number_input("Enter your serem Cholestrol in mg/dl (unit)")

    Fast_blood_sugar = st.number_input("Enter Fasting Blood Sugar in mg/dl (unit)")

    ecg = st.selectbox("Enter the type of ECG",("Normal","ST-T wave abnormality","left ventricular hyperthrophy"))
    
    heart_rate = st.number_input("Enter your heart rate")
   
    e_angina = st.selectbox("Is angina induced",("YES","NO"))
   
    st_depr_val = st.number_input("ST DEPRESSION Value")
   
    peak_ST_segment = st.selectbox("Peak exercise ST segment",("upsloping","flat","downsloping"))
   
    num_vessels = st.number_input("Number of major vessels 0-3")
   
    thal = st.selectbox("Select the type of Thal",("normal","fixed defect","reversible defect"))

    result =''

    if st.button('Predict'):

        result = prediction(Age,Gender,chest_pain_type,rest_blood_pressure,serum_chol,Fast_blood_sugar,ecg,heart_rate,e_angina,st_depr_val,peak_ST_segment,num_vessels,thal)
        st.success("You have {}".format(result))
        print(result)

if __name__ == '__main__':
    main()

