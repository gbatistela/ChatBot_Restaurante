// App.jsx
import React from "react";
import Header from "./components/Header";
import Menu from "./components/Menu";
import Footer from "./components/Footer";
import Chatbot from "./components/Chatbot"; // Importa el componente Chatbot
import "./styles.css";

function App() {
  return (
    <div className="App">
      <Header />
      <main>
        <Menu />
        <Chatbot /> {/* Agrega el componente Chatbot aquí */}
      </main>
      <Footer />
    </div>
  );
}

export default App;
