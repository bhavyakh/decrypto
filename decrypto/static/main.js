function isKeyPresent() {
    var checkBox = document.getElementById("keyPresent");
    var text = document.getElementById("keyInput");
    var text2 = document.getElementById("keyUnknownLabel");
    var checkBox2 = document.getElementById("keyUnknown")
    if (checkBox.checked == true) {
        text.style.display = "block";
        text2.style.display = "block";
    } else {
        text.style.display = "none";
        text2.style.display = "none";
    }
    if (checkBox2.checked != true) {
        text.style.display = "block";
    } else {
        text.style.display = "none";
    }
}