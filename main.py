import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"]) 

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    df = pd.read_csv(uploaded_file)
    st.subheader('Data Preview')
    st.write(df.head())

    st.subheader('Data Summary')
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select columns for filtering", columns)
    unique_values = df[selected_columns].unique()
    selected_values = st.selectbox("Select values for filtering", unique_values)

    filtered_df = df[df[selected_columns] == selected_values]
    st.success("Filtered Data")
    st.write(filtered_df)

    st.subheader("Data Visualization")
    x_column = st.selectbox("Select X-axis column", columns)
    y_column = st.selectbox("Select Y-axis column", columns)

    if x_column == y_column:
        st.warning("Please select different columns for X and Y axes.")
    elif st.button("Generate plot"):
        try:
            # Try converting x_column to datetime
            filtered_df[x_column] = pd.to_datetime(filtered_df[x_column], errors='ignore')
            fig, ax = plt.subplots()
            ax.plot(filtered_df[x_column], filtered_df[y_column])
            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)
            ax.set_title(f"{y_column} vs {x_column}")
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Could not plot the graph: {e}")
else:
    st.info("Please upload a CSV file to begin.")
