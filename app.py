import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Covid-19 Affect Prediction App

This app predicts **Whether the company affected by Covid-19 or not**

Data obtained from the [World Bank Data Library](https://raw.githubusercontent.com/vineshbavikkara/Streamlit-web-app-covid-19-affect/master/Albania_Cleaned_Data.csv)
""")

st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/vineshbavikkara/Streamlit-web-app-covid-19-affect/master/Example_file.csv)
[Description](https://raw.githubusercontent.com/vineshbavikkara/Streamlit-web-app-covid-19-affect/master/Description.csv)
""")
# Collects user input features into dataframe
st.set_option('deprecation.showfileUploaderEncoding', False)
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        Industry_Type = st.sidebar.selectbox('Industry Type',('Manufacturing','Retail','Other'))
        Current_Situation = st.sidebar.selectbox('Current Situation',('Open','Temporarily_Closed'))
        Direct_Export = st.sidebar.selectbox('Direct Export',('Very_Low','Low','Medium','High'))
        Indirect_Export = st.sidebar.selectbox('Indirect Export',('Very_Low','Low','Medium','High'))
        Hours_Worked_Per_Week = st.sidebar.selectbox('Hours Worked Per Week',('Decrease','Remain_the_Same','Increase'))
        Demand_For_Product = st.sidebar.selectbox('Demand For Product',('Decrease','Remain_the_Same','Increase'))
        Supply_Of_Raw_Materials = st.sidebar.selectbox('Supply of Raw Materials',('Decrease','Remain_the_Same','Increase'))
        Financial_Performance = st.sidebar.selectbox('Financial Performance',('Decrease','Remain_the_Same','Increase'))
        Online_Business = st.sidebar.selectbox('Online Business',('Yes','No'))
        data = {'Industry_Type': Industry_Type,'Current_Situation': Current_Situation,'Direct_Export': Direct_Export,'Indirect_Export': Indirect_Export,'Hours_Worked_Per_Week': Hours_Worked_Per_Week,'Demand_For_Product': Demand_For_Product,'Supply_Of_Raw_Materials': Supply_Of_Raw_Materials,'Financial_Performance': Financial_Performance,'Online_Business': Online_Business}
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()
# Changing to dummy variables
data_raw = pd.read_csv('Albania_Cleaned_Data.csv')
data = data_raw.drop(columns=['Sales_Performance'])
df = pd.concat([input_df,data],axis=0,ignore_index=True)
# Encoding of Label features
df = pd.get_dummies(df)
df = df.drop(columns = ['Industry_Type_Manufacturing','Current_Situation_Temporarily_Closed','Direct_Export_High','Indirect_Export_High','Hours_Worked_Per_Week_Increase','Demand_For_Product_Increase','Supply_Of_Raw_Materials_Increase','Financial_Performance_Increase','Online_Business_Yes'])
df = df.reindex(['Industry_Type_Retail','Industry_Type_Other','Current_Situation_Open','Direct_Export_Low','Direct_Export_Medium','Direct_Export_Very_Low','Indirect_Export_Low','Indirect_Export_Medium','Indirect_Export_Very_Low','Hours_Worked_Per_Week_Remain_the_Same','Hours_Worked_Per_Week_Decrease','Demand_For_Product_Remain_the_Same','Demand_For_Product_Decrease','Supply_Of_Raw_Materials_Remain_the_Same','Supply_Of_Raw_Materials_Decrease','Financial_Performance_Remain_the_Same','Financial_Performance_Decrease','Online_Business_No'],axis=1)
df = df.astype(int)
df = pd.DataFrame(df.iloc[:1,:])
# Displays the user input features
st.subheader('User Input features')
if uploaded_file is not None:
    st.write(df)
else:
    st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
    st.write(df)
# Reads in saved classification model
load_clf = pickle.load(open('model.pkl','rb'))
# Apply model to make predictions
prediction = load_clf.predict(df)
prediction_proba = load_clf.predict_proba(df)
st.subheader('Prediction')
Affected_or_not = np.array(['Affected','Not Affected'])
st.write(Affected_or_not[prediction])
st.subheader('Prediction Probability')
st.write(prediction_proba)