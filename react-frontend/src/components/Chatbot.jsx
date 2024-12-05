// Chatbot.jsx
import React, { useEffect } from "react";
import "./components/Chatbot.css"; // Importa el archivo de estilos chatbot.css

const Chatbot = () => {
  useEffect(() => {
    // Cargar el script de Dialogflow Messenger
    const script = document.createElement("script");
    script.src =
      "https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1";
    script.async = true;
    script.onload = () => {
      window.dfMessenger.render();
    };
    document.body.appendChild(script); // Agregar el script al body de la página

    // Limpiar el script cuando el componente se desmonte
    return () => {
      const existingScript = document.querySelector(
        'script[src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"]'
      );
      if (existingScript) {
        existingScript.remove();
      }
    };
  }, []);

  return (
    <div>
      {/* Renderiza el componente df-messenger en tu página */}
      <df-messenger
        intent="WELCOME"
        chat-title="chat-restaurant"
        agent-id="81d01c3f-2176-4ef6-a802-4e34f8ed6cf1" // Tu agent-id de Dialogflow
        language-code="es" // Cambia el idioma si es necesario
      ></df-messenger>
    </div>
  );
};

export default Chatbot;
