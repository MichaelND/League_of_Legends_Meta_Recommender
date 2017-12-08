function get_meta() {
	var request = new XMLHttpRequest();
	request.open("GET", "http://student04.cse.nd.edu:51049/meta/", true);

	request.onload = function(e) {
		var response = JSON.parse(request.responseText);
		// var e = document.getElementById("sel1")
		// var num = e.options[e.selectedIndex].value;
		for (i = 0; i < 5; i++) {
			document.getElementById("lane-row" + i).setAttribute("hidden", true)
			document.getElementById("top" + i).src = "http://ddragon.leagueoflegends.com/cdn/6.24.1/img/champion/" + response["TOP"][i][0] + ".png"
			// document.getElementById("jg" + i).src = "http://ddragon.leagueoflegends.com/cdn/6.24.1/img/champion/" + response["JUNGLE"][i][0] + ".png"
			// document.getElementById("mid" + i).src = "http://ddragon.leagueoflegends.com/cdn/6.24.1/img/champion/" + response["MID"][i][0] + ".png"
			// document.getElementById("bot" + i).src = "http://ddragon.leagueoflegends.com/cdn/6.24.1/img/champion/" + response["BOTTOM"][i][0] + ".png"
			
			// document.getElementById("top" + i).innerHTML = response["TOP"][i][0]
		}
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
function get_champ_id(champ_id) {
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


