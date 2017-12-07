// function Item() {
//     this.addToDocument = function() {
//         document.body.appendChild(this.item);
//     };
// }

// function Label() {
//     this.createLabel = function(text, id) {
//         this.item = document.createElement("p");

//         this.id = id;
//         this.item.setAttribute("id", this.id);
//         this.item.innerHTML = text;
//     };

//     this.setText = function(text) {
//         this.item.innerHTML = text;
//     };
//     this.getItem = function() {
//         return this.item;
//     };
// }
// function Button() {
//     this.createButton = function(text, id) {
//         this.item = document.createElement("button");
//         this.item.setAttribute("id", id);
//         this.item.innerHTML = text;
//     };
//     this.addClickEventHandler = function(handler) {
//         this.item.onmouseup = function() {
//             handler();
//         };
//     };
//     this.getItem = function() {
//         return this.item;
//     };
// }

// function Format() {
//     this.createFormat = function(id) {
//         this.item = document.createElement("div");
//         this.id = id;
//         this.item.setAttribute("id", this.id);
//     };
    
//     this.appendChild = function(child) {
//         this.item.appendChild(child);
//     };

//     this.getItem = function() {
//         return this.item;
//     };
// }
// Button.prototype = new Item();
// Format.prototype = new Item();
// Label.prototype = new Item();
