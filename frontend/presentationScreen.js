
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
    });
})





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

