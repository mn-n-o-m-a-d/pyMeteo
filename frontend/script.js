const weatherMap = {
    0: ["Sonnig", "☀️"],
    1: ["Klar", "🌤️"],
    2: ["Leicht bewölkt", "⛅"],
    3: ["Bedeckt", "☁️"],
    45: ["Nebel", "🌫️"],
    61: ["Regen", "🌧️"],
    71: ["Schneefall", "❄️"],
    77: ["Hagel", "🌨️"],
    80: ["Schauer", "🌦️"],
    85: ["Schneeschauer", "🌨️"],
    86: ["Starker Schneeschauer", "❄️"],
    95: ["Gewitter", "⛈️"]
};

async function loadWeather() {
    try {
        const response = await fetch('austria_weather.json?t=' + new Date().getTime());
        const cities = await response.json();
        const grid = document.getElementById('weather-grid');
        grid.innerHTML = ''; 

        cities.forEach(city => {
            
            console.log("Load city:", city.name);
            const card = document.createElement('div');
            card.className = 'weather-card';

            let forecastHtml = '';
            city.forecast.forEach((day, index) => {
                const date = new Date(day.date);
                const weekday = date.toLocaleDateString('de-AT', { weekday: 'short' });
                const [label, emoji] = weatherMap[day.code] || ["Unbekannt", "❓"];
                
                const isToday = index === 0 ? 'today-row' : '';

                forecastHtml += `
                    <div class="forecast-row ${isToday}">
                        <span class="day-name">${weekday}</span>
                        <span class="day-icon" title="${label}">${emoji}</span>
                        <span class="day-temp">${Math.round(day.temp_max)}° <small>/ ${Math.round(day.temp_min)}°</small></span>
                    </div>
                `;
            });

            card.innerHTML = `
                <h2>${city.name}</h2>
                <div class="forecast-list">
                    ${forecastHtml}
                </div>
                <div class="update-time">Update: ${city.timestamp.split(' ')[1]}</div>
            `;
            grid.appendChild(card);
        });
    } catch (e) {
        console.error("Datenfehler:", e);
    }
}

loadWeather();