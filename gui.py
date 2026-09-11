import streamlit as st
from blood_donor_views import BloodDonorManager

donor_instance=BloodDonorManager()
tab1, tab2 = st.tabs(["ADD","VIEW"])

with tab1 :
    st.title("add new blood donor")
    name=st.text_input("enter blood donor name:")
    blood_group=st.selectbox("eselect your blood group",["A+","B+","O+","AB+","A-","B-","O-","AB-"])
    phone=st.text_input("enter phone number")
    city=st.text_input("enter the city")
    last_donation=st.date_input("enter the last donation date(yyyy/mm/dd)")
    if st.button("add new blood donor"):
        donor_instance.post(name=name,blood_group=blood_group,phone=phone,city=city,last_donation=last_donation)
        st.success("add successfully")


with tab2:
    st.title("view blood donor details")
    records=donor_instance.get()
    if records:
        st.table(records)
    else:
        st.warning("no records found..!")








