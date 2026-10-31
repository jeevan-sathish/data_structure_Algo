import axios from "axios";
import { useState } from "react";

const App = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  console.log(data);
  const id = 2;
  const callapi = async () => {
    setLoading(true);
    setError("");

    try {
      const response = await axios.post(`http://localhost:8000/user/${id}`, {
        name: "prajwal",
      });

      setData(response.data.user);
    } catch (error) {
      if (axios.isAxiosError(error)) {
        setError(
          error.response?.data?.detail?.[0]?.msg ||
            error.response?.data?.detail ||
            "Server error",
        );
      } else {
        setError("Something went wrong");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <button onClick={callapi} disabled={loading}>
        Call API
      </button>

      {loading && <p>Loading please wait...</p>}

      {error && <p>{error}</p>}

      {data && <p>{JSON.stringify(data, null, 2)}</p>}
    </div>
  );
};

export default App;
