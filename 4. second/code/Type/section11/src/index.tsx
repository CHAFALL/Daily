import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";


// non - null 단언 : !
// 좀 더 직관적으로 해결하기 위해 : as HTMLElement

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
