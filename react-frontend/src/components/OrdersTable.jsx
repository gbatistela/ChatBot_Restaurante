import React, { useEffect, useState } from "react";

// Función para formatear el total en formato monetario
const formatCurrency = (amount) => {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
  }).format(amount);
};

// Component de la tabla de órdenes
function OrdersTable() {
  const [orders, setOrders] = useState([]);
  const [filter, setFilter] = useState("all");

  // Función para cargar las órdenes desde el endpoint
  useEffect(() => {
    fetch("http://127.0.0.1:8000/orders")
      .then((response) => response.json())
      .then((data) => {
        console.log(data); // Verifica lo que llega aquí
        setOrders(data.orders || data); // Ajusta según la estructura
      })
      .catch((error) => console.error("Error fetching orders:", error));
  }, []);

  // Filtrar las órdenes por estado
  const filteredOrders =
    filter === "all"
      ? orders
      : orders.filter((order) => order.order_status === filter);

  return (
    <div>
      {/* Filtro de estado */}
      <div>
        <label>Filter by status: </label>
        <select onChange={(e) => setFilter(e.target.value)} value={filter}>
          <option value="all">All</option>
          <option value="in progress">In Progress</option>
          <option value="in transit">In Transit</option>
          <option value="delivered">Delivered</option>
        </select>
      </div>

      {/* Tabla de órdenes */}
      <table
        border="1"
        cellPadding="10"
        style={{ width: "100%", marginTop: "20px", borderCollapse: "collapse" }}
      >
        <thead>
          <tr>
            <th>ID</th>
            <th>Items</th>
            <th>Total</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {filteredOrders.length === 0 ? (
            <tr>
              <td colSpan="4">No orders found</td>
            </tr>
          ) : (
            filteredOrders.map((order) => (
              <tr
                key={order.id}
                style={{
                  backgroundColor:
                    order.order_status === "delivered"
                      ? "#c8e6c9"
                      : order.order_status === "in progress"
                      ? "#fff3e0"
                      : "#ffccbc",
                }}
              >
                <td>{order.id}</td>
                <td>{order.items}</td>
                <td>{formatCurrency(order.total)}</td>
                <td
                  style={{
                    color:
                      order.order_status === "delivered"
                        ? "green"
                        : order.order_status === "in progress"
                        ? "orange"
                        : "blue",
                  }}
                >
                  {order.order_status}
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}

export default OrdersTable;
