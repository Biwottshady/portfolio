null=None
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import os

# --- Constants ---
CSV_PATH = r"C:\Users\PC\Downloads\Land casual workers tracker - daily_attendance_report.csv"
STANDARD_RATE = 750

# --- Load Data from CSV ---
@st.cache_data
def load_data():
    if os.path.exists(CSV_PATH):
        df = pd.read_csv(CSV_PATH)
        df["Task Date"] = pd.to_datetime(df["Task Date"], dayfirst=True, errors="coerce")
        df["Date of Monday"] = pd.to_datetime(df["Date of Monday"], dayfirst=True, errors="coerce")

        return df
    else:
        st.error(f"File not found: {CSV_PATH}")
        return pd.DataFrame()

# --- Page Setup ---
st.set_page_config(page_title="Casuals Payment Dashboard", layout="wide")
st.title("💰 Weekly Financial Dashboard for Land Casual Workers")

# Load data
df = load_data()

# --- Sidebar Filters ---
# --- Sidebar Filters ---
if not df.empty:
    st.sidebar.header("Filter Options")
    min_date = df["Date of Monday"].min().date()
    max_date = df["Date of Monday"].max().date()

    today = datetime.now().date()

    # Ensure the defaults are within the allowed range
    default_start = max(min_date, today - timedelta(days=7))
    default_end = min(max_date, today)

    # If start > end (e.g. today > max_date), reverse to stay in bounds
    if default_start > default_end:
        default_start = min_date
        default_end = max_date

    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(default_start, default_end),
        min_value=min_date,
        max_value=max_date
    )

    farmer_options = sorted(df["Worker Name"].dropna().unique())
    selected_farmer = st.sidebar.selectbox("Filter by Farmer", options=["All"] + list(farmer_options))

    supervisor_options = sorted(df["Field Officer"].dropna().unique())
    selected_supervisor = st.sidebar.selectbox("Filter by Supervisor", options=["All"] + list(supervisor_options))

    # --- Apply Filters ---
    filtered_df = df.copy()

    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = filtered_df[
            (filtered_df["Date of Monday"].dt.date >= start_date) & 
            (filtered_df["Date of Monday"].dt.date <= end_date)
        ]

    if selected_farmer != "All":
        filtered_df = filtered_df[filtered_df["FARMER_NAME"] == selected_farmer]

    if selected_supervisor != "All":
        filtered_df = filtered_df[filtered_df["Field Officer"] == selected_supervisor]

    filtered_df = filtered_df.drop_duplicates(subset=["ID Number", "Date of Monday"])

    # --- Metrics ---
    if not filtered_df.empty:
        total_days = len(filtered_df)
        total_payment = total_days * STANDARD_RATE

        filtered_df["Gender"] = filtered_df["Gender"].str.strip().str.lower()
        male_workers = filtered_df[filtered_df["Gender"] == "male"]["ID Number"].nunique()
        female_workers = filtered_df[filtered_df["Gender"] == "female"]["ID Number"].nunique()
        total_workers = filtered_df["ID Number"].nunique()

        with st.container():
            a, b, c = st.columns(3)
            a.metric("🗓️ Total Days Worked", total_days)
            b.metric("💸 Total Amount Payable", f"KES {total_payment:,.2f}")
            c.metric("👥 Total Workers", total_workers)

        with st.container():
            x, _, y, _ = st.columns(4)
            x.metric("🧍‍♂️ Male Workers", male_workers)
            y.metric("🧍‍♀️ Female Workers", female_workers)

        # --- Summary Table ---
        st.subheader("📊 Weekly Payment Summary")
        unique_dates = sorted(filtered_df["Date of Monday"].dt.date.unique())
        date_columns = [str(date) for date in unique_dates]

        summary_df = filtered_df.groupby([
            "Phone No", "ID Number", "Worker Name", "Farmer Name", "Field Officer"
        ]).agg({
            "Date of Monday": "nunique"
        }).reset_index()

        summary_df.rename(columns={"Date of Monday": "TOTAL_DAYS"}, inplace=True)
        summary_df["TOTAL_PAYMENT"] = summary_df["TOTAL_DAYS"] * STANDARD_RATE

        for date in unique_dates:
                date_str = str(date)
                worked_on_date = filtered_df[filtered_df["Date of Monday"].dt.date == date]
                workers_on_date = worked_on_date[["Phone No", "ID Number"]].drop_duplicates()
            
                summary_df[date_str] = summary_df.apply(
                    lambda row: "1" if ((row["Phone No"], row["ID Number"]) in 
                            zip(workers_on_date["Phone No"], workers_on_date["ID Number"])) else "",
                    axis=1
    )

        summary_df["Amount"] = STANDARD_RATE
        columns_order = ["Phone No", "ID Number", "Worker Name", "Farmer Name", "Field Officer", "Amount"] + date_columns + ["TOTAL_DAYS", "TOTAL_PAYMENT"]
        summary_df = summary_df[columns_order]

        summary_df.columns = [
            "Phone No", "ID NO", "Name", "Land Owner", "Supervisor", "Amount"
        ] + date_columns + ["Total Number of Days", "Total Payment"]

        summary_df["Amount"] = summary_df["Amount"].apply(lambda x: f"{x:,.2f}")
        summary_df["Total Payment"] = summary_df["Total Payment"].apply(lambda x: f"{x:,.2f}")

        st.dataframe(summary_df, use_container_width=True)

        csv = summary_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Summary Report (CSV)",
            data=csv,
            file_name="weekly_payment_summary.csv",
            mime="text/csv"
        )

        # --- Detailed Records Table ---
        st.subheader("📋 Detailed Records")
        st.dataframe(
            filtered_df[["Date of Monday", "Worker Name", "ID Number", "Phone No", "Farmer Name", "Field Officer"]]
            .sort_values("Date of Monday", ascending=False)
            .rename(columns={
                "Date of Monday": "Date",
                "Worker Name": "Name",
                "ID Number": "ID No",
                "Phone No": "Phone No",
                "Farmer Name": "Land Owner",
                "Field Officer": "Supervisor"
            }),
            use_container_width=True
        )
    else:
        st.info("No data available for the selected filters.")
else:
    st.warning("CSV file is missing or empty.")