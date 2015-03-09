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

	getCoords: function(){
		$.get("/pushcoords?lat=" + position.coords.latitude + 
				"&long=" + position.coords.longitude, function(data){
		    	// came back from server
		    	console.log("I came back from the server!");
		    	console.log(data);
		    	debugger;
	})
};


$(document).ready(function() {
  secretSpaces.init();
});