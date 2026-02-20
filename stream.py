import streamlit as st

st.title("BMI CALCULATOR")

wt = st.number_input("Enter your weight in kg", min_value=0.0, format="%f")
ht_unit = st.selectbox("Select height unit", ("cm", "m","feet"))
ht = st.number_input("Enter your height in cm", min_value=0.0, format="%f")
if st.button("Calculate BMI"):
    try:
        if ht_unit == "cm":
            ht = ht / 100
        elif ht_unit == "feet":
            ht = ht * 0.3048
        bmi = wt / (ht ** 2)
        st.write(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            st.write("You are underweight.")    
        elif 18.5 <= bmi < 25:
            st.write("You have a normal weight.")
        elif 25 <= bmi < 30:
            st.write("You are overweight.")
        else:
            st.write("You are obese.")
    except ZeroDivisionError:
        st.error("Height cannot be zero.")