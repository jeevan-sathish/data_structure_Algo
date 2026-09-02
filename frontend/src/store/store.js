import { configureStore } from "@reduxjs/toolkit";

import CounterReducer from "./CounterSlice";
import TodoReducer from "./TodoSlice";

export const Store = configureStore({
  reducer: {
    counter: CounterReducer,
    todoList: TodoReducer,
  },
});
