
let statCards = document.querySelectorAll(".statCard")

statCards.forEach((statCard) => {
    statCard.addEventListener("click", () => {
        statCard.classList.toggle("isOpen");
        console.log("hovered");
    })
})