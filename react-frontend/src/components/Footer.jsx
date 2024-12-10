// Footer.jsx
import React from "react";
import "./Footer.css"; // Asegúrate de tener un archivo de estilos

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-links">
          <a
            href="https://wa.me/1234567890"
            target="_blank"
            rel="noopener noreferrer"
          >
            <img
              src="/logowhatsapp.png"
              alt="WhatsApp"
              className="footer-icon"
            />
          </a>
          <a
            href="https://www.instagram.com/tu_instagram"
            target="_blank"
            rel="noopener noreferrer"
          >
            <img
              src="/instagram.png"
              alt="Instagram"
              className="footer-icon-ig"
            />
          </a>
          <a href="restaurant_bart@gmail.com">
            <img src="/image.jpg" alt="Correo" className="footer-icon" />
          </a>
          <a
            href="https://goo.gl/maps/tu-direccion"
            target="_blank"
            rel="noopener noreferrer"
          > 
            <img src="/mapa.jpg" alt="Dirección" className="footer-icon-maps" />
            
          </a>
        </div>

        <p>© 2024 Restaurante - Todos los derechos reservados</p>
      </div>
    </footer>
  );
}

export default Footer;
