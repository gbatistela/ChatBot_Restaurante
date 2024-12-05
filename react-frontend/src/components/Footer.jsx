// Footer.jsx
import React from "react";
import "./components/Footer.css"; // Asegúrate de tener un archivo de estilos

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
              src="/instagram.avif"
              alt="Instagram"
              className="footer-icon"
            />
          </a>
          <a href="mailto:contacto@restaurante.com">
            <img src="/image.jpg" alt="Correo" className="footer-icon" />
          </a>
          <a
            href="https://goo.gl/maps/tu-direccion"
            target="_blank"
            rel="noopener noreferrer"
          >
            <img
              src="/assets/images/location-logo.png"
              alt="Dirección"
              className="footer-icon"
            />
            Dirección
          </a>
          <a href="#sucursal" target="_blank" rel="noopener noreferrer">
            <img
              src="/assets/images/building-logo.png"
              alt="Sucursal"
              className="footer-icon"
            />
            Sucursal
          </a>
        </div>

        <p>© 2024 Restaurante - Todos los derechos reservados</p>
      </div>
    </footer>
  );
}

export default Footer;
