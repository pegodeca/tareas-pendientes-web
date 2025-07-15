import streamlit  as st 
import funciones

todos = funciones.leer_todos()

def add_tarea():
    tarea = st.session_state["nueva_tarea"] + "\n"
    todos.append(tarea)
    funciones.guardar_todos(todos)
    

st.title("Mi sistema de tareas")
st.subheader("Esta es mi aplicación web")
st.write("Si desea dar por completada una tarea pulse sobre el check que aparece a su izquierda y la tarea desaparece")


for index, todo in enumerate(todos): 
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        funciones.guardar_todos(todos)
        del st.session_state[todo]
        st.rerun()
    
st.text_input(label="", placeholder="Introduzca un tarea",
              on_change=add_tarea, key='nueva_tarea')
