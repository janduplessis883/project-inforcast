import pandas as pd


def update_location(df):
    most_frequent_location = df["location"].mode()[0]

    # Replace all other locations with 'Elsewhere'
    df["location"] = df["location"].apply(
        lambda x: x if x == most_frequent_location else "Elsewhere"
    )
    return df


def process_dataframe(df):
    df.rename(
        columns={
            "Vaccination type": "vaccine",
            "Event date": "date",
            "Patient ID": "pt_id",
            "Date of birth": "dob",
            "Event done at ID": "location",
            "Patient Count": "pt_count",
        },
        inplace=True,
    )
    df.dropna(subset="location", inplace=True)
    df["date"] = pd.to_datetime(df["date"], format="%d-%b-%Y")
    df["dob"] = pd.to_datetime(df["dob"], format="%d-%b-%Y")
    df["age_at_vaccine"] = df["date"].dt.year - df["dob"].dt.year
    df = df[df["age_at_vaccine"] > 0]
    return df


def to_timeseries_full(df, column, time_period="M"):
    # Resample and count occurrences in each period
    m_count = df.resample(time_period, on=column).size()
    # Convert to DataFrame
    m_count_df = m_count.reset_index()
    # Rename columns
    m_count_df.columns = ["date", "count"]
    return m_count_df
