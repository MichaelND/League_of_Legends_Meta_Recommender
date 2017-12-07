function get_meta() {
	var request = new XMLHttpRequest();
	request.open("GET", "http://student04.cse.nd.edu:51049/meta/", true);

	request.onload = function(e) {
		var response = JSON.parse(request.responseText);
		console.log(response["result"])
	}
	request.send(null);
}
function get_meta_champs(number) {
	var request = new XMLHttpRequest();
	request.open("GET", "http://student04.cse.nd.edu:51049/meta/" + number, true);

	request.onload = function(e) {
		var response = JSON.parse(request.responseText);
		console.log(response["result"])
	}
	request.send(null);
}
function post_meta_champ_id(champ_id, lane, meta_vote) {
	var request = new XMLHttpRequest();
	request.open("POST", "http://student04.cse.nd.edu:51049/meta/" + champ_id , true);

	request.onload = function(e) {
		var response = JSON.parse(request.responseText);
		console.log(response["result"])
	}
	request.send(null);
}
function get_champion_id(champ_id) {
	var request = new XMLHttpRequest();
	request.open("GET", "http://student04.cse.nd.edu:51049/champion/" + champ_id , true);

	request.onload = function(e) {
		var response = JSON.parse(request.responseText);
		console.log(response["result"])
	}
	request.send(null);
}

// On window load.
$(document).ready(function() {
	v = document.getElementById('video')
	v.play();
});


