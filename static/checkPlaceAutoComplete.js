// Initialize the platform object:

var service;
var infowindow;

function initMap() {
  var Kampala = new google.maps.LatLng(0.348047, 32.578523);
  var fenway = { lat: 42.345573, lng: -71.098326 };
  var sv = new google.maps.StreetViewService();

  panorama = new google.maps.StreetViewPanorama(
    document.getElementById("pano")
  );

  infowindow = new google.maps.InfoWindow();

  map = new google.maps.Map(document.getElementById("map"), {
    center: Kampala,
    zoom: 20,
    streetViewControl: false,
  });

  //add traffic api
  var trafficLayer = new google.maps.TrafficLayer();
  trafficLayer.setMap(map);

  //street view
  sv.getPanorama({ location: fenway, radius: 50 }, processSVData);

  map.addListener("click", function (event) {
    sv.getPanorama({ location: event.latLng, radius: 50 }, processSVData);
  });

  // alert(JSON.stringify(trafficLayer));

  //get data from html
  var card = document.getElementById("pac-card");
  var input = document.getElementById("pac-input");
  var types = document.getElementById("type-selector");
  var strictBounds = document.getElementById("strict-bounds-selector");

  map.controls[google.maps.ControlPosition.TOP_RIGHT].push(card);

  var autocomplete = new google.maps.places.Autocomplete(input);

  // Bind the map's bounds (viewport) property to the autocomplete object,
  // so that the autocomplete requests use the current map bounds for the
  // bounds option in the request.
  autocomplete.bindTo("bounds", map);

  // Set the data fields to return when the user selects a place.
  autocomplete.setFields(["address_components", "geometry", "icon", "name"]);

  var infowindow = new google.maps.InfoWindow();
  var infowindowContent = document.getElementById("infowindow-content");
  infowindow.setContent(infowindowContent);
  var marker = new google.maps.Marker({
    map: map,
    anchorPoint: new google.maps.Point(0, -29),
    zoom: 40,
  });

  autocomplete.addListener("place_changed", function () {
    infowindow.close();
    marker.setVisible(false);
    var place = autocomplete.getPlace();
    var long_name =place.address_components[0].long_name
    localStorage.setItem("currentplace", long_name);
    if (!place.geometry) {
      // User entered the name of a Place that was not suggested and
      // pressed the Enter key, or the Place Details request failed.
      window.alert("No details available for input: '" + place.name + "'");
      return;
    }

    // If the place has a geometry, then present it on a map.
    if (place.geometry.viewport) {
      map.fitBounds(place.geometry.viewport);
    } else {
      map.setCenter(place.geometry.location);
      map.setZoom(17); // Why 17? Because it looks good.
    }
    marker.setPosition(place.geometry.location);
    marker.setVisible(true);

    var address = "";
    if (place.address_components) {
      address = [
        (place.address_components[0] &&
          place.address_components[0].short_name) ||
          "",
        (place.address_components[1] &&
          place.address_components[1].short_name) ||
          "",
        (place.address_components[2] &&
          place.address_components[2].short_name) ||
          "",
      ].join(" ");
    }

    infowindowContent.children["place-icon"].src = place.icon;
    infowindowContent.children["place-name"].textContent = place.name;
    infowindowContent.children["place-address"].textContent = address;
    infowindow.open(map, marker);
  });

  // Sets a listener on a radio button to change the filter type on Places
  // Autocomplete.
  function setupClickListener(id, types) {
    var radioButton = document.getElementById(id);
    radioButton.addEventListener("click", function () {
      autocomplete.setTypes(types);
    });
  }

  setupClickListener("changetype-all", []);
  setupClickListener("changetype-address", ["address"]);
  setupClickListener("changetype-establishment", ["establishment"]);
  setupClickListener("changetype-geocode", ["geocode"]);

  document
    .getElementById("use-strict-bounds")
    .addEventListener("click", function () {
      console.log("Checkbox clicked! New state=" + this.checked);
      autocomplete.setOptions({ strictBounds: this.checked });
    });
}

function processSVData(data, status) {
  if (status === "OK") {
    var marker = new google.maps.Marker({
      position: data.location.latLng,
      map: map,
      title: data.location.description,
    });

    panorama.setPano(data.location.pano);
    panorama.setPov({
      heading: 270,
      pitch: 0,
    });
    panorama.setVisible(true);

    marker.addListener("click", function () {
      var markerPanoID = data.location.pano;
      // Set the Pano to use the passed panoID.
      panorama.setPano(markerPanoID);
      panorama.setPov({
        heading: 270,
        pitch: 0,
      });
      panorama.setVisible(true);
    });
  } else {
    console.error("Street View data not found for this location.");
  }
}

// $("#pano").ready(function () {
//   alert("sdsds");
// });

$("#btn").click(function () {
  html2canvas($("#pano").get(0), {
    useCORS: true,
    taintTest: false,
    allowTaint: false,
    logging: true,
    width: 1920,
    height: 1080,
  }).then(function (canvas) {
    $("#box").html("");
    $("#box").append(canvas);

    // canvas.toBlob(function (blob) {
    //   saveAs(blob, "Dashboard.png");
    // });
  });
});

$("#loc").click(function () {
  alert("erere");
});
