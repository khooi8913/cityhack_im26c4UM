<template>
  <div class='row'>
    <div class='col-lg-12'>
    <div class='card card-map'>
      <div class='header'>
        <h4 class='title'>Google Maps</h4>
      </div>
      <div class='map'>
        <div id='map'></div>
      </div>
      <div>
        <h4>Top busiest roads now: <span class="text-danger" v-tooltip.bottom="'Traffic is congested because police are handling a robbery case there.'">Jalan University</span>, <span class="text-warning" v-tooltip.bottom="'No vehicles are passable due to the ongoing streets demonstration'">Persiaran Lagoon</span></h4>
        </div>
    </div>
    </div>
<!-- 
    <div class='col-lg-4'>
      <div class='card card-map'>
        <div class='header'>
          <h4 class='title'>Most Busy Road</h4>
        </div>
        <div>
          <ol>
            <li>Jalan University</li>
            <li>Jalan PJS 11/1</li>
            <li>Jalan PJS 9/14</li>
            <li>Persiaran Lagoon</li>
            <li>Jalan Lagoon Selatan</li>
          </ol>
        </div>
      </div>
    </div> -->
    
    </div>
</template>

<script>
export default {
  mounted () {
    var myLatlng = new window.google.maps.LatLng(3.069263, 101.604714)
    var mapOptions = {
      zoom: 15,
      center: myLatlng,
      scrollwheel: false, // we disable de scroll over the map, it is a really annoing when you scroll through page
      styles: [
        {
          featureType: 'water',
          stylers: [{ saturation: 43 }, { lightness: -11 }, { hue: '#0088ff' }]
        },
        {
          featureType: 'road',
          elementType: 'geometry.fill',
          stylers: [{ hue: '#ff0000' }, { saturation: -100 }, { lightness: 99 }]
        },
        {
          featureType: 'road',
          elementType: 'geometry.stroke',
          stylers: [{ color: '#808080' }, { lightness: 54 }]
        },
        {
          featureType: 'landscape.man_made',
          elementType: 'geometry.fill',
          stylers: [{ color: '#ece2d9' }]
        },
        {
          featureType: 'poi.park',
          elementType: 'geometry.fill',
          stylers: [{ color: '#ccdca1' }]
        },
        {
          featureType: 'road',
          elementType: 'labels.text.fill',
          stylers: [{ color: '#767676' }]
        },
        {
          featureType: 'road',
          elementType: 'labels.text.stroke',
          stylers: [{ color: '#ffffff' }]
        },
        { featureType: 'poi', stylers: [{ visibility: 'off' }] },
        {
          featureType: 'landscape.natural',
          elementType: 'geometry.fill',
          stylers: [{ visibility: 'on' }, { color: '#b8cb93' }]
        },
        { featureType: 'poi.park', stylers: [{ visibility: 'on' }] },
        {
          featureType: 'poi.sports_complex',
          stylers: [{ visibility: 'on' }]
        },
        { featureType: 'poi.medical', stylers: [{ visibility: 'on' }] },
        {
          featureType: 'poi.business',
          stylers: [{ visibility: 'simplified' }]
        }
      ]
    }
    var map = new window.google.maps.Map(
      document.getElementById('map'),
      mapOptions
    )

    var marker = new window.google.maps.TrafficLayer()

    // To add the marker to the map, call setMap();
    marker.setMap(map)
    // var mapOptions = {zoom: 13, center: {lat: 34.04924594193164, lng: -118.24104309082031}}
    // var map = new windows.google.maps.Map(document.getElementById('map'), mapOptions)
    // var trafficLayer = new google.maps.TrafficLayer()
    // trafficLayer.setMap(map)
  }
}
</script>
<style>
.tooltip {
  display: block !important;
  z-index: 10000;
}

.tooltip .tooltip-inner {
  background: black;
  color: white;
  border-radius: 16px;
  padding: 5px 10px 4px;
}

.tooltip .tooltip-arrow {
  width: 0;
  height: 0;
  border-style: solid;
  position: absolute;
  margin: 5px;
  border-color: black;
}

.tooltip[x-placement^="top"] {
  margin-bottom: 5px;
}

.tooltip[x-placement^="top"] .tooltip-arrow {
  border-width: 5px 5px 0 5px;
  border-left-color: transparent !important;
  border-right-color: transparent !important;
  border-bottom-color: transparent !important;
  bottom: -5px;
  left: calc(50% - 5px);
  margin-top: 0;
  margin-bottom: 0;
}

.tooltip[x-placement^="bottom"] {
  margin-top: 5px;
}

.tooltip[x-placement^="bottom"] .tooltip-arrow {
  border-width: 0 5px 5px 5px;
  border-left-color: transparent !important;
  border-right-color: transparent !important;
  border-top-color: transparent !important;
  top: -5px;
  left: calc(50% - 5px);
  margin-top: 0;
  margin-bottom: 0;
}

.tooltip[x-placement^="right"] {
  margin-left: 5px;
}

.tooltip[x-placement^="right"] .tooltip-arrow {
  border-width: 5px 5px 5px 0;
  border-left-color: transparent !important;
  border-top-color: transparent !important;
  border-bottom-color: transparent !important;
  left: -5px;
  top: calc(50% - 5px);
  margin-left: 0;
  margin-right: 0;
}

.tooltip[x-placement^="left"] {
  margin-right: 5px;
}

.tooltip[x-placement^="left"] .tooltip-arrow {
  border-width: 5px 0 5px 5px;
  border-top-color: transparent !important;
  border-right-color: transparent !important;
  border-bottom-color: transparent !important;
  right: -5px;
  top: calc(50% - 5px);
  margin-left: 0;
  margin-right: 0;
}

.tooltip[aria-hidden='true'] {
  visibility: hidden;
  opacity: 0;
  transition: opacity .15s, visibility .15s;
}

.tooltip[aria-hidden='false'] {
  visibility: visible;
  opacity: 1;
  transition: opacity .15s;
}
</style>
