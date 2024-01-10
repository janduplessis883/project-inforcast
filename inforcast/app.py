import streamlit as st
import pandas as pd
from io import StringIO
import time
import datetime

# from streamlit_extras.metric_cards import style_metric_cards
# from streamlit_extras.stoggle import stoggle

from main import *

st.set_page_config(page_title="INForcast", layout="wide")


html = """
<style>
.gradient-text {
    background: linear-gradient(45deg, #284d74, #d8ad45, #b2d9db, #e16d33);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-size: 48px;
    font-weight: bold;
}
</style>
<div class="gradient-text">INForcast</div>
"""
html2 = """
<style>
.gradient-text {
    background: linear-gradient(45deg, #284d74, #d8ad45, #b2d9db, #e16d33);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-size: 28px;
    font-weight: bold;
}
</style><div class="gradient-text">Historic Influenza vaccine data</div>"""
html3 = """
<style>
.gradient-text {
    background: linear-gradient(45deg, #284d74, #d8ad45, #b2d9db, #e16d33);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-size: 28px;
    font-weight: bold;
</style>
<div class="gradient-text">Influenza vaccine data - 23/24</div>
"""
html4 = """
<style>
.gradient-text {
    background: linear-gradient(45deg, #284d74, #d8ad45, #b2d9db, #e16d33);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-size: 28px;
    font-weight: bold;
</style>
<div class="gradient-text">Quickstart</div>
"""
# Render the HTML in the Streamlit app
st.markdown(html, unsafe_allow_html=True)

# You can use columns to further utilize the wide layout
col1, col2, col3 = st.columns([1, 0.2, 3])

with col1:
    if st.checkbox("Load Sample Data"):
        url = "https://raw.githubusercontent.com/janduplessis883/project-inforcast/master/inforcast/sampledata/sampledata.csv"
        data = pd.read_csv(url)
        data = process_dataframe(data)
        data = update_location(data)

    # Set up the file uploader widget
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # To read file as string:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        data = pd.read_csv(stringio)
        data = process_dataframe(data)
        if not data.empty:
            data = update_location(data)
            # Assuming 'location' is the column name containing the IDs
            location_counts = data["location"].value_counts()
            most_frequent_location = location_counts.idxmax()

            # Create a selectbox with the most frequent location as the default
            selected_location = st.selectbox(
                "Select a location:",
                options=location_counts.index,
                index=location_counts.index.get_loc(most_frequent_location),
            )

            # Creating a slider
            selected_year = st.slider(
                "Select a year",
                min_value=2000,
                max_value=current_year,
                value=(2000, current_year),
            )

            # 4. Load the data based on the selected 'location' ID
            # Filter the DataFrame based on the selected location ID
            filtered_data = data[data["location"] == selected_location]

        df_list = age_groups(filtered_data)
        counts = count_last_year(filtered_data)
        dalta = count_previous_year(filtered_data)
    else:
        st.warning("Upload your CSV file.")

with col2:
    st.write()
with col3:
    # Check if df_list is available and valid for plotting
    if uploaded_file is not None and "df_list" in locals():
        st.markdown(html2, unsafe_allow_html=True)
        plot_age_groups(df_list, df_list[-1]["count"].max())
        current_year = datetime.datetime.now().year
        previous_year = int(current_year) - 1
        st.markdown(html3, unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)

        col1.metric(label="Children ", value=str(counts[0]), delta=str(dalta[0]))
        col2.metric(label="18 - 64 yrs", value=str(counts[1]), delta=str(dalta[1]))
        col3.metric(label="Over 65 yrs", value=str(counts[2]), delta=str(dalta[2]))
    else:
        st.markdown(html4, unsafe_allow_html=True)
        st.markdown(
            """**Welcome to VaxPlanner 360**, your tool for forecasting next year's Influenza vaccination needs! Leveraging advanced TimeSeries modeling, our platform delves into historical vaccination records and seasonal patterns, offering you a tailored prediction for your future Influenza vaccine requirements. Moreover, we provide a comparative analysis of your current year’s vaccination statistics against the data from previous years, giving you a clearer picture of trends and changes.

**Ready to get started?** Upload your vaccination data, and our model will tailor its predictions to your specific dataset. 

To prepare your data, download the [SystmOne Report file here and import to SystmOne Clinical Reporting](https://github.com/janduplessis883/project-vaxplanner-360/blob/master/images/VaxPlanner360%20-%20SystmOne%20Search.rpt) and breakdown the results into the following categories: 
- `Patient System ID`
- `Vaccination Type`
- `Event Date`
- `Event Location ID`
- `Patient Date of Birth`

Once you export this report to a CSV file, an extra column, `Patient Count`, will automatically be included.

**Important**:
>Please **update the format** of the 2 date columns, `Event date` and ` Date of Birth` as follows: 
- Open the csv in Excel, select both columns and right click **Format Cells** 
- Select CUSTOM and update the date format to `dd-mmm-yyyy`. Note you will need to type this as it is not selectable from the dorp-down list.

To initiate the prediction, enter your practice's ODE code into the designated 'Practice Code' field and upload your CSV file. Our app will then dynamically illustrate your historical Influenza Vaccination data, emphasizing the figures from the previous year. Based on this, our model will project the quantity of vaccines your practice might need for the upcoming Influenza vaccination season.

Embrace a smarter approach to vaccination planning with VaxPlanner 360."""
        )
