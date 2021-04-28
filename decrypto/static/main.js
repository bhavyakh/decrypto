var checkBox = document.getElementById("keyPresent");
var text = document.getElementById("keyInput");
var text2 = document.getElementById("keyUnknownLabel");
var checkBox2 = document.getElementById("keyUnknown");
var modal = document.getElementById("myModal");
maindict = {}

function isKeyPresent() {
    if (checkBox.checked == true) {
        text.style.display = "block";
        text2.style.display = "block";
    } else {
        text.style.display = "none";
        text2.style.display = "none";
    }
    if (checkBox2.checked == true) {
        text.style.display = "none";
    }
}


async function submitForm(e, form) {
    e.preventDefault();

    const btnSubmit = document.getElementById('btnSubmit');
    btnSubmit.disabled = true;
    setTimeout(() => btnSubmit.disabled = false, 4000);

    var moda = document.getElementById("myModal")
    moda.modal("show");

    const jsonFormData = buildJsonFormData(form);
    myJSON = JSON.stringify(jsonFormData);

    (async() => {
        const rawResponse = await fetch('/submit', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: myJSON
        });
        const content = await rawResponse.json();
        printOutput(content)
        maindict = content
        console.log(content);
    })();


}

function buildJsonFormData(form) {
    jsonFormData = {};
    for (const pair of new FormData(form)) {
        jsonFormData[pair[0]] = pair[1];
    }
    checks = { "break": false };
    if (checkBox.checked != true) {
        jsonFormData["key"] = ""
    }

    if (checkBox2.checked == true) {
        checks["break"] = true;
        jsonFormData["key"] = ""
    }
    const newObj = Object.assign({}, jsonFormData, checks);
    return newObj;
}

function printOutput(content) {
    const out = (content);


    // Select only the ciphers that had english words in them
    const final = out["english"];
    var outputField = document.getElementById("output");
    outputField.style.display = "block"
    var rows = document.getElementsByTagName("tbody")[0];
    var i;
    const keys = Object.keys(final)
    const values = Object.values(final)
    rows.style.display = "table-row-group"
    var innerData = ""
    for (i = 0; i < keys.length; i++) {
        innerData += '<tr>' + '<td>' + keys[i] + '</td>' + '<td>' + values[i] + '</td>' + '</tr>'
    }
    rows.innerHTML = innerData
}

const form = document.getElementById("form");
if (form) {
    form.addEventListener("submit", function(e) {
        submitForm(e, this);
    });
}


// Show all possible outputs

window.onload = function() {
    document.getElementById("all").onclick = allOut;
}

function allOut() {

    modal.style.display = "block";
    var allcontent = document.getElementById("allContent")
    allcontent.innerHTML = JSON.stringify(maindict, null, 4)

}
// Get the button that opens the modal

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}