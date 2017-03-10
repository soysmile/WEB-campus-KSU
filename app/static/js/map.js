var map;

function initMap() {
    var centerMap = {lat:46.641136, lng: 32.627992};
  map = new google.maps.Map(document.getElementById('map1'), {
    center: centerMap,
    zoom: 10
  });
    
}
function campus_two() {
    var centerMap = {lat:46.636141, lng: 32.629317};
    var myLatLng2= {lat:  46.636141, lng: 32.629317}; 
  map = new google.maps.Map(document.getElementById('map1'), {
    center: centerMap,
    zoom: 17
  });
    var marker = new google.maps.Marker({
    position: myLatLng2,
    map: map,
    title: 'Общежитие №2'
  });
    
}

function campus_three() {
    var centerMap = {lat:46.645016, lng: 32.630567};
    var myLatLng3 = {lat: 46.645016, lng: 32.630567}; 
  map = new google.maps.Map(document.getElementById('map1'), {
    center: centerMap,
    zoom: 17
  });
    var marker = new google.maps.Marker({
    position: myLatLng3,
    map: map,
    title: 'Общежитие №3'
  });
}

function campus_four() {
    var centerMap = {lat:46.644669, lng: 32.631089};
    var myLatLng4 = {lat:  46.644669, lng: 32.631089}; 
  map = new google.maps.Map(document.getElementById('map1'), {
    center: centerMap,
    zoom: 17
  });
    var marker = new google.maps.Marker({
    position: myLatLng4,
    map: map,
    title: 'Общежитие №4'
  });
}

function KSU() {
    var centerMap = {lat:46.646445, lng: 32.629634};
    var myLatLng4 = {lat:  46.646445, lng: 32.629634}; 
  map = new google.maps.Map(document.getElementById('map1'), {
    center: centerMap,
    zoom: 17
  });
    var marker = new google.maps.Marker({
    position: myLatLng4,
    map: map,
    title: 'Херсонский Государственный Университет'
  });
}