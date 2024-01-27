import "./App.css";
import React from "react";
import { Helmet } from "react-helmet";
import Chat from "./components/Chat";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  return (
    <>
      <Helmet>
        <link rel="stylesheet" href="https://use.typekit.net/exu3mxs.css" />
      </Helmet>
      <div className="App">
        <Chat />
      </div>
    </>
  );
}

export default App;
