# Smart Fridge Platform

**A. Overview**

This project was selected for pitching on the 2024 GenAI Hackathon for Sustainable Development Goals. It introduces a platform called 'Smart Fridge' which is presented as a solution for effective inventory managment such that no food bought and stored in fridge will go waste due to expiration. It works by offering real time recipe recommendations utilizing items going to expire soon and also tailoring to user preferences.


**B. Input/Output of products in Database**

The platform offers two ways to manage inventory (Input/ Output):  
1. **Selecting items** when added or removed from the fridge.  
2. **Barcode scanning** to quickly track items.



**C. Features**

1. **Chatbot:** 
  - Ask the chatbot about what’s inside the fridge, expiration dates, or what to cook with the available ingredients.
  
2. **Smart Recipe Generator:**
  - Recommends recipes based on available ingredients.
  - Automatically generates a shopping list for missing ingredients.
    
3. **Dashboard**
  - A dashboard is available to provide insights into the fridge's contents, using charts and other visual representations.




## Installation

### Prerequisites
- Python 3.7 or later
- Required libraries (you can install them via pip):
  ```bash
  pip install -r requirements.txt

## Setup
- Clone the repository
```bash
git clone https://github.com/christopher540/smart-fridge-hack4sdg-2024-final.git
```
- Navigate to the project directory:
```bash
cd smart-fridge-hack4sdg-2024-final
```
- Make a .env file with the content
```bash
API_KEY= 'Your API Key'
```
- Run the main application:
```bash
streamlit run main.py
```




