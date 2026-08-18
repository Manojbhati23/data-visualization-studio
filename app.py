import streamlit as st
import pandas as pd
import numpy as np

from modules.charts import (
    line_chart,
    scatter_chart,
    bar_chart,
    histogram,
    boxplot,
    heatmap,
    scatter_3d
)

from modules.eda import (
    data_summary,
    statistics,
    missing_values,
    data_types
)

from modules.export import generate_pdf
from modules.ml import train_model

st.set_page_config(
    page_title="Data Visualization Studio",
    layout="wide"
)

st.title("📊 Data Visualization Studio Pro")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset Loaded")

    st.subheader("Dataset")

    st.dataframe(df)

    st.divider()

    st.subheader("EDA Report")

    summary = data_summary(df)

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Rows",
        summary["rows"]
    )

    col2.metric(
        "Columns",
        summary["columns"]
    )

    col3.metric(
        "Missing Values",
        summary["missing"]
    )

    st.write("### Statistics")

    st.dataframe(
        statistics(df)
    )

    st.write("### Missing Values")

    st.dataframe(
        missing_values(df)
    )

    st.write("### Data Types")

    st.dataframe(
        data_types(df)
    )

    numeric_cols = df.select_dtypes(
        include=np.number
    ).columns.tolist()

    st.divider()

    chart_type = st.selectbox(
        "Choose Chart",
        [
            "Line",
            "Scatter",
            "Bar",
            "Histogram",
            "Boxplot",
            "Heatmap",
            "3D Scatter"
        ]
    )

    fig = None

    if chart_type == "Heatmap":

        fig = heatmap(df)

    elif chart_type == "Histogram":

        y = st.selectbox(
            "Column",
            numeric_cols
        )

        fig = histogram(
            df,
            y
        )

    elif chart_type == "Boxplot":

        y = st.selectbox(
            "Column",
            numeric_cols
        )

        fig = boxplot(
            df,
            y
        )

    elif chart_type == "3D Scatter":

        x = st.selectbox(
            "X Axis",
            numeric_cols
        )

        y = st.selectbox(
            "Y Axis",
            numeric_cols,
            index=1
        )

        z = st.selectbox(
            "Z Axis",
            numeric_cols,
            index=2
        )

        fig = scatter_3d(
            df,
            x,
            y,
            z
        )

    else:

        x = st.selectbox(
            "X Axis",
            df.columns
        )

        y = st.selectbox(
            "Y Axis",
            numeric_cols
        )

        if chart_type == "Line":
            fig = line_chart(df, x, y)

        elif chart_type == "Scatter":
            fig = scatter_chart(df, x, y)

        elif chart_type == "Bar":
            fig = bar_chart(df, x, y)

    if fig:
        st.pyplot(fig)

        fig.savefig("chart.png")

        with open(
            "chart.png",
            "rb"
        ) as f:

            st.download_button(
                "Download PNG",
                data=f,
                file_name="chart.png"
            )

    st.divider()

    st.subheader("Machine Learning Demo")

    if len(numeric_cols) >= 2:

        x_col = st.selectbox(
            "Feature Column",
            numeric_cols
        )

        y_col = st.selectbox(
            "Target Column",
            numeric_cols,
            index=1
        )

        prediction = train_model(
            df,
            x_col,
            y_col
        )

        st.success(
            f"Prediction when X=10 : {prediction:.2f}"
        )

    st.divider()

    if st.button("Generate PDF Report"):

        pdf_path = generate_pdf()

        with open(
            pdf_path,
            "rb"
        ) as file:

            st.download_button(
                "Download PDF",
                file,
                file_name="report.pdf"
            )