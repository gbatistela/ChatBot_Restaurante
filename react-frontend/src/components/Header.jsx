import React, { useState } from "react";
import { Link } from "react-router-dom"; // Importa Link
import "./Header.css";

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <header className="header">
      <div className="logo">
        <img src="logorestaurante.jpg" alt="Logo" />
      </div>
      <nav className={`nav ${isMenuOpen ? "open" : ""}`}>
        <ul>
          <li>
            <Link to="/">Home</Link> {/* Cambia href por Link */}
          </li>
          <li>
            <Link to="/">Menu</Link> {/* Cambia href por Link */}
          </li>
          <li>
            <Link to="/footer">Contacto</Link> {/* Cambia href por Link */}
          </li>
          <li>
            <Link to="/orders">Órdenes</Link>{" "}
            {/* Nueva página para las órdenes */}
          </li>
        </ul>
      </nav>
      <div className="menu-toggle" onClick={toggleMenu}>
        <span className="bar"></span>
        <span className="bar"></span>
        <span className="bar"></span>
      </div>
    </header>
  );
};

export default Header;
