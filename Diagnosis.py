import streamlit as st
import pandas as pd
from sklearn.svm import SVC

# Set page config
st.set_page_config(page_title='Diagnosis ISPA', layout='wide')

def run():
    @st.cache_data
    def load_data():
        data = pd.read_excel('ispabaru_normalized2.xlsx')
        return data

    # Title
    st.markdown("<h1 style= 'text-align: center;'>Diagnosis ISPA</h1>" , unsafe_allow_html=True)

    # Load data
    data = load_data()

    # Split dataset into features and target variable
    X = data.drop('Kategori', axis=1)
    y = data['Kategori']

    def user_input_features():
        # Create input fields based on the columns in the dataset
        features = {}
        for column in X.columns:
            if column in ["Umur", "RR", "S"]:
                feature_value = st.number_input(column, step=0.01, key=column)
            elif column in ["Gender"]:
                feature_value = st.selectbox(column, options=["Laki-laki","Perempuan"], key="Gender")
            else:
                feature_value = st.selectbox(column, options=["Ya", "Tidak"], key=column)
            features[column] = feature_value

        input_data = pd.DataFrame(features, index=[0])
        return input_data


    input_df = user_input_features()

    # Map input values to numeric values
    input_df = input_df.replace({"Ya": 1, "Tidak": 0})
    input_df = input_df.replace({"Laki-laki": 1, "Perempuan": 0})

    # CSS styling to center the input fields
    st.markdown(
        """
        <style>
        .element-container {
            display: flex;
            justify-content: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display user input
    st.subheader("User Input:")
    st.dataframe(input_df)

    # Create SVM model with a linear kernel
    model = SVC(kernel='linear', C=0.1)
    model.fit(X, y)

    # Make prediction on user input
    prediction = model.predict(input_df)

    # Mapping label
    label_mapping = {0: 'Anda Tidak didiagnosis Pneumonia',
                     1: 'Anda didiagnosis Pneumonia'}

    # Display prediction result
    st.subheader("Diagnosis Result:")
    if prediction[0] in label_mapping:
        st.success(label_mapping[prediction[0]])
    else:
        st.warning("Tidak dapat melakukan diagnosis")

run()
