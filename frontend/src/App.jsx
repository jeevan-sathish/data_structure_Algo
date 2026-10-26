import axios from "axios";
import { useState } from "react";

const App = () => {
  const [data, setData] = useState();
  const [loading, setLoading] = useState(false);
  const [error, setErroor] = useState("");
  const callapi = async () => {
    setLoading(true);
    try {
      const response = await axios.get("http://localhost:8000/res");
      const result = response.data;
      setTimeout(() => {
        setData(result);
        setLoading(false);
      }, 5000);
    } catch (error) {
      if (axios.isAxiosError(error)) {
        setErroor(error?.response?.data?.detail || "server error 500");
        setLoading(false);
      }
    }
  };

  return (
    <div>
      <button onClick={callapi}>call api</button>
      {error && <p>error</p>}
      <br />
      {loading && <p>loading please wait</p>}
      <div>
        <p>{JSON.stringify(data, null, 2)}</p>
      </div>
    </div>
  );
};

export default App;
