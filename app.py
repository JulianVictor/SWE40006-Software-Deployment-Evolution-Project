from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>🐱 Cat Facts App</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      margin: 0;
      padding: 0;
      background: #fff7f0;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
    }
    .app-container {
      width: 90%;
      max-width: 600px;
      background: #ffffff;
      border-radius: 16px;
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
      padding: 30px;
      text-align: center;
    }
    .fact-box {
      background-color: #fef6e4;
      padding: 20px;
      margin: 20px 0;
      border-left: 5px solid #f98fb0;
      font-size: 18px;
      animation: fadeIn 0.5s;
    }
    .buttons {
      margin-bottom: 20px;
    }
    button {
      padding: 10px 15px;
      margin: 5px;
      font-size: 16px;
      background-color: #f98fb0;
      color: white;
      border: none;
      border-radius: 8px;
      cursor: pointer;
    }
    button:hover {
      background-color: #e3729c;
    }
    ul {
      text-align: left;
      padding-left: 20px;
      max-height: 150px;
      overflow-y: auto;
    }
    .clear-btn {
      background-color: #ff9999;
    }
    .clear-btn:hover {
      background-color: #e97777;
    }
    @keyframes fadeIn {
      from {opacity: 0;}
      to {opacity: 1;}
    }
  </style>
</head>
<body>
  <div class="app-container">
    <h1>🐾 Cat Facts</h1>
    <div class="fact-box" id="fact-box">Loading cat fact...</div>
    <div class="buttons">
      <button onclick="getCatFact()">Get Another Fact</button>
      <button onclick="saveFavorite()">❤️ Save to Favorites</button>
    </div>
    
    <h2>Saved Favorites</h2>
    <ul id="favorites-list"></ul>
    <button class="clear-btn" onclick="clearFavorites()">🗑️ Clear All</button>
  </div>

  <script>
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
  </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
