import streamlit as st
from blood_donor_views import BloodDonorManager

donor_instance=BloodDonorManager()
tab1, tab2 = st.tabs(["ADD","VIEW"])

with tab1 :
    st.title("add new blood donor")
    name=st.text_input("enter blood donor name:")
    blood_group=st.text_input("enter blood donor group")
    phone=st.text_input("enter phone number")
    city=st.text_input("enter the city")
    last_donation=st.text_input("enter the last donation")
    if st.button("add new blood donor"):
        donor_instance.post(name=name,blood_group=blood_group,phone=phone,city=city,last_donation=last_donation)
        st.success("add successfully")


with tab2:
    st.title("view blood donor details")








