# -*- coding: utf-8 -*-
"""


"""

import numpy as np
import pickle
import streamlit as st
import time
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from streamlit_option_menu import option_menu

 

with st.sidebar:
    selected = option_menu("Menu", ["Home",'Diabetes Prediction',
     'Heart Disease Prediction', 'Others'], 
        icons=['house','activity', 'heart', 'three-dots'], default_index=0)

        
    

# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))
heart_model = pickle.load(open('heart_disease_model.sav', 'rb'))


# creating a function for prediction
def diabetes_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if prediction[0] == 0:
        return 'Not Diabetic'
    else:
        return 'Diabetic'
    
  

# Function to send a thank-you email with test result and contact details
def send_thank_you_email(name, email, diagnosis):
    sender_name = "uzair kanza"
    sender_email = "uzerkanza05@gmail.com"  
    sender_password = "snsf tlna hihm yhsn"  

    webpapp_url = "https://dpswebapp-by-uzair.streamlit.app/"
    
    banner = """<!-- Insert the banner image -->
    <img src="{}" alt="Banner Image" style="max-width: 100%; height: auto; margin-top: 20px;">
    """.format('https://d2jx2rerrg6sh3.cloudfront.net/images/Article_Images/ImageForArticle_22744_16565132428524067.jpg')
    
    # Additional tips for diabetic patients and prevention
    additional_tips = """ 
    <p><strong><u>Tips for Diabetic Patients:</u></strong></p>
    <ol>
        <li><strong>Monitor Blood Sugar Levels:</strong><br>
        - Regularly check your blood glucose levels as advised by your healthcare provider.</li>
        <li><strong>Medication Adherence:</strong><br>
        - Take medications as prescribed by your healthcare provider.</li>
        <li><strong>Balanced Nutrition:</strong><br>
        - Adopt a diet rich in whole grains, lean proteins, fruits, and vegetables.</li>
        <li><strong>Regular Exercise:</strong><br>
        - Engage in physical activity like brisk walking, swimming, or cycling.</li>
        <li><strong>Mindful Stress Management:</strong><br>
        - Practice stress-reducing techniques, such as mindfulness, meditation, or yoga.</li>
    </ol>
    <p><strong><u>Tips for Diabetes Prevention:</u></strong></p>
    <ol>
        <li><strong>Healthy Dietary Choices:</strong><br>
        - Consume a well-balanced diet with a focus on fruits, vegetables, whole grains, and lean proteins.<br>
        - Limit the intake of processed foods, sugary drinks, and high-fat items.</li>
        <li><strong>Regular Physical Activity:</strong><br>
        - Engage in regular physical activity to maintain a healthy weight and improve insulin sensitivity.</li>
        <li><strong>Weight Management:</strong><br>
        - Aim for a body mass index (BMI) within the normal range.<br>
        - Even a small reduction in weight can significantly lower the risk of diabetes.</li>
        <li><strong>Reduce Sedentary Time:</strong><br>
        - Minimize sitting time and incorporate more movement into your daily routine.</li>
        <li><strong>Routine Health Check-ups:</strong><br>
        - Schedule regular check-ups to monitor overall health and detect any potential issues early on.</li>
    </ol>
    <p>**It's important to note that these tips should be personalized based on individual health conditions and preferences. Consultation with healthcare professionals is crucial for tailored advice and management.</p>
    """

    subject = "Thank You for Visiting Diabetes Prediction Web Application!"
    color = "red" if diagnosis == "Diabetic" else "green"
    body = f"Dear {name},<br><br>Thank you for visiting my Diabetes Prediction Web Application!<br><br><b>Test Result:</b> <b style='color:{color}'>{diagnosis}</b>{banner}{additional_tips}<br><br>WebApp URL: {webpapp_url}<br><br><br>Best regards,<br>Uzair kanza"

    message = MIMEMultipart()
    message["From"] = f"{sender_name} <{sender_email}>"
    message["To"] = email
    message["Subject"] = subject
    message.attach(MIMEText(body, "html"))

    # Open the PNG file
    with open("Diabetes_Infographics.png", "rb") as img_file:
        # Correct MIME type for PNG file
            pdf_attachment = MIMEApplication(img_file.read(), _subtype="png")
        
        # Ensure the filename matches the file type
            pdf_attachment.add_header(
            "Content-Disposition", "attachment", filename="Diabetes_Disease_Info.png"
        )
        
        # Attach the file to the email
            message.attach(pdf_attachment)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, message.as_string())
        
        
        
def heart_disease_prediction(input_data):
    try:
        # Convert all inputs to float to ensure numerical values
        input_data = [float(x) for x in input_data]

        # Reshape input for model
        input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)

        # Debugging: Print the input data and its shape
        print("Processed Input:", input_data_as_numpy_array)
        print("Input Shape:", input_data_as_numpy_array.shape)

        # Make prediction
        prediction = heart_model.predict(input_data_as_numpy_array)

        # Return the result
        return 'No Heart Disease' if prediction[0] == 0 else 'Heart Disease Detected'

    except ValueError as e:
        return f"Error: Invalid input! {str(e)}"
    except Exception as e:
        return f"Unexpected Error: {str(e)}"
 

# Function to send a thank-you email with test result and contact details
def send_thank_you_email_to_heart(name, email, diagnosis):
    sender_name = "uzair kanza"
    sender_email = "uzerkanza05@gmail.com"  
    sender_password = "snsf tlna hihm yhsn"  

    webpapp_url = "https://dpswebapp-by-uzair.streamlit.app/"
    
    banner = """<!-- Insert the banner image -->
<img src="{}" alt="Banner Image" style="max-width: 100%; height: auto; margin-top: 20px;">
""".format('https://www.labiotech.eu/wp-content/uploads/2023/05/Cure-for-cardiovascular-diseases.jpg')  # Replace with a valid image URL
    
    # Additional tips for heart patients and prevention
    additional_tips = """ 
    <p><strong><u>Tips for heart disease Patients:</u></strong></p>
    <ol>
        <li><strong>Heart-Healthy Diet:</strong><br>
        - Choose a diet rich in fruits, vegetables, whole grains, and lean proteins.<br>
        - Limit saturated and trans fats, cholesterol, and sodium.</li>
        <li><strong>Regular Exercise:</strong><br>
        - Engage in aerobic exercises like walking, jogging, or swimming for at least 150 minutes per week.<br>
        - Include strength training exercises to improve overall cardiovascular health.</li>
        <li><strong>Manage Blood Pressure:</strong><br>
        - Monitor blood pressure regularly and follow your healthcare provider's recommendations.<br>
        - Maintain a healthy weight and limit alcohol intake.</li>
        <li><strong>Quit Smoking:</strong><br>
        - If you smoke, quit. Smoking is a major risk factor for heart disease.</li>
        <li><strong>Manage Stress:</strong><br>
        - Practice stress-reducing techniques, such as mindfulness, meditation, or yoga.</li>
    </ol>
    <p><strong><u>Tips for heart Prevention:</u></strong></p>
    <ol>
        <li><strong>Regular Health Check-ups:</strong><br>
        - Monitor cholesterol levels, blood pressure, and other cardiovascular risk factors.<br>
        - Follow your healthcare provider's advice for preventive screenings.</li>
        <li><strong>Limit Alcohol Intake:</strong><br>
        -  If you drink alcohol, do so in moderation.</li>
        <li><strong>Maintain Optimal Blood Sugar Levels:</strong><br>
        - Keep blood sugar levels within the recommended range, as diabetes can contribute to heart disease.</li>
        <li><strong>Stay Hydrated:</strong><br>
        - Maintain proper hydration for overall health and heart function.</li>
        
    </ol>
    <p>**It's important to note that these tips should be personalized based on individual health conditions and preferences. Consultation with healthcare professionals is crucial for tailored advice and management.</p>
    """

    subject = "Thank You for Visiting heart Prediction Web Application!"
    color = "red" if diagnosis == "Heart Disease Detected" else "green"
    body = f"Dear {name},<br><br>Thank you for visiting my heart Prediction Web Application!<br><br><b>Test Result:</b> <b style='color:{color}'>{diagnosis}</b>{banner}{additional_tips}<br><br>WebApp URL: {webpapp_url}<br><br><br>Best regards,<br>Uzair kanza"

    message = MIMEMultipart()
    message["From"] = f"{sender_name} <{sender_email}>"
    message["To"] = email
    message["Subject"] = subject
    message.attach(MIMEText(body, "html"))

    # Open the PNG file
    with open("Heart_Disease_Info.png", "rb") as img_file:
        # Correct MIME type for PNG file
            pdf_attachment = MIMEApplication(img_file.read(), _subtype="png")
        
        # Ensure the filename matches the file type
            pdf_attachment.add_header(
            "Content-Disposition", "attachment", filename="Heart_Disease_Info.png"
        )
        
        # Attach the file to the email
            message.attach(pdf_attachment)

    
        

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, message.as_string())         

def main():
    if selected == 'Home':
        # Set page title
        st.title("🏠 Welcome to the Multiple Disease Prediction System!")
    
    # Introduction
        st.markdown(
        """
        
        🔍 **What is this platform?**  
        This web app helps users predict the likelihood of diseases like **Diabetes, Heart Disease, and more** using **Machine Learning**.  
        Just enter your details, and our model will analyze your health parameters to give you a risk assessment.
        """
    )
    
    # Features Section
        st.subheader("✨ Features of Our System")
        st.markdown(
        """  
        ✔️ **User-Friendly Interface** – Simple, fast, and easy-to-use web app.  
        ✔️ **Multi-Disease Support** – Currently supports **Diabetes & Heart Disease** prediction.  
        ✔️ **Health Awareness** – Learn about symptoms, prevention, and management tips.   
        """
    )
    
    # How to Use Section
        st.subheader("📌 How to Use?")
        st.markdown(
        """
        1️⃣ **Navigate** to the disease you want to check (Diabetes/Heart Disease).  
        2️⃣ **Enter required details** like blood pressure, glucose level, etc.  
        3️⃣ **Click \"Predict\"** to get your results instantly.  
        4️⃣ **Check the \"About\" tab** for more information on diseases. 

        """
    )
        
        st.subheader("⚠️ Disclaimer")
        st.markdown(
            """
        - **This Web App may not provide accurate predictions at all times. When in doubt, please enter the  values again and verify the predictions.**
        - **You are requested to provide your Name and Email for sending details about your test results. Rest assured, your information is safe and will be kept confidential.**
        - **It is important to note that individuals with specific risk factors or concerns should consult with healthcare professionals for personalized advice and management.**
"""
        )
    
    # Contact Information
        st.subheader("📞 Need Help?")
        st.markdown(
        """
        📩 **Email:** [uzerkanza05@gmail.com](mailto:uzerkanza05@gmail.com)  
        🌐 **webpapp_url:** https://dieseasewebapp.streamlit.app/  
        """
    )


    elif selected == 'Diabetes Prediction':
        tab1, tab2 = st.tabs(["Diabetes Diagnosis", "About Diabetes"])

        with tab1:
            st.title('Diabetes Prediction')

            name = st.text_input('Enter Your Name')
            email = st.text_input('Enter Your Email')

            if not name or not email:
                st.warning('Please enter both Name and Email to proceed!', icon="⚠️")
            else:
                email_type = ('@gmail.com', '@yahoo.com', '@outlook.com')
                if not email.endswith(email_type):
                    st.error("Invalid email address!", icon="❌")
                else:
                    st.caption("**Having confusion in giving inputs? Navigate to the Options menu in the top-left corner and click on **Others** for more information.")

                    sex = st.selectbox('Gender', ('Male', 'Female'))
                    Pregnancies = st.text_input('Number of Pregnancies (Enter 0 if Male)')
                    Glucose = st.text_input('Glucose Level')
                    BloodPressure = st.text_input('BloodPressure Value')
                    SkinThickness = st.text_input('Skin Thickness Value')
                    Insulin = st.text_input('Insulin Level')
                    BMI = st.text_input('BMI Value')
                    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
                    Age = st.slider('Choose your Age', 1, 100)

                    # Check if the entered values are numeric
                    if not all(value.replace('.', '', 1).isdigit() for value in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction]):
                        st.error("❗Please enter valid numerical values for the input fields.")
                    else:
                        # Prediction button
                        if st.button('Predict'):
                            with st.spinner('Please wait, loading...'):
                                diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
                                send_thank_you_email(name, email, diagnosis)

                                st.success(f"Test Result: **{diagnosis}**")

                                # Expandable Test Report Section
                                with st.expander("Click here to see Test Report"):
                                    st.markdown("### Patient Details")
                                    st.markdown(f"**Patient Name:** {name}")
                                    st.markdown(f"**Gender:** {sex}")
                                    st.markdown(f"**Age:** {Age}")

                                    # Dynamic Data for Table
                                    data = {
                                        "Parameter Name": ["gender","Age", "Pregnancies", "Glucose", "Blood Pressure", "Skin Thickness", "Insulin", "BMI", "Diabetes Pedigree Function"],
                                        "Patient Values": [sex,Age, Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction],
                                        "Normal Range": ["male/female","0-100", "0-10", "70-125", "120/80", "8-25", "25-250", "18.5-24.9", "< 1"],
                                        "Unit": ["string","years", "Number", "mg/dL", "mmHg", "mm", "mIU/L", "kg/m²", "No units"]
                                    }

                                    # Display Table
                                    import pandas as pd
                                    df = pd.DataFrame(data)
                                    st.dataframe(df, use_container_width=True)
                                    st.info('Do check your email for more details, Thank You.', icon="ℹ️")

            st.markdown(
                """<div style="position: fixed; bottom: 7.6px;left: 10px; right: 10px; text-align: left;color: grey; font-size: 14px;">
                Made by <span style="font-weight: bold; color:grey;">uzair</span>🎈
                </div>""",
                unsafe_allow_html=True)




        with tab2:
            st.subheader('What is Diabetes?')
            st.write(
        """
        Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy. 
        It occurs when your blood glucose (sugar) levels are too high. Over time, having too much sugar in your 
        blood can cause serious health problems, such as heart disease, vision loss, and kidney disease.
        """)

            st.subheader('Types of Diabetes:')
            st.write(
        """
        1. **Type 1 Diabetes:** 
           - A condition where the body produces little or no insulin. 
           - Often diagnosed in children and young adults.
           - Requires daily insulin injections.
        
        2. **Type 2 Diabetes:** 
           - A condition where the body doesn’t use insulin properly (insulin resistance).
           - Most common type of diabetes.
           - Often associated with obesity and lifestyle factors.
        
        3. **Gestational Diabetes:** 
           - Diabetes that occurs during pregnancy.
           - Usually resolves after childbirth but increases the risk of Type 2 diabetes later in life.
        """)

            st.subheader('Symptoms of Diabetes:')
            st.markdown(
        """
        - **Frequent urination:** Excess glucose in the blood causes the kidneys to work harder to filter it out.
        - **Increased thirst:** Frequent urination leads to dehydration, causing excessive thirst.
        - **Unexplained weight loss:** The body starts burning fat and muscle for energy when it can't use glucose properly.
        - **Fatigue:** Lack of glucose in the cells leads to low energy levels.
        - **Blurred vision:** High blood sugar levels can cause swelling in the lenses of the eyes.
        - **Slow-healing sores:** Diabetes affects blood circulation and the body's ability to heal.
        """)

            st.subheader('Risk Factors for Diabetes:')
            st.markdown(
        """
        - **Family history:** Having a parent or sibling with diabetes increases your risk.
        - **Obesity:** Excess body fat, especially around the abdomen, is a major risk factor.
        - **Sedentary lifestyle:** Lack of physical activity contributes to insulin resistance.
        - **Age:** Risk increases with age, especially after 45.
        - **Ethnicity:** Certain ethnic groups (e.g., African American, Hispanic, Native American) are at higher risk.
        - **Gestational diabetes:** Women who had diabetes during pregnancy are at higher risk of developing Type 2 diabetes later.
        """ )

            st.subheader('Prevention and Management:')
            st.write(
        """
        - **Maintain a healthy diet:** Focus on whole grains, fruits, vegetables, lean proteins, and healthy fats.
        - **Exercise regularly:** Aim for at least 30 minutes of moderate exercise most days of the week.
        - **Monitor blood sugar levels:** Regular monitoring helps you understand how food, activity, and medication affect your blood sugar.
        - **Take prescribed medications:** Follow your doctor's advice on medications or insulin therapy.
        - **Avoid smoking and limit alcohol:** Smoking and excessive alcohol consumption can worsen diabetes complications.
        """)

            st.subheader('Complications of Diabetes:')
            st.markdown(
        """
        - **Cardiovascular disease:** Diabetes increases the risk of heart attack, stroke, and high blood pressure.
        - **Nerve damage (neuropathy):** High blood sugar can damage nerves, leading to pain, tingling, or numbness.
        - **Kidney damage (nephropathy):** Diabetes can damage the kidneys, potentially leading to kidney failure.
        - **Eye damage (retinopathy):** Diabetes can damage the blood vessels in the retina, leading to blindness.
        - **Foot problems:** Poor circulation and nerve damage can lead to foot ulcers and infections.
        """)

            st.subheader('Myths and Facts About Diabetes:')
            st.markdown(
        """
        - **Myth:** Eating too much sugar causes diabetes.
          **Fact:** While sugar intake is a factor, diabetes is caused by a combination of genetic and lifestyle factors.
        
        - **Myth:** People with diabetes can't eat sweets.
          **Fact:** Sweets can be eaten in moderation as part of a balanced diet.
        
        - **Myth:** Only overweight people get diabetes.
          **Fact:** While obesity is a risk factor, people of any weight can develop diabetes.
        """)

            st.subheader('Resources and Further Reading:')
            st.markdown(
        """
        - [indian Diabetes Association](https://idf.org/our-network/regions-and-members/south-east-asia/members/india/diabetic-association-of-india/)
        - [World Health Organization (WHO) - Diabetes](https://www.who.int/health-topics/diabetes)
        - [National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK)](https://www.niddk.nih.gov/)
        """)

            # Load the image and provide download option
            
            st.subheader('Diabetes Disease Infographic')
            with open("Diabetes_Infographics.png", "rb") as file:
                btn = st.download_button(
                label="⬇️ Download Infographic",
                data=file,
                file_name="Diabetes_Infographic.jpg",
                mime="image/jpeg")


            
            st.info(
        """
        If you suspect you have diabetes or are at risk, consult a healthcare professional for proper diagnosis and treatment. 
        """)    
                
        
       
        
    elif selected == 'Heart Disease Prediction':
    # 🔹 Create tabs
        tab1, tab2 = st.tabs(["Heart Disease Diagnosis", "About Heart Disease"])

        with tab1:
            st.title('Heart Disease Prediction')

            name = st.text_input('Enter Your Name')
            email = st.text_input('Enter Your Email')

            if not name or not email:
                st.warning('Please enter both Name and Email to proceed!', icon="⚠️")
            else:
                email_type = ('@gmail.com', '@yahoo.com', '@outlook.com')
                if not email.endswith(email_type):
                    st.error("Invalid email address!", icon="❌")
                else:
                    st.caption("**Having confusion in giving inputs? Navigate to the Options menu in the top-left corner and click on **Others** for more information.")

                age = st.slider('Choose your age', 1, 100)
                sex = st.slider('Gender (0 = Female, 1 = Male)', 0, 1)
                cp = st.slider('Chest Pain Type', 1, 3)
                trestbps = st.slider('Resting Blood Pressure', 94, 200)
                chol = st.slider('Cholesterol', 126, 576)
                fbs = st.slider('Fasting Blood Sugar (1 = True, 0 = False)', 0, 1)
                restecg = st.slider('Resting Electrocardiographic', 0, 2)
                thalach = st.slider('Max Heart Rate', 71, 202)
                exang = st.slider('Exercise Induced Angina (1 = Yes, 0 = No)', 0, 1)
                oldpeak = st.slider('ST Depression', 0.0, 6.2, step=0.1)
                slope = st.slider('Slope', 0, 2)
                ca = st.slider('Number of Major Vessels (0-3) Colored by Fluoroscopy', 0, 4)
                thal = st.slider('Thalassemia (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)', 0, 3)

                input_values = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

                # Check if all inputs are valid
                if not all(value is not None and str(value).replace('.', '', 1).isdigit() for value in input_values):
                    st.error("❗Please enter valid numerical values for the input fields.")
                else:
                    # Prediction button
                    if st.button('Predict'):
                        with st.spinner('Please wait, loading...'):
                            diagnosis = heart_disease_prediction(input_values)
                            send_thank_you_email_to_heart(name, email, diagnosis)

                            st.success(f"Test Result: **{diagnosis}**")

                            # Expandable Test Report Section
                            with st.expander("Click here to see Test Report"):
                                st.markdown("### Patient Details")
                                st.markdown(f"**Patient Name:** {name}")
                                st.markdown(f"**Gender:** {'Male' if sex == 1 else 'Female'}")
                                st.markdown(f"**Age:** {age}")

                                # Dynamic Data for Table
                                data = {
                                    "Parameter Name": ["Age", "Sex", "Chest Pain Type", "Resting Blood Pressure", "Cholesterol", "Fasting Blood Sugar", "Resting ECG", "Max Heart Rate", "Exercise Induced Angina", "ST Depression", "Slope", "Major Vessels", "Thalassemia"],
                                    "Patient Values": [age, "Male" if sex == 1 else "Female", cp, trestbps, chol, "True" if fbs == 1 else "False", restecg, thalach, "Yes" if exang == 1 else "No", oldpeak, slope, ca, thal],
                                    "Normal Range": ["0-100", "0 (Female), 1 (Male)", "0-3", "90-120", "<200", "0 (False), 1 (True)", "0-2", "60-200", "0 (No), 1 (Yes)", "0.0-6.2", "0-2", "0-3", "0-3"],
                                    "Unit": ["Years", "Binary", "Category", "mmHg", "mg/dL", "Binary", "Category", "bpm", "Binary", "mm", "Category", "Count", "Category"]
                                }

                                # Display Table
                                import pandas as pd
                                df = pd.DataFrame(data)
                                st.dataframe(df, use_container_width=True)
                                st.info('Do check your email for more details, Thank You.', icon="ℹ️")

            st.markdown(
            """<div style="position: fixed; bottom: 7.6px; left: 10px; right: 10px; text-align: left; color: grey; font-size: 14px;">
            Made by <span style="font-weight: bold; color: grey;">uzair</span>🎈
            </div>""",
            unsafe_allow_html=True
        )

        with tab2:
            st.subheader('What is Heart Disease?')
            st.write(
            """
            Heart disease refers to various types of conditions that affect the heart's structure and function.
            It is one of the leading causes of death worldwide.
            """
        )

            st.subheader('Types of Heart Disease:')
            st.write("""
            1. **Coronary Artery Disease (CAD):** Blockage of the heart’s major blood vessels.  
            2. **Heart Arrhythmias:** Irregular heartbeats.  
            3. **Heart Valve Disease:** Malfunctioning of heart valves.  
            4. **Congenital Heart Defects:** Heart problems present at birth.
            """)

            st.subheader('Symptoms of Heart Disease:')
            st.markdown("""
            - **Chest pain (Angina):** Discomfort or pressure in the chest.
            - **Shortness of breath:** Difficulty breathing, especially after physical activity.
            - **Fatigue:** Unusual tiredness due to reduced blood flow.
            - **Dizziness or fainting:** May indicate poor circulation or irregular heartbeats.
            - **Swelling in legs or feet:** Due to fluid retention from heart failure.
            - **Heart palpitations:** Rapid or irregular heartbeat.
            """)


            st.subheader('Prevention:')
            st.write("""
            - Eat a healthy diet  
            - Exercise regularly  
            - Manage stress  
            - Avoid smoking and alcohol
            """)
            
            st.subheader('Causes of Heart Disease:')
            st.write("""
            - **High Blood Pressure (Hypertension):** Can damage arteries over time.
            - **High Cholesterol:** Leads to plaque buildup in arteries.
            - **Smoking:** Increases the risk of heart disease.
            - **Diabetes:** Can contribute to artery damage.
            - **Obesity:** Extra weight puts strain on the heart.
            - **Genetics:** Family history can play a role in heart disease.
            """)
            
            st.subheader('Risk Factors:')
            st.write("""
            - **Unhealthy Diet:** Diets high in salt, sugar, and unhealthy fats contribute to heart disease.
            - **Lack of Physical Activity:** Sedentary lifestyles increase risk.
            - **Chronic Stress:** Long-term stress can elevate blood pressure.
            - **Excess Alcohol Consumption:** Weakens heart muscles over time.
            """)
            
            st.subheader('Complications of Heart Disease:')
            st.markdown("""
            - **Heart Attack:** Caused by blocked arteries.  
            - **Stroke:** Reduced blood supply to the brain.  
            - **Heart Failure:** When the heart can't pump blood effectively.  
            - **Kidney Damage:** Poor blood circulation affects kidney function.  
            - **Aneurysm:** Artery walls weaken and bulge, which can be fatal.  
            """)
            
            st.markdown("""
🔗             **Learn More:**  
            - [indian Heart Association](https://indianheartassociation.org/)  
            - [World Health Organization - Heart Disease](https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds))  
            """)

            
            

            st.subheader('Heart Disease Infographic')
                        
            # Path to the uploaded image file

            image_path="Heart_Disease_Infographic.jpg"

            with open("Heart_Disease_Info.png", "rb") as file:
                st.download_button(
                label="⬇️ Download Infographic",
                data=file,
                file_name="Heart_Disease_Infographic.jpg",
                mime="image/jpeg") 

            st.info("For more information, consult a cardiologist.")    
    


    elif(selected == 'Others'):

        tab1, tab2, tab3 = st.tabs(["❓Help", "💬 Feedback", "📩 Contact"])
        
        with tab1:
            placeholder = st.empty()
            st.header("Welcome to the Help Page!",divider='rainbow')
            st.subheader("Diabetes help section:")
            st.write("This application is designed to predict whether a person is diabetic or not based on input data such as the number of pregnancies, glucose level, blood pressure, and other relevant factors.")
            st.write("It works in real-time with 90% accuracy, since it is built using a trained and tested machine learning model.")
            st.write("If you possess true values for pregnancies, BMI, insulin, etc., enter them for precise predictions.")
            st.write("To experience how the application functions, you can use the diabetes data values from kaggle provided below.")
            st.write("In the table Outcome, the Diabetes Status is represented as follows:")
            st.markdown("""
            - **1 indicates that the person is Diabetic.**
            - **0 indicates that the person is Non-Diabetic.**
            """
            )

            # diabetes data table
            Diabetes_data = {
                "Pregnancies": [6, 1, 8, 1, 0, 5, 3, 10, 2],
                "Glucose": [148, 85, 183, 89, 137, 116, 78, 115, 197],
                "BloodPressure": [72, 66, 64, 66, 40, 74, 50, 0, 70],
                "SkinThickness": [35, 29, 0, 23, 35, 0, 32, 0, 45],
                "Insulin": [0, 0, 0, 94, 168, 0, 88, 0, 543],
                "BMI": [33.6, 26.6, 23.3, 28.1, 43.1, 25.6, 31, 35.3, 30.5],
                "PedigreeFunction": [0.627, 0.351, 0.672, 0.167, 2.288, 0.201, 0.248, 0.134, 0.158],
                "Age": [50, 31, 32, 21, 33, 30, 26, 29, 53],
                "Outcome": [1,0,1,0,1,0,1,0,1]
            }

            # Convert sample data to a Pandas DataFrame for better tabular display
            import pandas as pd
            diab_df = pd.DataFrame(Diabetes_data)

            st.caption("Diabetes Data:")
            # st.dataframe(sample_df)
            st.table(diab_df)


            st.subheader("Diabetes Disease Data Info")

            st.write("Download the **Diabetes Disease Data** PDF to learn more about key health indicators, symptoms, and prevention methods.")

            # Path to the uploaded PDF file
            pdf_path = "Diab_Data_info.pdf"

            # Display Download Button
            with open("Diab_Data_info.pdf", "rb") as file:
                st.download_button(
                    label="⬇️ Download Diabetes Disease Data info PDF",
                    data=file,
                    file_name="Diab_Data_info.pdf",
                    mime="application/pdf")

            #for heart 
            placeholder = st.empty()
            with placeholder.container():
                st.header("",divider='rainbow')
                st.subheader("Heart Disease help section:")
                st.write("This application is designed to predict whether a person is heart disease or not based on input data such as the age,  gender, chest pain type , resting blood pressure, and other relevant factors.")
                st.write("It works in real-time with 90% accuracy, since it is built using a trained and tested machine learning model.")
                st.write("If you possess true values for age, gender, chest pain type, etc., enter them for precise predictions.")
                st.write("To experience how the application functions, you can use the heart data values from kaggle provided below.")
                st.write("In the table Outcome, the Diabetes Status is represented as follows:")
                st.markdown("""
            - **1 indicates that the person is Heart Disease.**
            - **0 indicates that the person is not Heart Disease.**
            """
            )



            #heart data table
            heart_data ={
                "age": [63, 37, 41, 56,57,45,68,57,57],
                "sex": [1, 1, 0, 1, 0,1,1,1,0],
                "cp": [3, 2, 1, 1, 0,3,0,0,1],
                "trestbps": [145, 130, 130, 120, 140,110,144,130,130],
                "chol": [233, 250, 204, 236, 241,264,193,131,236],
                "fbs": [1, 0, 0, 0, 0,0,1,0,0],
                "restecg": [0, 1, 0, 1, 1,1,1,1,0],
                "thalach": [150, 187, 172, 178, 123,132,141,115,174],
                "exang":[0,0,0,0,1,0,0,1,0],
                "oldpeak":[2.3,3.5,1.4,0.8,0.2,1.2,3.4,1.2,0],
                "slope":[0,0,2,2,1,1,1,1,1],
                "ca":[0,0,0,0,0,0,2,1,1],
                "thal":[1,1,2,2,3,3,3,3,2],
                "Outcome":[1,1,1,1,0,0,0,0,0]
            }
            
                

            # Convert sample data to a Pandas DataFrame for better tabular display
            import pandas as pd
            heart_df = pd.DataFrame(heart_data)

            st.caption("Heart Data:")
            # st.dataframe(heart_df)
            st.table(heart_df)


            st.subheader("Heart Disease Data Info")

            st.write("Download the **Heart Disease Data** PDF to learn more about key health indicators, symptoms, and prevention methods.")

            # Path to the uploaded PDF file
            pdf_path = "Heart_Data_info.pdf"

            # Display Download Button
            with open("Heart_Data_info.pdf", "rb") as file:
                st.download_button(
                    label="⬇️ Download Heart Disease Data info PDF",
                    data=file,
                    file_name="Heart_Data_info.pdf",
                    mime="application/pdf")


            st.subheader("Note:")

            
            st.info(
                
                "This webpage requests your name and email to send you details about your test results.\n\n"
                "Rest assured, your information is safe and will be kept confidential."
                )
            
        with tab3:
            st.write("Email: [uzerkanza05@gmail.com](mailto:uzerkanza05@gmail.com)")
            st.write(" ")
            
            st.markdown(
            """<div style="position: fixed; bottom: 7.6px; left: 10px; right: 10px; text-align: left; color: grey; font-size: 14px;">
            Made by <span style="font-weight: bold; color: grey;">uzair</span>🎈
            </div>""",
            unsafe_allow_html=True
            ) 
            
        with tab2:
            st.subheader("Your Feedback is Valuable!", divider='rainbow')
            st.write(
                "Please rate your overall experience in using our Web App:")
            rating = st.slider("Rate your experience (1 = Poor, 5 = Excellent)", 1, 5, 3)

            # Convert rating to stars
            stars = "⭐" * rating
            st.write(f"Your Rating: {stars}")
            user_message = st.text_area("Have questions or suggestions? I'd love to hear from you.", height=80, placeholder="Type here...")
            if st.button("Send"):
                formspree_endpoint = "https://formspree.io/f/xyzkwvel"
                data = {"rating": f"{rating} stars ({stars})", "message": user_message}
                response = requests.post(formspree_endpoint, data=data)
                
                if response.status_code == 200:
                    st.success("Message sent successfully!")
                else:
                    st.error("Failed to send message, Please try again.")
            
if __name__ == "__main__":
    main()
