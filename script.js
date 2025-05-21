const factBox = document.getElementById("fact-box");
const favoritesList = document.getElementById("favorites-list");
let currentFact = "";

async function getCatFact() {
  try {
    const response = await fetch("https://catfact.ninja/fact");
    const data = await response.json();
    currentFact = data.fact;
    factBox.textContent = currentFact;
  } catch (error) {
    factBox.textContent = "Failed to fetch cat fact 😿";
  }
}

function saveFavorite() {
  if (!currentFact) return;

  const favorites = JSON.parse(localStorage.getItem("catFavorites") || "[]");
  if (!favorites.includes(currentFact)) {
    favorites.push(currentFact);
    localStorage.setItem("catFavorites", JSON.stringify(favorites));
    renderFavorites();
  }
}

function clearFavorites() {
  localStorage.removeItem("catFavorites");
  renderFavorites();
}

function renderFavorites() {
  const favorites = JSON.parse(localStorage.getItem("catFavorites") || "[]");
  favoritesList.innerHTML = "";

  favorites.forEach(fact => {
    const li = document.createElement("li");
    li.textContent = fact;
    favoritesList.appendChild(li);
  });
}

window.onload = () => {
  getCatFact();
  renderFavorites();
};
