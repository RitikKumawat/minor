import numpy as np 
import pickle
import streamlit as st 
loaded_model = pickle.load(open('https://github.com/RitikKumawat/minor/blob/main/trained_model.sav','rb'))

def fraud_prediction(input_data):
    input_data_as_numpy_array =  np.array(input_data)

    input_data_reshaped =  input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==0):
        return "It is not a fraud transaction"
    else:
        return "It is a fraud Transaction"
    
def main():

    st.title("Credit Card Fraud Detection")

    v1 = st.text_input("V1")
    v2 = st.text_input("V2")
    v3 = st.text_input("V3")
    v4 = st.text_input("V4")
    v5 = st.text_input("V5")
    v6 = st.text_input("V6")
    v7 = st.text_input("V7")
    v8 = st.text_input("V8")
    v9 = st.text_input("V9")
    v10 = st.text_input("V10")
    v11 = st.text_input("V11")
    v12 = st.text_input("V12")
    v13 = st.text_input("V13")
    v14 = st.text_input("V14")
    v15 = st.text_input("V15")
    v16 = st.text_input("V16")
    v17 = st.text_input("V17")
    v18 = st.text_input("V18")
    v19 = st.text_input("V19")
    v20 = st.text_input("V20")
    v21 = st.text_input("V21")
    v22 = st.text_input("V22")
    v23 = st.text_input("V23")
    v24 = st.text_input("V24")
    v25 = st.text_input("V25")
    v26 = st.text_input("V26")
    v27 = st.text_input("V27")
    v28 = st.text_input("V28")

    amount = st.text_input("Amount")


    detection = ''

    if st.button("Detect Fraud"):
        detection = fraud_prediction([v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,amount])

    st.success(detection)


if __name__ == "__main__":
    main()
