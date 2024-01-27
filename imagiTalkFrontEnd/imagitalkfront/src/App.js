import "./App.css";
import React from "react";
import { Helmet } from "react-helmet";
import Chat from "./components/Chat";
import Home from "./components/Home"
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  return (
    <>
      <Helmet>
        <link rel="stylesheet" href="https://use.typekit.net/exu3mxs.css" />
      </Helmet>
      <div className="App">
        <Home />
      </div>
    </>
  );
}

export default App;
