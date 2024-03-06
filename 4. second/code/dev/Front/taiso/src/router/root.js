import MainPage from "../pages/MainPage";

const { createBrowserRouter } = require("react-router-dom");


const root = createBrowserRouter([
  {
    path: '',
    element: <MainPage />
  }
])

export default root