import { Component } from "react";

class ErrorBoundry extends Component {
  state = {
    hasError: false,
  };

  static getDerivedStateFromError() {
    return { hasError: true };
  }

  componentDidCatch(error) {
    console.error("error", error);
  }

  render() {
    if (this.state.hasError) {
      return <p>something went wrong</p>;
    }
    return this.props.children;
  }
}

export default ErrorBoundry;
