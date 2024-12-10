import React from "react";
import "./Menu.css"; // Archivo de estilos mejorado

function Menu() {
  const menus = [
    {
      id: 4,
      title: "Hamburguesas",
      image: "/menu2.jpg",
      description: "Exquisito y lleno de sabor.",
    },
    {
      id: 5,
      title: "Gaseosas",
      image: "/gaseosa.jpg",
      description: "Bebidas refrescantes para todos los gustos.",
    },
    {
      id: 6,
      title: "Pizzas",
      image: "/pizza1.jpg",
      description: "Perfectamente horneadas con los mejores ingredientes.",
    },
    {
      id: 7,
      title: "Tragos",
      image: "/tragos.jpg",
      description: "Cocteles y bebidas para cualquier ocasión.",
    },
    {
      id: 8,
      title: "Postres",
      image: "/torta.jpg",
      description: "El final dulce perfecto para tu comida.",
    },
    {
      id: 9,
      title: "Ensaladas",
      image: "/ensalada.jpeg",
      description: "Frescas, saludables y deliciosas.",
    },
    {
      id: 10,
      title: "Cafés",
      image: "/cafe.jpeg",
      description: "El aroma perfecto para acompañar cualquier momento.",
    },
    {
      id: 11,
      title: "Tacos",
      image: "/tacos.jpeg",
      description: "Sabor auténtico y lleno de tradición.",
    },
    {
      id: 12,
      title: "Sopas",
      image: "/sopa.jpeg",
      description: "Calientes y reconfortantes, como en casa.",
    },
    {
      id: 13,
      title: "Snacks",
      image: "/snacks.jpeg",
      description: "Ideales para compartir en cualquier momento.",
    },
  ];

  // Funciones para el desplazamiento horizontal
  const scrollLeft = () => {
    document
      .querySelector(".menu-carousel")
      .scrollBy({ left: -300, behavior: "smooth" });
  };

  const scrollRight = () => {
    document
      .querySelector(".menu-carousel")
      .scrollBy({ left: 300, behavior: "smooth" });
  };

  return (
    <section className="menu-section">
      <h2>Menú</h2>
      <div className="menu-controls">
        <button onClick={scrollLeft} className="scroll-button left">
          ◀
        </button>
        <div className="menu-carousel">
          {menus.map((menu) => (
            <div key={menu.id} className="menu-card">
              <img src={menu.image} alt={menu.title} />
              <h3>{menu.title}</h3>
              <p>{menu.description}</p>
            </div>
          ))}
        </div>
        <button onClick={scrollRight} className="scroll-button right">
          ▶
        </button>
        
      </div>
      <p className="menu-footer">¡Explora nuestra deliciosa selección de platillos! 🌟</p>
    </section>
  );
}

export default Menu;

