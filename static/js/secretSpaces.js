// this js file is referenced in base.html

var secretSpaces = {
	init: function(){
		this.events();
	},

	events: function(){
		var self = this;
		$('.get-location').on("click", function(e){
			e.preventDefault();
			self.getLocation();
		});
	},

	getLocation: function(){
		if (navigator.geolocation) {
    		navigator.geolocation.getCurrentPosition(showPosition);
		}	else { 
	    	console.log ("Geolocation is not supported by this browser.");
		}
	},

	// showPosition: function(){
	// 	x.innerHTML = "Latitude: " + position.coords.latitude + 
	// 	    "Longitude: " + position.coords.longitude;
	// 	    var longitude = position.coords.longitude;
	// 	    var latitude = position.coords.latitude;
	// 	}
	// },

	// storePosition: function(){
	// 	$('.container').append("<input id='bomb' type='hidden' name='bomb' value=" + longitude + "," + latitude + "/>");
	// 	};
	// },

	// getCoords: function(){
	// 	$.get("/pushcoords?lat=" + position.coords.latitude + 
	// 			"&long=" + position.coords.longitude, function(data){
	// 	    	// came back from server
	// 	    	console.log("I came back from the server!");
	// 	    	console.log(data);
	// 	    	debugger;
	// });
};

$(document).ready(function() {
  secretSpaces.init();
});