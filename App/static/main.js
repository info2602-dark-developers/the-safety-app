
function showPosition(position)
{
    currentLatitude = position.coords.latitude;
    currentLongitude = position.coords.longitude;
    console.log("Latitude: " + currentLatitude);
    console.log("Longitude: " + currentLongitude);
}


async function getUserData(){
    const response = await fetch('/api/users');
    return response.json();
}

function loadTable(users){
    const table = document.querySelector('#result');
    for(let user of users){
        table.innerHTML += `<tr>
            <td>${user.id}</td>
            <td>${user.username}</td>
        </tr>`;
    }
}

async function main(){
    const users = await getUserData();
    loadTable(users);
}

main();

// Initialize the map
let map = new google.maps.Map(document.getElementById("map"), {
  center: { lat: 0, lng: 0 },
  zoom: 2,
});

// Add a marker at the center of the map
let marker = new google.maps.Marker({
  position: map.getCenter(),
  map: map,
  draggable: true,
});

// Update the latitude and longitude input fields when the marker is dragged
marker.addListener("dragend", function () {
  let latLng = marker.getPosition();
  document.getElementById("latitude").value = latLng.lat();
  document.getElementById("longitude").value = latLng.lng();
});

// Handle form submission
document.querySelector("form").addEventListener("submit", function (event) {
  event.preventDefault();

  // Extract the latitude and longitude values
  let latitude = document.getElementById("latitude").value;
  let longitude = document.getElementById("longitude").value;

  // Send the data to the server using a fetch request
  fetch("/location", {
    method: "POST",
    body: JSON.stringify({ latitude, longitude }),
    headers: {
      "Content-Type": "application/json",
    },
  }).then(function (response) {
    // Handle the response from the server
    console.log(response);
  });
});

