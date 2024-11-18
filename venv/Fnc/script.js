async function calculateDerivative() {
    const fValues = {
      'xi+2': parseFloat(document.getElementById('xi+2').value),
      'xi+1': parseFloat(document.getElementById('xi+1').value),
      'xi-1': parseFloat(document.getElementById('xi-1').value),
      'xi-2': parseFloat(document.getElementById('xi-2').value),
    };
    const h = parseFloat(document.getElementById('h').value);

    try {
      const response = await fetch('/calculate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ fValues, h })
      });
      const data = await response.json();
      document.getElementById('result').innerText = `Resultado: ${data.result}`;
    } catch (error) {
      document.getElementById('result').innerText = 'Error al calcular la derivada.';
    }
  }