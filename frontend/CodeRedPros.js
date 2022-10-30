
formSubmission = document.getElementById("submitForm");
let allLIs = document.querySelectorAll("li");


formSubmission.addEventListener("click", function () {
    location.href = "http://localhost:63342/CodeRedPros/frontend/presentationScreen.html"

})


function sendDataInput() {
    for(let i = 0; i < allLIs.length; i++){
        if(allLIs[i].classList.contains("active")){
           let id = allLIs[i].getAttribute("id");
           let size;
           let use;
           let price;
           if(allLIs[i].classList.contains("pcSize")){
               size = id;
           }
        }
    }



    let xhttp = new XMLHttpRequest();
    xhttp.open("POST", `http://127.0.0.1:8000/api/${query}/?format=json`, false);
    xhttp.send();
    if (xhttp.status !== 404) {
        let data = JSON.parse(xhttp.responseText);
        console.log(data)
        return data;
    }
    return false;

}