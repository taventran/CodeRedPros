
let statCards = document.querySelectorAll(".statCard")

let anchorOne = document.getElementById("anchorOne")
let anchorTwo = document.getElementById("anchorTwo")
let anchorThree = document.getElementById("anchorThree")
let imgOne = document.getElementById("imgOne")
let imgTwo = document.getElementById("imgTwo")
let imgThree = document.getElementById("imgThree")

let useCase = 4

statCards.forEach((statCard) => {
    statCard.addEventListener("click", () => {
        statCard.classList.toggle("isOpen");
        console.log("hovered");
    })
})



function setImages(){
    switch (useCase) {
        case 1:
            anchorOne.href = "https://store.steampowered.com/"
            anchorTwo.href = "https://us.shop.battle.net/en-us?from=root"
            anchorThree.href = "https://discord.com/"
            imgOne.src = "assets/steam.png"
            imgTwo.src = "assets/battlenet.png"
            imgThree.src = "assets/discord.png"
        case 2:
            anchorOne.href = "https://www.notion.com/"
            anchorTwo.href = "https://www.malwarebytes.com/"
            anchorThree.href = "https://www.spotify.com/"
            imgOne.src = "assets/notion.png"
            imgTwo.src = "assets/malwarebytes.png"
            imgThree.src = "assets/spotify.png"
        case 3:
            anchorOne.href = "https://www.notion.com/"
            anchorTwo.href = "https://www.slack.com/"
            anchorThree.href = "https://www.office365.com/"
            imgOne.src = "assets/notion.png"
            imgTwo.src = "assets/slack.png"
            imgThree.src = "assets/office365.png"
        case 4:
            anchorOne.href = "https://www.canva.com/"
            anchorTwo.href = "https://www.figma.com/"
            anchorThree.href = "https://www.adobe.com/"
            imgOne.src = "assets/canva.png"
            imgTwo.src = "assets/figma.png"
            imgThree.src = "assets/adobe.png"
        case 5:
            anchorOne.href = "https://www.notion.com/"
            anchorTwo.href = "https://www.groupme.com/"
            anchorThree.href = "https://www.office365.com/"
            imgOne.src = "assets/notion.png"
            imgTwo.src = "assets/groupme.png"
            imgThree.src = "assets/office365.png"

    }




    anchorOne.style.backgroundImage = "url(" + imgOne.src + ")";
    anchorTwo.style.backgroundImage = "url(" + imgTwo.src + ")";
    anchorThree.style.backgroundImage = "url(" + imgThree.src + ")";
}

