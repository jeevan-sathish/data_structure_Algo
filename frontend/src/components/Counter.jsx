import { useState } from "react";

const Counter = () => {
  const [count, setCount] = useState(0);

  function increment() {
    setCount((prev) => prev + 1);
  }
  return (
    <div>
      {count}
      <button onClick={increment}>increment</button>
    </div>
  );
};

export default Counter;
