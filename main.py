import pandas as pd
import numpy as np
import pickle
import streamlit as st

st.title("It will predict the house price in hyderbad")




facing_list=['facingDesc_East', 'facingDesc_West', 'facingDesc_North', 'facingDesc_North-East', 'facingDesc_South', "facingDesc_Don't Know", 'facingDesc_South-East', 'facingDesc_North-West', 'facingDesc_South-West']
furnish_list=['furnishing_Semi', 'furnishing_Unfurnished', 'furnishing_Full']
locality_list=['locality_Kondapur', 'locality_Kukatpally', 'locality_Gachibowli', 'locality_Miyapur', 'locality_Manikonda', 'locality_Nizampet', 'locality_Madhapur', 'locality_Hafeezpet', 'locality_Chanda Nagar', 'locality_Serilingampally', 'locality_Pragathi Nagar', 'locality_Banjara Hills', 'locality_Kothaguda', 'locality_Begumpet', 'locality_Kokapet', 'locality_Narsingi', 'locality_Attapur', 'locality_Madinaguda', 'locality_Shaikpet', 'locality_Ramachandra Puram', 'locality_Puppalguda', 'locality_Bachupally', 'locality_Toli Chowki', 'locality_Bandlaguda Jagir', 'locality_Nagole', 'locality_Nanakaramguda', 'locality_Puppalaguda', 'locality_Borabanda', 'locality_Mehdipatnam', 'locality_Manikonda Jagir', 'locality_Gajularamaram', 'locality_Boduppal', 'locality_Kothapet', 'locality_Uppal', 'locality_Hyderabad', 'locality_Nanakramguda', 'locality_Jubilee Hills', 'locality_Moosapet', 'locality_Saroornagar', 'locality_Hitec City', 'locality_Alwal', 'locality_Vanasthalipuram', 'locality_Pocharam', 'locality_Peerzadiguda', 'locality_Moti Nagar', 'locality_Tellapur', 'locality_Sainikpuri', 'locality_Kapra', 'locality_Beeramguda', 'locality_Nallagandla', 'locality_Somajiguda', 'locality_Amberpet', 'locality_Secunderabad', 'locality_West Marredpally', 'locality_Himayatnagar', 'locality_Malkajgiri', 'locality_Gopanpally', 'locality_Kavadiguda', 'locality_Nacharam', 'locality_Yousufguda', 'locality_Dilsukhnagar', 'locality_Kompally', 'locality_Old Bowenpally', 'locality_Ameerpet', 'locality_Gopanapalli', 'locality_Ameenpur', 'locality_New Nallakunta', 'locality_Adibatla', 'locality_Whitefields', 'locality_Nagaram', 'locality_Upparpally', 'locality_LB Nagar', 'locality_Moula Ali', 'locality_Lingampally']
parking_list=['parking_BOTH', 'parking_TWO_WHEELER', 'parking_FOUR_WHEELER', 'parking_NONE']
water_supply_list=['waterSupply_CORP_BORE', 'waterSupply_CORPORATION', 'waterSupply_BOREWELL']



# furnish_cols=list(3)
# locality_cols=list(74)
# parking_cols=list(4)
# water_supply_cols=list(3)


non_cat_cols=['bathroom', 'property_age', 'property_size', 'totalFloor','amenities']
amenities_list=['swimmingPool', 'lift', 'gym', 'internet', 'AC', 'club', 'INTERCOM', 'servant', 'security']

bathrooms=st.number_input("Enter a number of Bathrooms you need",0,5)
property_age=st.number_input("Enter the property age",0,12)
property_size=st.number_input("Enter the property size",0,5000)
totalFloor=st.number_input("Enter the total number of floors",0,100)

facing=st.selectbox("Enter your House Facing",facing_list)
facing_cols=pd.Series( facing_list)
facing_cols=np.where(facing_cols==facing.strip() ,True,False)

furnishing=st.selectbox("Enter your House Furnishing type",furnish_list)
furnishing_cols=pd.Series(furnish_list)
furnishing_cols=np.where(furnishing_cols==furnishing.strip() ,True,False)

locality=st.selectbox("Enter your locality",locality_list)
locality_cols=pd.Series(locality_list)
locality_cols=np.where(locality_cols==locality.strip() ,True,False)

parking=st.selectbox("Enter your Parking type",parking_list)
parking_cols=pd.Series(parking_list)
parking_cols=np.where(parking_cols==parking.strip() ,True,False)
# print(type(parking_cols))

waterSupply=st.selectbox("Enter your Water Supply type",water_supply_list)
water_supply_cols=pd.Series(water_supply_list)
water_supply_cols=np.where(water_supply_cols==waterSupply.strip() ,True,False)

amenities=st.multiselect("Select amenities", amenities_list)
amenities=len(amenities)
input_data_list=[bathrooms,property_age,property_size,totalFloor]+list(facing_cols)+list(furnishing_cols)+list(locality_cols)+list(parking_cols)+list(water_supply_cols)+[amenities]
if st.button("Predict House Price"):
    loaded_model=pickle.load(open("finalized_model.sav","rb"))
    prediction = loaded_model.predict(np.array(input_data_list).reshape(1, -1))
    print(prediction)
    st.title("Predicted Value is : " + str(round(prediction[0],2))+ " RS")






