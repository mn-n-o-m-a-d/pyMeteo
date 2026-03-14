async function loadAustriaWeather() {
    try {
        const response = await fetch('austria_weather.json');
        const cities = await response.json();
        const grid = document.getElementById('weather-grid');
        grid.innerHTML = '';

        const weatherMap = {
            0: "☀️", 1: "🌤️", 2: "⛅", 3: "☁️", 45: "🌫️", 61: "🌧️", 95: "⛈️"
        };

        cities.forEach(city => {
            const emoji = weatherMap[city.code] || "❓";

            const card = document.createElement('div');
            card.className = 'weater-card';
            card.innerHTML = `
                <h3>${city.name}</h3>
                <div style="font-size: 3rem;">${emoji}</div>
                <h2>${Math.round(city.temp)}°C</h2>
            `;
            grid.appendChild(card);
            console.log("Timestamp:", city.timestamp)
        });
    } catch (e) {
        console.error("Loading error:", e);
    }
}

loadAustriaWeather();
