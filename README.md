# House-Price-Prediction-Project

### Project Description
The goal of this project is to build a predictive model to estimate house prices based on various features such as house area, number of bedrooms and bathrooms, presence of amenities (like air conditioning, hot water heating, guest rooms, etc.), and proximity to a main road.

I have also built a web application that  allows users to predict house prices based on various property features using a Support Vector Regressor (SVR) model. The app is built using Streamlit for the frontend, allowing users to input house details and receive a predicted price based on the trained model.

![image](https://github.com/user-attachments/assets/42744036-5cae-4562-b88c-b5153ccfb04d)

### Features
- Predict house prices based on property characteristics like area, bedrooms, bathrooms, parking, and more.
- Simple and intuitive user interface built with Streamlit.
- Efficient and accurate predictions using a pre-trained SVR model.

### Installation
Follow these steps to set up and run the project locally:

##### 1. Clone the repository
```
git clone https://github.com/Arfa-Ahsan/House-Price-Prediction-Project.git
cd House-Price-Prediction-Project
```

##### 2. Create a virtual environment and activate it (optional but recommended)
```
python -m venv env
source env/bin/activate   # For Linux/macOS
env\Scripts\activate      # For Windows
```
##### 3. Install dependencies
```
pip install -r requirements.txt
```

##### 4.Run the Jupyter Notebook 
```
jupyter notebook notebooks/House price prediction.ipynb
```
##### 5.Run the Streamlit app
```
streamlit run house_price_prediction.py
```
