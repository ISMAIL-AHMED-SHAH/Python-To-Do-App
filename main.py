import streamlit as st
import json
import os

# --- Constants ---
FILENAME = "tasks.json"

# --- Function to Load Tasks from JSON File ---
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

# --- Function to Save Tasks to JSON File ---
def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)


# --- App Config ---
st.set_page_config(page_title="📝 To-Do App", layout="centered")
st.image("todo.webp")
st.sidebar.image("https://img.icons8.com/ios-filled/50/000000/todo-list.png", width=90)

# --- App Title ---
st.title("📝 My To-Do List")
st.markdown("Add your tasks, check them off, and stay productive! 💪")

# --- Session State Setup ---
if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()

# --- Add New Task ---
new_task = st.text_input("➕ Add a new task", "")
if st.button("Add Task"):
    if new_task.strip() != "":
        st.session_state.tasks.append({"task": new_task, "completed": False})
        save_tasks(st.session_state.tasks)
        st.success(f"Task added: `{new_task}`")
    else:
        st.warning("Please enter a valid task.")

st.markdown("---")

# --- Task List ---
st.subheader("📋 Your Tasks")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.1, 0.9])
        checked = col1.checkbox("", value=task["completed"], key=f"checkbox_{i}")
        st.session_state.tasks[i]["completed"] = checked
        if checked:
            col2.markdown(
                f"~~{task['task']}~~ <span style='color: green;'>✓ Completed</span>",
                unsafe_allow_html=True
            )
        else:
            col2.markdown(task["task"])
    save_tasks(st.session_state.tasks)  # Auto-save after any checkbox toggle
else:
    st.info("No tasks yet. Add one above to get started! 🏃‍♂️")

# --- Clear Buttons ---
col1, col2 = st.columns(2)
if col1.button("🗑️ Clear Completed Tasks"):
    st.session_state.tasks = [t for t in st.session_state.tasks if not t["completed"]]
    save_tasks(st.session_state.tasks)
    st.success("Completed tasks cleared!")

if col2.button("❌ Clear All Tasks"):
    st.session_state.tasks = []
    save_tasks(st.session_state.tasks)
    st.success("All tasks cleared!")

# --- Sidebar ---
st.sidebar.markdown("---")
st.sidebar.header("💡 Productivity Tips")
st.sidebar.markdown("- Start with small tasks ✅")
st.sidebar.markdown("- Set realistic goals 🎯")
st.sidebar.markdown("- Review your list daily 🔁")
st.sidebar.markdown("- Celebrate completed tasks 🎉")
st.sidebar.markdown("---")

# 📬 Contact Section
st.sidebar.markdown("### 📬 Contact")
st.sidebar.write("📧 [Email Us](mailto:ismailahmedshahpk@gmail.com)")
st.sidebar.write("🔗 [LinkedIn](https://www.linkedin.com/in/ismail-ahmed-shah-2455b01ba/)")
st.sidebar.write("💬 [WhatsApp](https://wa.me/923322241405)")

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='text-align: center; color: grey;'>Build with ❤️ By Ismail Ahmed Shah</p>", unsafe_allow_html=True)
