import streamlit as st
import pandas as pd

def app():
    st.title("Expense Summary")

    # Read file and summarize expenses.
    summarize_expenses("expenses.csv")

def summarize_expenses(expense_file_path):
    st.subheader("Summary of Expenses")
    df = pd.read_csv(expense_file_path, names=["Name", "Amount", "Category"])
    
    total_expenses = df["Amount"].sum()
    st.write(f"Total Expenses: ${total_expenses:.2f}")
    
    df_expenses = pd.read_csv("expenses.csv", names=["Name", "Amount", "Category"])
    total_expenses = df_expenses["Amount"].sum()

    df_income = pd.read_csv("income.csv", names=["Source", "Amount", "Category"])
    total_income = df_income["Amount"].sum()

    # Calculate remaining budget
    remaining_budget = total_income - total_expenses
    st.write(f"Remaining Budget: ${remaining_budget:.2f}")
   
    
    st.subheader("Detailed Expenses")
    st.write(df)

