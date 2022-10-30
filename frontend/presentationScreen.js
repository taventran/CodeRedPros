
let statCards = document.querySelectorAll(".statCard")
let partCards = document.querySelectorAll(".card")


let anchorOne = document.getElementById("anchorOne")
let anchorTwo = document.getElementById("anchorTwo")
let anchorThree = document.getElementById("anchorThree")
let imgOne = document.getElementById("imageOne")
let imgTwo = document.getElementById("imageTwo")
let imgThree = document.getElementById("imageThree")

let useCase = 3

statCards.forEach((statCard) => {
    statCard.addEventListener("click", () => {
        statCard.classList.toggle("isOpen");
        if(statCard.getAttribute("id") === "thirdStat"){
            setImages();
            let curr = document.getElementById("softwareRecommended");
            curr.classList.toggle("active");
            document.querySelectorAll(".recIcons").forEach((recIcon) => {
                recIcon.classList.toggle("activeImg");
            })
        }
        if(statCard.getAttribute("id") === "firstStat"){
            let curr = document.getElementById("priceBreakdown");
            curr.classList.toggle("active");
        }
        if(statCard.getAttribute("id") === "secondStat"){
            let curr = document.getElementById("partsCompared");
            curr.classList.toggle("active");
        }
        if(statCard.getAttribute("id") === "fourthStat"){
            let curr = document.getElementById("tips");
            curr.classList.toggle("active");
        }
    })
})

function off() {
    document.getElementById("overlay").style.display = "none";
}

partCards.forEach((partCard) => {
    partCard.addEventListener("click", function () {
        let overlay = document.getElementById("overlay");
        overlay.style.display = "block";
        let overlayTitle = document.getElementById("Title");
        let overlayDescription = document.getElementById("Desc");
        switch (this.id){
            case "cpu":
                overlayTitle.innerHTML = "CPU";
                overlayDescription.innerHTML = "The CPU, or Central Processing Unit, is the brains of your computer. It handles all the tasks sent at it and manages everything you may need.";
                break;
            case "cpucooler":
                overlayTitle.innerHTML = "CPU Cooler";
                overlayDescription.innerHTML = "The CPU Cooler is designed to keep the brains of your computer cool. It is a vital part of any build and should be kept clean and in good condition.";
                break;
            case "ram":
                overlayTitle.innerHTML = "RAM";
                overlayDescription.innerHTML = "The RAM, or Random Access Memory, is used to temporarily store data for your computer to handle in its processing. The data gets cleared whenever you reset your computer, but usually, a safe shutdown will prevent any important data lost";
                break;
            case "gpu":
                overlayTitle.innerHTML = "GPU";
                overlayDescription.innerHTML = "The GPU, or video card, is used primarily to process graphical information, from images to video games. It is the most important part of a gaming PC, as it is the part that will determine how well your games will run. The GPU is also used to process video and images, so it is important to have a good one if you plan on doing any video editing or photo editing.";
                break;
            case "storage":
                overlayTitle.innerHTML = "Storage";
                overlayDescription.innerHTML = "This is where data is stored on your computer. This is where your operating system, programs, and files are stored. The more storage you have, the more data you can store on your computer. The more data you have, the more your computer will have to work to access it. This can slow down your computer. If you have a lot of data, you should consider getting a larger storage drive.";
                break;
            case "case":
                overlayTitle.innerHTML = "Case";
                overlayDescription.innerHTML = "This is what holds all your precious computer parts, keeping it safe and cool. It also has a window so you can show off your build.";
                break;
            case "psu":
                overlayTitle.innerHTML = "Power Supply";
                overlayDescription.innerHTML = "This is what powers your computer. It converts the electricity from your wall outlet into the electricity your computer needs to run.";
                break;
            case "mobo":
                overlayTitle.innerHTML = "Motherboard";
                overlayDescription.innerHTML = "This is the main circuit board of your computer. It connects all the other parts together.";
                break;
            default:
                break;
        }
})})

function setImages(){
    switch (useCase) {
        case 1:
            anchorOne.href = "https://store.steampowered.com/"
            anchorTwo.href = "https://us.shop.battle.net/en-us?from=root"
            anchorThree.href = "https://discord.com/"
            imgOne.setAttribute("src", "assets/steam.png")
            imgTwo.setAttribute("src", "assets/Battlenet.png")
            imgThree.setAttribute("src", "assets/discord.png")
            break;
        case 2:
            anchorOne.href = "https://www.notion.com/"
            anchorTwo.href = "https://www.malwarebytes.com/"
            anchorThree.href = "https://www.spotify.com/"
            imgOne.setAttribute("src", "assets/Notion.png")
            imgTwo.setAttribute("src", "assets/malwarebytes.png")
            imgThree.setAttribute("src", "assets/spotify.png")
            break;
        case 3:
            anchorOne.href = "https://www.notion.com/"
            anchorTwo.href = "https://www.slack.com/"
            anchorThree.href = "https://www.office365.com/"
            imgOne.setAttribute("src", "assets/Notion.png")
            imgTwo.setAttribute("src", "assets/slack.png")
            imgThree.setAttribute("src", "assets/office365.png")
            break;
        case 4:
            anchorOne.href = "https://www.canva.com/"
            anchorTwo.href = "https://www.figma.com/"
            anchorThree.href = "https://www.adobe.com/"
            imgOne.setAttribute("src", "assets/canva.png")
            imgTwo.setAttribute("src", "assets/figma.png")
            imgThree.setAttribute("src", "assets/adobe.png")

            break;
        case 5:
            anchorOne.href = "https://www.notion.com/"
            anchorTwo.href = "https://www.groupme.com/"
            anchorThree.href = "https://www.office365.com/"
            imgOne.setAttribute("src", "assets/Notion.png")
            imgTwo.setAttribute("src", "assets/groupme.png")
            imgThree.setAttribute("src", "assets/office365.png")

            break;
        default:
            break;
        }

}

