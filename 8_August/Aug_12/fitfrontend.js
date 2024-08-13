let map;
let markers = [];

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 40.7128, lng: -74.0060 },
        zoom: 13
    });

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const pos = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude,
                };
                map.setCenter(pos);
                searchRestaurants(pos.lat, pos.lng);
            },
            () => {
                console.error('Error: The Geolocation service failed.');
            }
        );
    } else {
        console.error('Error: Your browser doesn\'t support geolocation.');
    }
}

async function searchRestaurants(lat, lng, term = '') {
    clearMarkers();
    const response = await fetch(`/api/restaurants?latitude=${lat}&longitude=${lng}&term=${term}`);
    const data = await response.json();
    displayRestaurants(data.businesses);
}

function displayRestaurants(restaurants) {
    const restaurantList = document.getElementById('restaurant-list');
    restaurantList.innerHTML = '';

    restaurants.forEach(restaurant => {
        const card = document.createElement('div');
        card.classList.add('restaurant-card');
        card.innerHTML = `
            <h3>${restaurant.name}</h3>
            <p>${restaurant.location.address1}</p>
            <p>Rating: ${restaurant.rating}</p>
        `;
        card.addEventListener('click', () => showRestaurantDetails(restaurant));
        restaurantList.appendChild(card);

        const marker = new google.maps.Marker({
            position: {
                lat: restaurant.coordinates.latitude,
                lng: restaurant.coordinates.longitude
            },
            map: map,
            title: restaurant.name
        });

        marker.addListener('click', () => showRestaurantDetails(restaurant));
        markers.push(marker);
    });
}

async function showRestaurantDetails(restaurant) {
    const modal = document.getElementById('restaurant-details');
    const restaurantName = document.getElementById('restaurant-name');
    const restaurantAddress = document.getElementById('restaurant-address');
    const restaurantPhone = document.getElementById('restaurant-phone');
    const restaurantRating = document.getElementById('restaurant-rating');
    const reviewsList = document.getElementById('reviews-list');

    restaurantName.textContent = restaurant.name;
    restaurantAddress.textContent = restaurant.location.address1;
    restaurantPhone.textContent = restaurant.phone;
    restaurantRating.textContent = `Rating: ${restaurant.rating}`;

    reviewsList.innerHTML = 'Loading reviews...';

    const response = await fetch(`/api/reviews/${restaurant.id}`);
    const data = await response.json();

    reviewsList.innerHTML = '';
    data.reviews.forEach(review => {
        const reviewElement = document.createElement('div');
        reviewElement.innerHTML = `
            <p><strong>${review.user.name}</strong> - ${review.rating} stars</p>
            <p>${review.text}</p>
        `;
        reviewsList.appendChild(reviewElement);
    });

    modal.style.display = 'block';
}

function clearMarkers() {
    markers.forEach(marker => marker.setMap(null));
    markers = [];
}

document.getElementById('search-btn').addEventListener('click', () => {
    const searchTerm = document.getElementById('search-input').value;
    const center = map.getCenter();
    searchRestaurants(center.lat(), center.lng(), searchTerm);
});

document.querySelector('.close').addEventListener('click', () => {
    document.getElementById('restaurant-details').style.display = 'none';
});

window.onclick = (event) => {
    const modal = document.getElementById('restaurant-details');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
};

initMap();