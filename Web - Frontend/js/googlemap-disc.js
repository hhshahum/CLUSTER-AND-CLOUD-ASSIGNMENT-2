	var mapStyle = [{
        'stylers': [{'visibility': 'off'}]
      },
	  // {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
	  // {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
	  // {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
	  // {
	  //   'elementType': 'geometry',
	  //   'stylers': [{'visibility': 'on'}, {'color': '#242f3e'}]
	  // },
	  {
	    'elementType': 'labels.text.stroke',
	    'stylers': [{'visibility': 'on'}, {'color': '#242f3e'}]
	  },
	  {
	    'elementType': 'labels.text.fill',
	    'stylers': [{'visibility': 'on'}, {'color': '#e3ebf4'}]
	  },
	  {
        'featureType': 'landscape',
        'elementType': 'geometry',
        'stylers': [{'visibility': 'on'}, {'color': '#242f3e'}]
      }, {
        'featureType': 'water',
        'elementType': 'geometry',
        'stylers': [{'visibility': 'on'}, {'color': '#17263c'}]
      }];
      var map,heatmap;
	  var AUSTRALIA_BOUNDS = {
	          north: -9.7491,
	          south: -44.1874,
	          west: 104.0238,
	          east: 166.3163,
	        };
	var drawLayerSite = null;
	var	propertyArray = []
	var areaName = []
	var barName = []
	var barValue = []
      function initMap() {
        // load the map
        map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -25.344, lng: 131.036},
          zoom: 4,
          styles: mapStyle,
		  restriction: {
		              latLngBounds: AUSTRALIA_BOUNDS,
		              strictBounds: false,
		            },
        });
		heatmap = new google.maps.visualization.HeatmapLayer({
		  data: getPoints(),
		  map: map
		});
		
      }

      /** Loads the state boundary polygons from a GeoJSON source. */
      function loadMapShapes(dataPath) {
		// map.data.setData(null)
        // load US state outline polygons from a GeoJson file
        // map.data.loadGeoJson('https://swift.rc.nectar.org.au/v1/AUTH_5c31854668b64f0fbdace4807fbc8857/json_data/south_australia/states.json', { idPropertyName: 'STATE' });
		var data = null
		data = dataPath
		if (drawLayerSite && drawLayerSite.setMap){
			 drawLayerSite.setMap(null);
		}
	    drawLayerSite = new google.maps.Data({map: map
		 });
		
		var myLatlng = {lat: -25.363, lng: 131.044};
		var featureProperties = ""
		var infoWindow = new google.maps.InfoWindow(
		            {content: 'Click the map to get more information', position: myLatlng});
		infoWindow.open(map);
		
		drawLayerSite.addListener('mouseover', function(mapsMouseEvent) {
		          // Close the current InfoWindow.
		          infoWindow.close();
				  featureProperties = ""
		          // Create a new InfoWindow
		          infoWindow = new google.maps.InfoWindow({position: mapsMouseEvent.latLng,maxWidth: 400});
				  mapsMouseEvent.feature.forEachProperty(function(value,property) {
					  if(value==null){
					  	value = 0
					  }
					    if(property=='est_ppl_18yrs_plus_dgre_othr_cltr_2014_num'||property=='est_ppl_18yrs_plus_past_12_mth_exp_dctn_2014_num'
						|| property =='est_ppl_18yrs_plus_feel_safe_loc_area_2014_num' || property =='lga_name'
						){
							featureProperties = "\n" + featureProperties + property + ":" + value + "\n";
						}
				          
				  });
		          infoWindow.setContent(featureProperties);
		          infoWindow.open(map);
		        });
				
		drawLayerSite.addListener('click', function(mapsMouseEvent) {
				 propertyArray = []

		          infoWindow.close();
				  mapsMouseEvent.feature.forEachProperty(function(value,property) {
						if(value==null){
							value = 0
						}
						if(property=='est_ppl_18yrs_plus_dgre_othr_cltr_2014_num'||property=='est_ppl_18yrs_plus_past_12_mth_exp_dctn_2014_num'
						|| property =='est_ppl_18yrs_plus_feel_safe_loc_area_2014_num' || property =='lga_name'
						){
							propertyArray.push({'value':value,'name':property})
						}
						
				  });

				  for(i=0;i<propertyArray.length;i++){
					    if(propertyArray[i]['name'] == 'lga_name'){
							areaName = propertyArray[i]
						}
				  		barName.push(propertyArray[i]['name'])
						barValue.push(propertyArray[i]['value'])
				  }
				  
				  
				  myChart.clear();
				  changeChartFlag = false;
				  myChart.setOption({
						title: {
							text: 'Discrimination Data',
							subtext: 'Area: '+areaName['value'],
							left: 'center'
						},
						tooltip: {
							trigger: 'item',
							formatter: '{a} <br/>{b} : {c} ({d}%)'
						},
						// legend: {
						// 	orient: 'vertical',
						// 	left: 'right',
						// 	data: propertyName
						// },
						series: [
							{
								name: 'type',
								type: 'pie',
								radius: '65%',
								center: ['50%', '62%'],
								data: propertyArray,
								emphasis: {
									itemStyle: {
										shadowBlur: 300,
										shadowOffsetX: 0,
										shadowColor: 'rgba(0, 0, 0, 0.5)'
									}
								}
							}
						]
					});
				  show()
		        });
		// set up the style rules and events for google.maps.Data
		drawLayerSite.setStyle({
		  fillColor: 'white',
		  fillOpacity: 0.3,
		  strokeWeight: 2,
		  strokeColor: 'orange',
		  strokeOpacity: 0.4
		});
		
		drawLayerSite.addListener('mouseover', function(event) {
				drawLayerSite.revertStyle();
				drawLayerSite.overrideStyle(event.feature, {strokeWeight: 6});
		        });
		drawLayerSite.addListener('mouseout', function(event) {
		  drawLayerSite.revertStyle();
		});
		
		drawLayerSite.loadGeoJson(data);
		
		// wait for the request to complete by listening for the first feature to be
        // added
        // google.maps.event.addListenerOnce(map.data, 'addfeature', function() {
        //   google.maps.event.trigger(document.getElementById('census-variable'),
        //       'change');
        // });
      }

      /**
       * Loads the census data from a simulated API call to the US Census API.
       *
       * @param {string} variable
       */
      function loadCensusData(variable) {
        // load the requested variable from the census API (using local copies)
        var xhr = new XMLHttpRequest();
        xhr.open('GET', variable + '.json');
        xhr.onload = function() {
          var censusData = JSON.parse(xhr.responseText);
          censusData.shift(); // the first row contains column names
          censusData.forEach(function(row) {
            var censusVariable = parseFloat(row[0]);
            var stateId = row[1];

            // keep track of min and max values
            if (censusVariable < censusMin) {
              censusMin = censusVariable;
            }
            if (censusVariable > censusMax) {
              censusMax = censusVariable;
            }

            // update the existing row with the new data
            map.data
              .getFeatureById(stateId)
              .setProperty('census_variable', censusVariable);
          });

          // update and display the legend
          document.getElementById('census-min').textContent =
              censusMin.toLocaleString();
          document.getElementById('census-max').textContent =
              censusMax.toLocaleString();
        };
        xhr.send();
      }

      /** Removes census data from each shape on the map and resets the UI. */
      function clearCensusData() {
        censusMin = Number.MAX_VALUE;
        censusMax = -Number.MAX_VALUE;
        map.data.forEach(function(row) {
          row.setProperty('census_variable', undefined);
        });
        document.getElementById('data-box').style.display = 'none';
        document.getElementById('data-caret').style.display = 'none';
      }

      /**
       * Applies a gradient style based on the 'census_variable' column.
       * This is the callback passed to data.setStyle() and is called for each row in
       * the data set.  Check out the docs for Data.StylingFunction.
       *
       * @param {google.maps.Data.Feature} feature
       */
      function styleFeature(feature) {
        var low = [5, 69, 54];  // color of smallest datum
        var high = [151, 83, 34];   // color of largest datum

        // delta represents where the value sits between the min and max
        // var delta = (feature.getProperty('census_variable') - censusMin) /
        //     (censusMax - censusMin);

        var color = [];
        for (var i = 0; i < 3; i++) {
          // calculate an integer color based on the delta
          color[i] = (high[i] - low[i]) * delta + low[i];
        }

        // determine whether to show this shape or not
		
        // var showRow = true;
        // if (feature.getProperty('census_variable') == null ||
        //     isNaN(feature.getProperty('census_variable'))) {
        //   showRow = false;
        // }

        // var outlineWeight = 0.5, zIndex = 1;
        // if (feature.getProperty('state') === 'hover') {
        //   outlineWeight = zIndex = 2;
        // }

        return {
          strokeWeight: outlineWeight,
          strokeColor: '#fff',
          zIndex: zIndex,
          fillColor: 'hsl(' + color[0] + ',' + color[1] + '%,' + color[2] + '%)',
          fillOpacity: 0.75,
          visible: showRow
        };
      }

      /**
       * Responds to the mouse-in event on a map shape (state).
       *
       * @param {?google.maps.MouseEvent} e
       */
      function mouseInToRegion(e) {
        // set the hover state so the setStyle function can change the border
        e.feature.setProperty('state', 'hover');

        var percent = (e.feature.getProperty('census_variable') - censusMin) /
            (censusMax - censusMin) * 100;

        // update the label
        document.getElementById('data-label').textContent =
            e.feature.getProperty('NAME');
        document.getElementById('data-value').textContent =
            e.feature.getProperty('census_variable').toLocaleString();
        document.getElementById('data-box').style.display = 'block';
        document.getElementById('data-caret').style.display = 'block';
        document.getElementById('data-caret').style.paddingLeft = percent + '%';
      }

      /**
       * Responds to the mouse-out event on a map shape (state).
       *
       * @param {?google.maps.MouseEvent} e
       */
      function mouseOutOfRegion(e) {
        // reset the hover state, returning the border to normal
        e.feature.setProperty('state', 'normal');
      }
	  // heatmap-js
	  function toggleHeatmap() {
	    heatmap.setMap(heatmap.getMap() ? null : map);
	  }
	  
	  function getPoints() {
	  		let requestURL = 'https://storage.googleapis.com/aurin_data/twitter/discrim_by_date_loc_lang.json'
	  		let request = new XMLHttpRequest();
	  		request.open('GET', requestURL);
	  		request.responseType = 'text';
	  		request.send();
	  		//处理来自服务器的数据
	  		var locationArray = new Array();
	  		var result = []
	  		request.onload = function() {
	  		        let crimeText = request.response;
	  		        let crimeJson = JSON.parse(crimeText);
	  		        let rows = crimeJson['rows']
	  				for (let i = 0; i < rows.length; i++){
	  					for(let j=0; j< rows[i]['value'];j++){
	  						locationArray.push(rows[i]['key'][1])
	  					}
	  				}
	  				console.log(locationArray.length)
	  				for(let i = 0; i < locationArray.length; i++){
	  					result.push(new google.maps.LatLng(locationArray[i][1],locationArray[i][0]))
	  			}
	  		}
	  	
	    return result
	  
	  }
      function changeGradient() {
        var gradient = [
          'rgba(0, 255, 255, 0)',
          'rgba(0, 255, 255, 1)',
          'rgba(0, 191, 255, 1)',
          'rgba(0, 127, 255, 1)',
          'rgba(0, 63, 255, 1)',
          'rgba(0, 0, 255, 1)',
          'rgba(0, 0, 223, 1)',
          'rgba(0, 0, 191, 1)',
          'rgba(0, 0, 159, 1)',
          'rgba(0, 0, 127, 1)',
          'rgba(63, 0, 91, 1)',
          'rgba(127, 0, 63, 1)',
          'rgba(191, 0, 31, 1)',
          'rgba(255, 0, 0, 1)'
        ]
        heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
      }

      function changeRadius() {
        heatmap.set('radius', heatmap.get('radius') ? null : 20);
      }

      function changeOpacity() {
        heatmap.set('opacity', heatmap.get('opacity') ? null : 0.2);
      }
	  
	  
	  
	  
	  