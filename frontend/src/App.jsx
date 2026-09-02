import { useDispatch, useSelector } from "react-redux";
import { increment, decrement, reset } from "./store/CounterSlice";
import { addTodo, deleteTodo, editTodo } from "./store/TodoSlice";
import { useState } from "react";

const App = () => {
  const [text, setText] = useState("");
  const [edit, setEdit] = useState(false);
  const [editIndex, setEditIndex] = useState(null);

  const dispatch = useDispatch();

  const { todo } = useSelector((state) => state.todoList);
  const { count } = useSelector((state) => state.counter);

  function handleChange(e) {
    setText(e.target.value);
  }

  function handleSubmit(e) {
    e.preventDefault();

    if (edit) {
      dispatch(
        editTodo({
          index: editIndex,
          newText: text,
        }),
      );

      setEdit(false);
      setEditIndex(null);
      setText("");
    } else {
      dispatch(addTodo(text));
      setText("");
    }
  }

  function handleEdit(oldtext, index) {
    setEdit(true);
    setText(oldtext);
    setEditIndex(index);
  }

  return (
    <div>
      <div>
        <p>{count}</p>

        <button onClick={() => dispatch(increment(10))}>increment</button>

        <button onClick={() => dispatch(decrement())}>decrement</button>

        <button onClick={() => dispatch(reset())}>reset</button>
      </div>

      <div>
        <form onSubmit={handleSubmit}>
          <input type="text" name="text" value={text} onChange={handleChange} />

          <button type="submit">{edit ? "Update" : "Submit"}</button>
        </form>

        {todo.map((ele, i) => (
          <div key={i}>
            {ele}

            <button onClick={() => handleEdit(ele, i)}>edit</button>

            <button onClick={() => dispatch(deleteTodo(i))}>delete</button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;
