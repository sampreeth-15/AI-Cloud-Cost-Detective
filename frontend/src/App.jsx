import { useEffect, useState } from "react";

function App() {
  const [resources, setResources] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/scan-resources")
      .then((res) => res.json())
      .then((data) => setResources(data.resources))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>🚀 AI Cloud Cost Detective</h1>

      <h2>Resources Found</h2>

      {resources.map((resource, index) => (
        <div
          key={index}
          style={{
            border: "1px solid gray",
            padding: "10px",
            marginBottom: "10px",
          }}
        >
          <h3>{resource.name}</h3>
          <p>Type: {resource.type}</p>
          <p>Status: {resource.status}</p>
          <p>Savings: {resource.estimated_savings}</p>
        </div>
      ))}
    </div>
  );
}

export default App;