$(document).ready(function(){
  $('.portfolio-items').slick({
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 3,
    dots: true,
    centerMode: true,
    variableWidth: true,
    draggable: true,
    focusOnSelect: true
      });
});

function myMap() {
    var mapProp = {center:new google.maps.LatLng(55.8740524,-4.2921628),zoom:11};
    var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
    var geocoder = new google.maps.Geocoder();
    var testLocation = "{{ service_ad.location }}";
    var test = "glasgow";
    geocodeAddress(geocoder, map);
}

function geocodeAddress(geocoder, resultsMap) {
    geocoder.geocode({'address' : "tenerife"}, function(results, status) {
        if (status === 'OK') {
            resultsMap.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
            map: resultsMap,
            position: results[0].geometry.location
        });
        } else {
            alert('geocode not found for: ' + status);
        }
    });
}
