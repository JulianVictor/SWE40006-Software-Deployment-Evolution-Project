const factElement = document.getElementById("fact");

async function getCatFact() {
  try {
    const response = await fetch("https://catfact.ninja/fact");
    const data = await response.json();
    factElement.textContent = data.fact;
  } catch (error) {
    factElement.textContent = "Could not load cat fact.";
  }
}

getCatFact();
