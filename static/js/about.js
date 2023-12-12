function toggleText(id) {
    var textElement = document.getElementById(id);
    var imageElement = document.getElementById(id + "_img");

    if (textElement.style.display === "none") {
        textElement.style.display = "block";
    } else {
        textElement.style.display = "none";
    }
}

function tested(){
alert("123");
}