console.log("hi")
// var top = new Button();
// var mid = new Button();
// var jungle = new Button();
// var bot_sup = new Button();

// var top_label = new Label();
// var mid_label = new Label();
// var jungle_label = new Label();
// var bot_sup_label = new Label();

// top_label.createLabel("The top lane", "top");
// top.createButton("Top", "top");
// mid.createButton("Mid", "mid");
// jungle.createButton("Jungle", "jungle");
// bot_sup.createButton("Bot/Sup", "bot-sup");

// top.addClickEventHandler(get_top_meta);
// mid.addClickEventHandler(get_mid_meta);
// jungle.addClickEventHandler(get_jungle_meta);
// bot_sup.addClickEventHandler(get_bot_sup_meta);

// var main = new Format();
// main.createFormat("main");
// main.appendChild(top_label.getItem());

// main.addToDocument();

function get_top_meta() {
	var request = new XMLHttpRequest();
	request.open("GET", "http://student04.cse.nd.edu:51049/champion/15", true);

	request.onload = function(e) {
		var response = JSON.parse(request.responseText);
		// top_label.setText(response["c_name"]);
		console.log(response["c_name"])
	}
	request.send(null);
}
function get_mid_meta() {
	// var request = new XMLHttpRequest();
	// request.open("GET", "http://student04.cse.nd.edu:51049/movies/" + mid, true);
	
	// request.onload = function(e) {
 //                var response = JSON.parse(request.responseText);
	// 	movie.setText(response["title"]);
	// 	image.setImage(response["img"]);
 //        }
 //        request.send(null);
}
function get_jungle_meta() {
	// var request = new XMLHttpRequest();
	// request.open("GET", "http://student04.cse.nd.edu:51049/ratings/" + mid, true);

 //        request.onload = function(e) {
 //                var response = JSON.parse(request.responseText);
	// 	rating.setText(response["rating"]);
 //        }
 //        request.send(null);
}
function get_bot_sup_meta() {
	// var dict = {"movie_id": mid,"rating": 5};
	// var json_dict = JSON.stringify(dict);

	// var request = new XMLHttpRequest();
	// request.open("PUT", "http://student04.cse.nd.edu:51049/recommendations/" + uid, true);
	// request.onload = function(e) {
	// 	getMovie(uid);
	// }
	// request.send(json_dict);
}


// On window load.
$(document).ready(function() {
	v = document.getElementById('video')
	v.play();
});


