// this js file is referenced in base.html

var secretSpaces = {
	init: function(){
		this.events();
	},

	events: function(){
		debugger;
		var self = this;
		$('#get-location').on("click", function(e){
			e.preventDefault();
			self.getLocation();
		});
	},

	showPosition: function(longitude, latitude){
		$('.container').append("<input id='bomb' type='hidden' name='bomb' value=" + longitude + "," + latitude + "/>");
	},

	getCoords: function(position){
		$.get("/pushcoords?lat=" + position.coords.latitude + 
				"&long=" + position.coords.longitude, function(data){
		    	// came back from server
		    	console.log("I came back from the server!");
		    	console.log(data);
		    	debugger;
		});
	},

	storePosition: function(position){
		var self = this;
		alert("STORE POSITION");
		debugger;
		var coordinates = "Latitude: " + position.coords.latitude + 
		    "Longitude: " + position.coords.longitude;
		    var longitude = position.coords.longitude;
		    var latitude = position.coords.latitude;
		self.showPosition(longitude, latitude); //FIXME - undefined is not a function, 'this' is a window (should be an object)
		self.getCoords(position); //FIXME - undefined is not a function
	},

	getLocation: function(){
		debugger;
		if (navigator.geolocation) {
    		navigator.geolocation.getCurrentPosition(this.storePosition);
		}	else { 
	    	console.log ("Geolocation is not supported by this browser.");
		}
	},


};

$(document).ready(function() {
  secretSpaces.init();
});