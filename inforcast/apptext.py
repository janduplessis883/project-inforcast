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
</style><div class="gradient-text">Historic Influenza vacc data (2000-current)</div>"""


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
<div class="gradient-text">Inf vacc Totals - 23/24</div>
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
<div class="gradient-text">Quick Start Guide</div>
"""

quickguide = """**Welcome to INForcast**, your tool for forecasting next year's Influenza vaccination needs! Leveraging advanced TimeSeries modeling, our platform delves into historical vaccination records and seasonal patterns, offering you a tailored prediction for your future Influenza vaccine requirements. Moreover, we provide a comparative analysis of your current year’s vaccination statistics against the data from previous years, giving you a clearer picture of trends and changes.
    **Ready to get started?** 
    Upload your vaccination data, and our model will tailor its predictions to your specific dataset. 
    To prepare your data, download the [SystmOne Report file here and import to SystmOne Clinical Reporting](https://github.com/janduplessis883/project-vaxplanner-360/blob/master/images/VaxPlanner360%20-%20SystmOne%20Search.rpt) and breakdown the results into the following categories: 
    

    Once you export this report to a CSV file, an extra column, `Patient Count`, will automatically be included.

    **Important**:
    >Please **update the format** of the 2 date columns, `Event date` and ` Date of Birth` as follows: 
    - Open the csv in Excel, select both columns and right click **Format Cells** 
    - Select CUSTOM and update the date format to `dd-mmm-yyyy`. Note you will need to type this as it is not selectable from the dorp-down list.

    To initiate the prediction, enter your practice's ODE code into the designated 'Practice Code' field and upload your CSV file. Our app will then dynamically illustrate your historical Influenza Vaccination data, emphasizing the figures from the previous year. Based on this, our model will project the quantity of vaccines your practice might need for the upcoming Influenza vaccination season.

    Embrace a smarter approach to vaccination planning with VaxPlanner 360."""

guide_code1 = """Vaccination Type
Event Date
Event Location ID
Patient Date of Birth"""
