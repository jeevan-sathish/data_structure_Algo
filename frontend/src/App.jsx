import { useState } from "react";

const App = () => {
  const [message, setMessage] = useState([]);
  const [text, setText] = useState("");
  const [editIndex, setEditIndex] = useState(null);

  function handleForm(formdata) {
    const data = formdata.get("text");

    if (editIndex !== null) {
      setMessage((prev) =>
        prev.map((item, index) => (index === editIndex ? data : item)),
      );

      setEditIndex(null);
      setText("");
    } else {
      setMessage((prev) => [...prev, data]);
      setText("");
    }
  }

  function handleEdit(index) {
    setEditIndex(index);

    // Put the selected message into the input
    setText(message[index]);
  }

  return (
    <div>
      <form action={handleForm}>
        <input
          type="text"
          name="text"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />

        <button type="submit">
          {editIndex !== null ? "Update" : "Submit"}
        </button>
      </form>

      <div>
        {message.map((e, i) => (
          <div key={i}>
            <p>{e}</p>

            <button onClick={() => handleEdit(i)}>Edit</button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;
