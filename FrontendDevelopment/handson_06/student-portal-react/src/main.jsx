import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import { Provider } from "react-redux";

import App from "./App";
import "./index.css";

import { EnrollmentProvider } from "./context/EnrollmentContext";
import { store } from "./redux/store";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <Provider store={store}>
      <EnrollmentProvider>
        <BrowserRouter>
          <App />
        </BrowserRouter>
      </EnrollmentProvider>
    </Provider>
  </React.StrictMode>
);