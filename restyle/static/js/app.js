const API_KEY = "YOUR_API_KEY";
const PLACE_ID = "YOUR_PLACE_ID";

fetch(`https://maps.googleapis.com/maps/api/place/details/json?place_id=${PLACE_ID}&fields=reviews&key=${API_KEY}`)
.then(res => res.json())
.then(data => {
    const container = document.getElementById("google-reviews");

    data.result.reviews.forEach(r => {
        const div = document.createElement("div");
        div.classList.add("review-card");

        div.innerHTML = `
            <strong>${r.author_name}</strong>
            <div>⭐ ${r.rating}</div>
            <p>${r.text}</p>
        `;

        container.appendChild(div);
    });
});