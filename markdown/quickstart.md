**Welcome to INForcast**, never order too many vaccines again!

INForcast will help you forcast your next Influenza vaccine order.

Leveraging advanced TimeSeries modeling, the app delves into historical vaccination records and seasonal patterns, offering you a tailored prediction for your future Influenza vaccine requirements. Moreover, we provide a comparative analysis of your current year’s vaccination statistics against the data from previous years, giving you a clearer picture of trends and changes. Use our trained model to forcast your vaccination requirement, or train the model with your own data.

![Interface Overview](https://github.com/janduplessis883/project-inforcast/blob/master/images/info2.png?raw=true, width=300)

**Ready to get started?**

Upload your vaccination data, using the upload form. Data can be from SystmOne or Emis, as long as it is in the right format. 

Download the `csv` template below as a guide. 

**Very important** is the format of Event date and Date of Birth, they both need to be in the format **dd-mmm-yyyy** i.e. 28-Jan-2024. If your software exports it in a different format, open your csv with Excel and highlight the date columns, right click and select **format cells**, then **custom** and enter the date format as dd-mmm-yyyy, save your file and then upload to INForcast. 

You could also download the SystmOne Report Template bolow to import in SystmOne Reporting, you will need to **breakdown** your results in the required columns:

```
Vaccination Type
Event Date
Event done at ID
Date of Birth
Patient Count
```

[Download CSV templete](https://github.com/janduplessis883/project-inforcast/blob/master/inforcast/sampledata/csv_template.csv)

[SystmOne Report Template](https://github.com/janduplessis883/project-inforcast/blob/master/images/INForcast-SystmOne-Search.rpt)

**Using Pre-Trained Model**

soon

**Train your own Model**

soon
