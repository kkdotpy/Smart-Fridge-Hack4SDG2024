import streamlit as st
from PIL import Image
import pickle
import pandas as pd
from datetime import datetime, timedelta


def remove_vegetable_page():
    # Set the title of the app
    st.title("Remove Vegetable")

    images = [
    'vegetable_image/bokchoy.jpeg',
    'vegetable_image/brocolli.jpeg',
    'vegetable_image/cabbage.jpeg',
    'vegetable_image/carrot.jpeg',
    'vegetable_image/potato.jpeg',
    'vegetable_image/spinach.jpeg'
    ]

    # Corresponding item names
    item_names = ["Bokchoy", "Brocolli", "Cabbage", "Carrot", "Potato", "Spinach"]
    expiration=[1,2,3,4,5,6]

    # Initialize session state for quantities if it doesn't exist
    if 'quantities' not in st.session_state:
        st.session_state.quantities = [0] * len(images)


    # Desired height for the images
    desired_height = 200

    # Create a 2x3 column layout
    cols = st.columns(3)

    for i in range(6):
        with cols[i % 3]:
            # Open the image using PIL
            img = Image.open(images[i])
            
            # Resize the image
            img_resized = img.resize((200, 200))

            # Display the resized image
            st.image(img_resized, use_column_width=True)
            st.session_state.quantities[i] = st.number_input(
                label='Quantity', 
                key=f'quantity_{i}', 
                min_value=0, 
                value=st.session_state.quantities[i],
                step=1
            )
        
    with open('database.pkl','rb') as f:
        df=pickle.load(f)

    if st.button(label='Submit'):
        st.write("You have removed:")
        for i in range(len(images)):

            if st.session_state.quantities[i] > 0:
                st.write(f"{item_names[i]}: {st.session_state.quantities[i]}")
                quantity = st.session_state.quantities[i]

                while quantity > 0:
                    # Remove the oldest items (Most Recent Expiry date) First
                    oldest_df = df[(df['Item'] == item_names[i]) & (df['Category'] == 'Vegetable')]
                    if oldest_df.empty:
                        break
                    oldest_item_idx = df[(df['Item'] == item_names[i]) & (df['Category'] == 'Vegetable')]['Expiration'].idxmin()

                    df.loc[oldest_item_idx, 'Quantity'] -= quantity
                    quantity = -df.loc[oldest_item_idx, 'Quantity']
                    if quantity >= 0:
                        df = df.drop(oldest_item_idx)
                    

        st.session_state.clear()

    with open('database.pkl','wb') as f:
        pickle.dump(df,f)

    st.dataframe(df)