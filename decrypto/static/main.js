var checkBox = document.getElementById("keyPresent");
var text = document.getElementById("keyInput");
var text2 = document.getElementById("keyUnknownLabel");
var checkBox2 = document.getElementById("keyUnknown")


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
    setTimeout(() => btnSubmit.disabled = false, 2000);

    const jsonFormData = buildJsonFormData(form);
    myJSON = JSON.stringify(jsonFormData);

    console.log(jsonFormData)

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
    if (checkBox.checked == true) {
        checkBox2.checked = false;
    }
    if (checkBox2.checked == true) {
        checks["break"] = true;
        jsonFormData["key"] = ""
    }
    const newObj = Object.assign({}, jsonFormData, checks);
    return newObj;
}

const form = document.getElementById("form");
if (form) {
    form.addEventListener("submit", function(e) {
        submitForm(e, this);
    });
}