import { Route, Routes } from "react-router"
import DefaultLayout from "./components/layouts/DefaultLayout"
import MainPage from "./pages/MainPage"
import LoginPage from "./pages/LoginPage"
import RegistrationPage from "./pages/RegistrationPage"

function App() {
  return (
    <Routes>
      <Route path="/" element={<DefaultLayout />} >
        <Route index element={<MainPage />}/>
        <Route path="login" element={<LoginPage />}/>
        <Route path="registration" element={<RegistrationPage />}/>
      </Route>
    </Routes>
  )
}

export default App