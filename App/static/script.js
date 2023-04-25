var latitude;
var longitude;

function trackLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      latitude = position.coords.latitude;
      longitude = position.coords.longitude;
    });
  } else {
    console.log("Geolocation is not supported by this browser.");
  }
}

trackLocation()