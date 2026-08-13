import { useState } from "react";

const App = () => {
  const [inp, setInp] = useState("");
  const [chat, setChat] = useState([]);
  const [loading, setLoading] = useState(false);
  const [newchat, setNewchat] = useState([]);

  function handleChange(e) {
    setInp(e.target.value);
  }

  async function handleSubmit() {
    setChat((prev) => [...prev, { message: inp, role: "user" }]);
    setLoading(true);
    setInp(" ");
    try {
      const response = await fetch("http://localhost:3000/message", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: inp,
        }),
      });
      const result = await response.json();
      setChat((prev) => [...prev, { message: result.response, role: "bot" }]);
      setLoading(false);
    } catch (error) {
      console.log(error);
    } finally {
      setLoading(false);
    }
  }

  function handleNewChat() {
    setNewchat((prev) => [...prev, chat]);
    setChat([]);
  }
  return (
    <div>
      <input type="text" name="inp" value={inp} onChange={handleChange} />

      <button onClick={handleSubmit}>submit</button>
      <button onClick={handleNewChat}>new chat</button>
      <div style={{ color: "pink" }}>
        {newchat.map((ele) =>
          ele.map((e, i) => (
            <div
              key={i}
              style={{
                display: "flex",
                justifyContent: e.role === "user" ? "flex-end" : "flex-start",
                margin: "10px",
              }}
            >
              <div
                style={{
                  padding: "10px",
                  backgroundColor:
                    e.role === "user" ? "lightblue" : "lightgray",
                  borderRadius: "10px",
                }}
              >
                {e.message}
              </div>
            </div>
          )),
        )}
      </div>

      <div style={{ color: "red" }}>
        {chat.map((ele, i) => (
          <div key={i}>
            {ele.role}: {ele.message}
          </div>
        ))}

        {loading && <div>loading....</div>}
      </div>
    </div>
  );
};

export default App;
