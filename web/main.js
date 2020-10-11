async function reliver(){
    let name = document.getElementById("name").value;
    let number = document.getElementById("number").value;
    // let output = document.getElementById("output");
    eel.connectDB()();
    const result = await eel.fetchUser(name, number)();
    console.log(name, number)
    console.log(result["Amount"])

    var Elements = ["Name", "Number", "Amount", "S/O W/O D/O", "Location", "Place", "Item", "Pledged Date", "Weight"]; 

    function AddNewElementsByJquery() { 
        for (var i = 0; i < Elements.length; i++) { 
        $("#output") 
        .append('<li>' + Elements[i] + " : " + result[Elements[i]] + '</li>'); 
        } 
    } 
    AddNewElementsByJquery()
}   


async function surrender(){
    let name = document.getElementById("name").value;
    let number = document.getElementById("number").value;
    let location = document.getElementById("location").value;
    let place = document.getElementById("place").value;
    let mobile = document.getElementById("mobile").value;
    let itemType = document.getElementById("item-type").value;
    let item = document.getElementById("item").value;
    let amount = document.getElementById("amount").value;
    let relation = document.getElementById("S/O W/O D/O").value;
    let pledgedDate = document.getElementById("Pledged Date").value;
    let weight = document.getElementById("weight").value;
    document.getElementById("name").value = "";
    document.getElementById("number").value = "";
    document.getElementById("location").value = "";
    document.getElementById("place").value = "";
    document.getElementById("mobile").value = "";
    document.getElementById("item-type").value = "";
    document.getElementById("item").value = "";
    document.getElementById("amount").value = "";
    document.getElementById("S/O W/O D/O").value = "";
    document.getElementById("Pledged Date").value = "";
    document.getElementById("weight").value = "";
    await eel.connectDB()();
    eel.newUser(number, amount, name, relation, location, place, item, itemType, mobile, pledgedDate, weight)();
}

async function jewel(){
    // let name = document.getElementById("name").value;
    await eel.capture("Mani")();

}