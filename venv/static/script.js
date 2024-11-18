async function calculateDerivative() {
  const h = parseFloat(document.getElementById('h').value);
  const formula = document.getElementById('formula').value;

  // Validación básica
  if (isNaN(h) || !formula) {
    document.getElementById('error').innerText = "Por favor, ingresa un valor válido para h y la fórmula.";
    document.getElementById('result').innerText = "";
    return;
  }

  try {
    const response = await fetch('/calculate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ h, formula })
    });

    const data = await response.json();

    if (response.ok) {
      document.getElementById('result').innerHTML = `<p><strong>Resultado:</strong> ${data.result}</p>`;
      document.getElementById('error').innerText = "";
    } else {
      document.getElementById('error').innerText = data.error || "Ocurrió un error.";
      document.getElementById('result').innerText = "";
    }
  } catch (error) {
    document.getElementById('error').innerText = "Error al conectarse con el servidor.";
    document.getElementById('result').innerText = "";
  }
}