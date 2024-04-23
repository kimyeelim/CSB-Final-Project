import streamlit as st
from expense import Expense  # Assuming Expense class is defined in expense.py

def app():
    st.title("Expense Tracker")

    # Get user input for expense.
    expense = get_user_expense()

    # Button to save the expense
    if st.button("Save Expense"):
        save_expense_to_file(expense, "expenses.csv")
        st.success("Expense saved successfully!")

def get_user_expense():
    st.subheader("Enter Expense Details")
    expense_name = st.text_input("Enter expense name:")
    expense_amount = st.number_input("Enter expense amount:", min_value=0.0, step=0.01)
    expense_categories = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Clothing",
        "Education",
        "Other",
    ]
    selected_category = st.selectbox("Select a category:", expense_categories)

    new_expense = Expense(
        name=expense_name,
        category=selected_category,
        amount=expense_amount
    )
    return new_expense

def save_expense_to_file(expense: Expense, expense_file_path):
    st.subheader("Saving User Expense")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")
