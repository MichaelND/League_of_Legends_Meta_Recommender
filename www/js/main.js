function get_top_meta() {
	var request = new XMLHttpRequest();
	request.open("GET", "http://student04.cse.nd.edu:51049/champion/15", true);

	request.onload = function(e) {
		var response = JSON.parse(request.responseText);
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