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
	}
};


$(document).ready(function() {
  secretSpace.init();
});