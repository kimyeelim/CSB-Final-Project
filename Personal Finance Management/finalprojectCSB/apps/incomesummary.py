import streamlit as st
import pandas as pd

def app():
    st.title("Income Summary")

    # Read file and summarize income.
    summarize_income("income.csv")

def summarize_income(income_file_path):
    st.subheader("Summary of Income")
    df = pd.read_csv(income_file_path, names=["Source", "Amount", "Category"])
    
    total_income = df["Amount"].sum()
    st.write(f"Total Income: ${total_income:.2f}")
    
    df_expenses = pd.read_csv("expenses.csv", names=["Name", "Amount", "Category"])
    total_expenses = df_expenses["Amount"].sum()

    df_income = pd.read_csv("income.csv", names=["Source", "Amount", "Category"])
    total_income = df_income["Amount"].sum()

    # Calculate remaining budget
    remaining_budget = total_income - total_expenses
    st.write(f"remaining_budget: ${remaining_budget:.2f}")

    st.subheader("Detailed Income")
    st.write(df)

