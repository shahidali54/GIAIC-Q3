import streamlit as st

def unit_converter():
    st.title("Unit Converter")
    st.write("Easily convert different measurement units")

    categories = {
        "Length": {
            "Meters": 1.0, "Kilometers": 0.001, "Centimeters": 100.0, "Millimeters": 1000.0,
            "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28084, "Inches": 39.3701
        },
        "Weight/Mass": {
            "Kilograms": 1.0, "Grams": 1000.0, "Milligrams": 1000000.0, "Metric Tons": 0.001,
            "Pounds": 2.20462, "Ounces": 35.274, "Stones": 0.157473
        },
        "Temperature": {
            "Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"
        },
        "Area": {
            "Square Meter": 1.0, "Square Kilometer": 0.000001, "Square Centimeter": 10000.0,
            "Square Millimeter": 1000000.0, "Square Mile": 3.861e-7, "Square Yard": 1.19599,
            "Square Foot": 10.7639, "Square Inch": 1550.0, "Acre": 0.000247105, "Hectare": 0.0001
        },
        "Volume": {
            "Cubic Meter": 1.0, "Cubic Centimeter": 1000000.0, "Liter": 1000.0, "Milliliter": 1000000.0,
            "Gallon (US)": 264.172, "Quart (US)": 1056.69, "Pint (US)": 2113.38, "Cup (US)": 4226.75,
            "Fluid Ounce (US)": 33814.0, "Cubic Inch": 61023.7, "Cubic Foot": 35.3147
        },
        "Speed": {
            "Meter per second": 1.0, "Kilometer per hour": 3.6, "Mile per hour": 2.23694,
            "Foot per second": 3.28084, "Knot": 1.94384
        },
        "Time": {
            "Second": 1.0, "Millisecond": 1000.0, "Microsecond": 1000000.0, "Minute": 1/60.0,
            "Hour": 1/3600.0, "Day": 1/86400.0, "Week": 1/604800.0, "Month": 1/2592000.0,
            "Year": 1/31536000.0
        }
    }

    chosen_category = st.selectbox("Choose a category", list(categories.keys()))
    units = list(categories[chosen_category].keys())

    col1, col2 = st.columns(2)

    with col1:
        from_unit = st.selectbox("From", units)
    with col2:
        to_unit = st.selectbox("To", units)

    input_value = st.number_input("Enter value", value=1.0)

    if st.button("Convert"):
        base_value = input_value / categories[chosen_category][from_unit]
        result = base_value * categories[chosen_category][to_unit]

        st.markdown(
            f"""
            <div style="text-align: center; padding: 20px; border: 2px solid #ddd; border-radius: 10px; background-color: #f9f9f9;">
                <h2 style="color: #007BFF;">{input_value} {from_unit} = {result:.2f} {to_unit}</h2>
                <p style="font-size: 16px; color: #666;"><strong>Formula:</strong> Multiply the {from_unit} value by {categories[chosen_category][to_unit]}</p>
            </div>
            """, 
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    unit_converter()

