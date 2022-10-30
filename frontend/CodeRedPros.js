
formSubmission = document.getElementById("submitForm");
let allLIs = document.querySelectorAll("li");


formSubmission.addEventListener("click", function () {
    location.href = "http://localhost:63342/CodeRedPros/frontend/presentationScreen.html"

})


function sendDataInput() {
    let size;
    let use;
    let price;
    let aesthetic;
    for(let i = 0; i < allLIs.length; i++){
        if(allLIs[i].classList.contains("active")){
           let id = allLIs[i].getAttribute("id");

           if(allLIs[i].classList.contains("pcSize")){
               size = id.substring(id.length-1);
           }
           if(allLIs[i].classList.contains("budget")){
                price = id.substring(id.length-1);
            }
            if(allLIs[i].classList.contains("usage")){
                use = id.substring(id.length-1);
            }
            if (allLIs[i].classList.contains("aesthetic")) {
                aesthetic = id.substring(id.length-1);
            }
        }
    }
    let xhttp = new XMLHttpRequest();
    xhttp.open("POST", `http://127.0.0.1:8000/api/userdata/`, false);
    xhttp.setRequestHeader("use", use)
    xhttp.setRequestHeader("size", size)
    xhttp.setRequestHeader("price", price)
    xhttp.setRequestHeader("aesthetic", aesthetic)
    xhttp.send();
    if (xhttp.status !== 404) {
        let data = JSON.parse(xhttp.responseText);
        console.log(data)
        return true;
    }
    return false;

}