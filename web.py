import os 
import pickle #pre trained model loading
import streamlit as st #web app
from streamlit_option_menu import option_menu
#Go to streamlit documentation to know all

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon='doctor')
diabetese_model = pickle.load(open(r"training-models\diabetes_model.sav",'rb'))
heart_disease_model = pickle.load(open(r"training-models\heart_model.sav",'rb'))
parkinsons_model = pickle.load(open(r"training-models\parkinsons_model.sav",'rb'))

with st.sidebar:
    selected = option_menu('Prediction of disease outbreak system',['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                           menu_icon='hospital-fill', icons=['activity','heart','person'],default_index=0)

if selected == 'Diabetes Prediction':
    st.title("Diabetese Prediction using ML")
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        Bloodpressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPredigreeFunction = st.text_input('Diabetese Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the person')

        
    st.write("Fill in the values and click the prediction button.")
    
    if st.button('Check for Diabetes'):
        user_input = [Pregnancies,Glucose,Bloodpressure,SkinThickness,Insulin,BMI,DiabetesPredigreeFunction,Age]
        user_input = [float(x) for x in user_input]
        diab_prediciton = diabetese_model.predict([user_input])
        if diab_prediciton[0] == 1:
            st.success("The person is likely to have Diabetes.")
        else:
            st.success("The person is unlikely to have Diabetes.")

if selected == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction using ML")
    col1,col2,col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Gender')
    with col3:
         cp = st.selectbox(
        'Chest Pain Type',
        options=[1, 2, 3, 4], 
        format_func=lambda x: {
            1: "Typical angina",
            2: "Atypical angina",
            3: "Non-anginal pain",
            4: "Asymptomatic"
        }[x]
         )
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.text_input('Exercise-Induced Angina')
    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise')
    with col2:
        slope = st.text_input('Slope of the Peak Exercise ST Segment')
    with col3:
        ca = st.text_input('Number of Major Vessels Colored by Fluoroscopy')
    with col1:
        thal = st.text_input('Thalassemia')
        
    st.write("Fill in the values and click the prediction button.")
    
    if st.button('Check for Heart Disease'):
        user_input = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        user_input = [float(x) for x in user_input]
        heart_pred = heart_disease_model([user_input])
        if heart_pred[0]==1:
            st.success("The person is likely to have a Heart Disease.")
        else:
            st.success("The person is unlikely to have a Heart Disease.")


if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction using ML')
    col1,col2,col3 = st.columns(3)
    with col1:
        fo = st.text_input("Fundamental Frequency")
        jitter_perc = st.text_input("Frequency Variation")
        ppq = st.text_input('Pitch Period Perturbation Quotient')
        shimmer_db = st.text_input("Shimmer value measured in decibels")
        MDVP_apq = st.text_input('amplitude perturbation')
        HNR = st.text_input("Harmonics-to-Noise Ratio")
        spread1 = st.text_input("Nonlinear fundamental Frequency's Variation")
        ppe = st.text_input('Pitch Period Entropy')

    with col2:
        fhi = st.text_input("Highest Frequency")
        jitter_abs = st.text_input('Absolute jitter value in Hz')
        jitter_ddp = st.text_input('Difference of Differences of Periods')
        Apq3 = st.text_input('Three-point Amplitude Perturbation Quotient')
        Shimmer_dda = st.text_input('Shimmer Detrended Data Analysis')
        RPDE = st.text_input("Recurrence Period Density Entropy")
        spread2 = st.text_input("Nonlinear Frequency Variation")

    with col3:
        flo = st.text_input("Lowest Frequency")
        MDVP_rap = st.text_input('Relative Amplitude Perturbation')
        Shimmer = st.text_input('Amplitude variation in the voice signal')
        Apq5 = st.text_input('Five-point Amplitude Perturbation Quotient')
        NHR = st.text_input("Noise-to-Harmonics Ratio")
        DFA = st.text_input("Signal Correlation")
        D2 = st.text_input("Signal Complexity Measure")

    st.write("Fill in the values and click the prediction button.")


    if st.button("Check for Parkinson's Disease"):
        user_input = [fo, fhi, flo, jitter_perc, jitter_abs, MDVP_rap,shimmer_db, jitter_ddp, Shimmer, shimmer_db, Apq3, Apq5, MDVP_apq, Shimmer_dda, NHR, HNR, RPDE, 
                    DFA, spread1, spread2, D2, ppe]
        user_input = [float(x) for x in user_input]  # Convert to float
        prediction = parkinsons_model.predict([user_input])  
        if prediction[0] == 1:
            st.success("The person is likely to have Parkinson's Disease.")
        else:
            st.success("The person is unlikely to have Parkinson's Disease.")


