import Counter from "./components/Counter";
import CounterHover from "./components/CounterHover";
import ErrorBoundary from "./utils/ErrorBoundry";

const App = () => {
  return (
    <div>
      <ErrorBoundary>
        <Counter />
      </ErrorBoundary>
      <ErrorBoundary>
        <CounterHover />
      </ErrorBoundary>
    </div>
  );
};

export default App;
