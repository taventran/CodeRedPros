
formSubmission = document.getElementById("submitForm");

formSubmission.addEventListener("click", function () {
    location.href = "http://localhost:63342/CodeRedPros/frontend/presentationScreen.html"
    getPartList("CPU");
})


function getPartList(query) {
    let xhttp = new XMLHttpRequest();
    xhttp.open("GET", `http://127.0.0.1:8000/api/${query}/?format=json`, false);
    xhttp.send();
    if (xhttp.status !== 404) {
        let data = JSON.parse(xhttp.responseText);
        console.log(data)
        return true;
    }
    return false;

}