import React from "react";
import "./Menu.css"; // Archivo de estilos separado

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
      description: "Exquisito y lleno de sabor.",
    },
    {
      id: 6,
      title: "Pizzas",
      image: "/pizza1.jpg",
      description: "Exquisito y lleno de sabor.",
    },
    {
      id: 7,
      title: "Tragos",
      image: "/tragos.jpg",
      description: "Exquisito y lleno de sabor.",
    },
    {
      id: 8,
      title: "Postres",
      image: "/torta.jpg",
      description: "Exquisito y lleno de sabor.",
    },
  ];

  // Funciones para el desplazamiento horizontal
  function scrollLeft() {
    document
      .querySelector(".menu-carousel")
      .scrollBy({ left: -300, behavior: "smooth" });
  }

  function scrollRight() {
    document
      .querySelector(".menu-carousel")
      .scrollBy({ left: 300, behavior: "smooth" });
  }

  return (
    <section className="menu-section">
      <h2>Menú</h2>
      <div className="menu-controls">
        <button onClick={scrollLeft} className="scroll-button">
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
        <button onClick={scrollRight} className="scroll-button">
          ▶
        </button>
      </div>
    </section>
  );
}

export default Menu;
