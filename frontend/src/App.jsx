import { api } from "./utils/api";

const App = () => {
  async function handleRequest() {
    try {
      const response = await api.post("/access");
      const { demo_access_token, demo_refresh_token } = response.data;

      console.log(demo_access_token);
      console.log(demo_refresh_token);
      localStorage.setItem("demo_access_token", demo_access_token);
      localStorage.setItem("demo_refresh_token", demo_refresh_token);
    } catch (error) {
      console.log(error);
    }
  }

  async function handleVerify() {
    try {
      const response = await api.get("/verify");
      const result = response.data.result;
      console.log(result);
    } catch (error) {
      console.log(error.response.data.result);
    }
  }
  return (
    <div>
      <button onClick={handleRequest}>send</button>
      <button onClick={handleVerify}>verify</button>
    </div>
  );
};

export default App;
