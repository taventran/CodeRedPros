
formSubmission = document.getElementById("submitForm");
let allLIs = document.querySelectorAll("li");


formSubmission.addEventListener("click", function () {
    location.href = "http://localhost:63342/CodeRedPros/frontend/presentationScreen.html"
    sendDataInput();
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
               console.log(size)
           }
           if(allLIs[i].classList.contains("budget")){
                price = id.substring(id.length-1);
               console.log(price)
            }
            if(allLIs[i].classList.contains("usage")){
                use = id.substring(id.length-1);

                console.log(use)
            }
            if (allLIs[i].classList.contains("aesthetic")) {
                aesthetic = id.substring(id.length-1);
            }
        }
    }

    return fetch(`http://127.0.0.1:8000/api/userdata/`, {
        method: 'POST',
        body: JSON.stringify({
            "size": size,
            "use": use,
            "price": price,
            "aesthetic": aesthetic,
        }),
        headers: {
            'Content-Type': 'application/json',
        }
    }).catch((error) => {
        console.error('Error:', error);
    });
    // let xhttp = new XMLHttpRequest();
    // xhttp.open("POST", `http://127.0.0.1:8000/api/userdata/`, false);
    // xhttp.setRequestHeader("use", use)
    // xhttp.setRequestHeader("size", size)
    // xhttp.setRequestHeader("price", price)
    // xhttp.setRequestHeader("aesthetic", aesthetic)
    // xhttp.send();
    // if (xhttp.status !== 404) {
    //     console.log("success")
    //     return true;
    // }
    // return false;

}