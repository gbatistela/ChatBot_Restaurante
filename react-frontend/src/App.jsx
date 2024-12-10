import React from "react";
import Header from "./components/Header";
import Menu from "./components/Menu";
import Footer from "./components/Footer";
import Chatbot from "./components/Chatbot";
import OrdersTable from "./components/OrdersTable"; // Importa el componente OrdersTable
import "./styles.css";

function App() {
  return (
    <div className="App">
      <Header />
      <main>
        <Menu />
        <Chatbot />
        <OrdersTable /> {/* Agrega el componente OrdersTable aquí */}
      </main>
      <Footer />
    </div>
  );
}

export default App;
