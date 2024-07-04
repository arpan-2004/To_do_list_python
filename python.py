import streamlit as st

def main():
    st.title("To-Do List App")
    
    # Initialize task list (using a simple list)
    if 'tasks' not in st.session_state:
        st.session_state.tasks = []

    # Input for adding new tasks
    new_task = st.text_input("Enter task:", key='new_task')
    
    # Add task button
    if st.button("Add Task"):
        if new_task:
            st.session_state.tasks.append(new_task)
            st.success("Task added successfully!")
        else:
            st.warning("Please enter a task.")

    # Display current tasks with option to delete or update
    st.write("## Current Tasks:")
    for index, task in enumerate(st.session_state.tasks):
        task_id = index
        col1, col2, col3, col4 = st.columns([0.1, 2, 0.1, 0.1])
        
        with col2:
            st.write(f"{index + 1}. {task}")
        
        with col3:
            if st.button(f"Update##{task_id}"):
                new_description = st.text_input("Update task:", key=f"update_{task_id}")
                if st.button("Apply Update"):
                    st.session_state.tasks[task_id] = new_description
                    st.success("Task updated successfully!")
        
        with col4:
            if st.button(f"Delete##{task_id}"):
                del st.session_state.tasks[task_id]
                st.success("Task deleted successfully!")
                # After deleting, adjust the index so that they remain consecutive
                st.session_state.tasks = [task for task in st.session_state.tasks]

if __name__ == "__main__":
    main()