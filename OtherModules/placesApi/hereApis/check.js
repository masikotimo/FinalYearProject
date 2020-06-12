// Initialize the platform object:
var resultContainer = document.getElementById("box");

var platform = new H.service.Platform({
  apikey: "wLZOXH5nSFQQ_2spa8EVwYsay2cyQGAuQCeo01EQa7Q",
});

// Obtain the default map types from the platform object
var maptypes = platform.createDefaultLayers();

// Instantiate (and display) a map object:
var map = new H.Map(
  document.getElementById("mapContainer"),
  maptypes.vector.normal.map,
  {
    zoom: 10,
    center: { lat: 0.347596, lng: 32.58252 },
  }
);

$("#btn").click(function () {
  html2canvas($("#mapContainer").get(0)).then(function (canvas) {
    $("#box").html("");
    $("#box").append(canvas);
  });
});
