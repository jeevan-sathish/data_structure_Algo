import { createSlice } from "@reduxjs/toolkit";
const initialState = {
  todo: [],
};
const TodoSlice = createSlice({
  name: "todo",
  initialState,
  reducers: {
    addTodo: (state, action) => {
      state.todo.push(action.payload);
    },
    deleteTodo: (state, action) => {
      state.todo = state.todo.filter((_, i) => i !== action.payload);
    },
    editTodo: (state, action) => {
      state.todo = state.todo.map((ele, i) =>
        i === action.payload.index ? action.payload.newText : ele,
      );
    },
  },
});

export const { addTodo, deleteTodo, editTodo } = TodoSlice.actions;
export default TodoSlice.reducer;
