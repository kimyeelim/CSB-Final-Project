import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def app():
    st.title("Analysis")

    # Read expenses and income data
    df_expenses = pd.read_csv("expenses.csv", names=["Name", "Amount", "Category"])
    total_expenses = df_expenses["Amount"].sum()

    df_income = pd.read_csv("income.csv", names=["Source", "Amount", "Category"])
    total_income = df_income["Amount"].sum()

    # Create pie chart for expense summary
    fig_expenses = go.Figure(data=[go.Pie(labels=df_expenses["Category"], values=df_expenses["Amount"])])
    # fig_expenses.update_layout(title="Expense Summary")

    # Create pie chart for income summary
    fig_income = go.Figure(data=[go.Pie(labels=df_income["Category"], values=df_income["Amount"])])
    fig_income.update_layout(title="I ")

    # Display the expense summary graph
    st.subheader("Expense Summary")
    st.plotly_chart(fig_expenses, use_container_width=True)

    # Display the income summary graph
    st.subheader("Income Summary")
    st.plotly_chart(fig_income, use_container_width=True)
