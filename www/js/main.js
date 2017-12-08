function get_meta() {
	var request = new XMLHttpRequest();
	request.open("GET", "http://student04.cse.nd.edu:51049/meta/", true);

	request.onload = function(e) {
		var response = JSON.parse(request.responseText);
		var e = document.getElementById("sel1")
		var num = e.options[e.selectedIndex].value;
		for (i = 0; i < 5; i++) {
			document.getElementById('top' + i).src = "#";
			document.getElementById('jg' + i).src = "#";
			document.getElementById('mid' + i).src = "#";
			document.getElementById('bot' + i).src = "#";
		}
		for (i = 0; i < num; i++) {
			document.getElementById("top" + i).src = "http://ddragon.leagueoflegends.com/cdn/6.24.1/img/champion/" + response["TOP"][i][0] + ".png"
			document.getElementById("jg" + i).src = "http://ddragon.leagueoflegends.com/cdn/6.24.1/img/champion/" + response["JUNGLE"][i][0] + ".png"
			document.getElementById("mid" + i).src = "http://ddragon.leagueoflegends.com/cdn/6.24.1/img/champion/" + response["MID"][i][0] + ".png"
			document.getElementById("bot" + i).src = "http://ddragon.leagueoflegends.com/cdn/6.24.1/img/champion/" + response["BOTTOM"][i][0] + ".png"
		}
		for (i = 1; i < 5; i++) {
			document.getElementById("lr" + i).style.visibility = "visible";
		}
	}
	request.send(null);
}
function post_meta_champ_id(meta_vote) {
	champ_id = document.getElementById("champ_id");
	lane = document.getElementById("sel2");

	var dict = {"lane": lane, "meta_vote": meta_vote};
	var json_dict = JSON.stringify(dict);

	var request = new XMLHttpRequest();
	request.open("POST", "http://student04.cse.nd.edu:51049/meta/" + champ_id , true);

	// request.onload = function(e) { }

	request.send(json_dict);
}

// On window load.
$(document).ready(function() {
	v = document.getElementById('video')
	v.play();
});