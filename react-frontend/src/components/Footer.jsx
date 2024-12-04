import React from "react";
import './footer.css'; // Asegúrate de tener un archivo de estilos

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-links">
          <a href="https://wa.me/1234567890" target="_blank" rel="noopener noreferrer">
            <i className="fab fa-whatsapp"></i> WhatsApp
          </a>
          <a href="https://www.instagram.com/tu_instagram" target="_blank" rel="noopener noreferrer">
            <i className="fab fa-instagram"></i> Instagram
          </a>
          <a href="mailto:contacto@restaurante.com">
            <i className="fas fa-envelope"></i> Correo
          </a>
          <a href="https://goo.gl/maps/tu-direccion" target="_blank" rel="noopener noreferrer">
            <i className="fas fa-map-marker-alt"></i> Dirección
          </a>
          <a href="#sucursal" target="_blank" rel="noopener noreferrer">
            <i className="fas fa-building"></i> Sucursal
          </a>
        </div>
        <p>© 2024 Restaurante - Todos los derechos reservados</p>
      </div>
    </footer>
  );
}

export default Footer;

