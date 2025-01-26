import L from 'leaflet';

export function initializeMap(mapElementId) {
const map = L.map(mapElementId).setView([52.0705, 4.3007], 13);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);

  return map;
}

export function updateMap(map, properties) {
  map.eachLayer(function (layer) {
    if (layer instanceof L.Marker) {
      map.removeLayer(layer);
    }
  });

  properties.forEach(property => {
    if (property.latitude && property.longitude) {
      L.marker([property.latitude, property.longitude])
        .addTo(map)
        .bindPopup(`
          <b>Property ID:</b> ${property.id}<br>
          <b>Address:</b> ${property.full_address}<br>
          <b>Value:</b> ${property.estimated_market_value}<br>
          <b>Size:</b> ${property.building_square_feet} sq. ft.
        `);
    }
  });

  const group = new L.featureGroup(properties.map(property => L.marker([property.latitude, property.longitude])));
  map.fitBounds(group.getBounds());
}
