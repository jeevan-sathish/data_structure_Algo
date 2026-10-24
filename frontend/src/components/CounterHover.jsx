import { useState } from "react";

const CounterHover = () => {
  const [count, setCount] = useState(0);

  function increment() {
    setCount((prev) => prev + 1);
    console.log("rerendered CounterHOver");
  }
  return (
    <div>
      {count}
      <button onMouseOver={increment}>increment</button>
    </div>
  );
};

export default CounterHover;
