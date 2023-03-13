import streamlit as st
import functions as f


def add_todo():
    newtodo = st.session_state["new_todo"] + "\n"
    todos.append(newtodo)
    f.savefile_txt(todos, "todos.txt")
    st.session_state["new_todo"] = ""


todos = f.get_todo_txt("todos.txt")

st.title("Neil's To-Do Web App")
st.subheader("Neil's first self-created Python web-app")
st.write("This app is to increase my productivity")

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(i)
        f.savefile_txt(todos)
        del st.session_state[todo]
        st._rerun()

st.text_input(label="To Do Input", label_visibility="hidden",
              placeholder="Add a new to do...",
              on_change=add_todo, key="new_todo")


# st.session_state