import React, { useState, useCallback } from "react";

const Child = React.memo(({ handleClick }) => {
  console.log("Child rendered");

  return <button onClick={handleClick}>Child Button</button>;
});

function Counter() {
  const [count, setCount] = useState(0);

  const handleClick = useCallback(() => {
    console.log("Child clicked");
  }, []);

  return (
    <div>
      <h1>{count}</h1>

      <button onClick={() => setCount((p) => p + 1)}>Increment</button>

      <Child handleClick={handleClick} />
    </div>
  );
}

export default Counter;
