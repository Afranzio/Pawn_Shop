var name = document.getElementById("name")
var number = document.getElementById("number")
var location = document.getElementById("location")
var place = document.getElementById("place")
var itemType = document.getElementById("item-type")
var item = document.getElementById("item")
var amount = document.getElementById("amount")

function newUser(){
    let a = await eel.fetchUser(name,number)();
}