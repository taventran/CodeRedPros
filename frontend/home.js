//Get all dropdowns drom the document
const dropdowns = document.querySelectorAll('.dropdown');

//Loop through all the dropdown elemtns
dropdowns.forEach(dropdown => {
    //Get inner elemtns from each dropdown
    const select = dropdown.querySelector('.select');
    const caret = dropdown.querySelector('.caret');
    const menu = dropdown.querySelector('.menu');
    const options = dropdown.querySelectorAll('.menu li');
    const selected = dropdown.querySelector('.selected');

    //Add a click event to the select element
    select.addEventListener('click', () => {
        //add the clicked select styles to the select element
        select.classList.toggle('select-clicked');
        //Add the rotate styles to the caret element
        caret.classList.toggle('caret-rotate');
        //Add the open styles to the menu elemtn
        menu.classList.toggle('menu-open');
    });

    //Loop through all the option elemtns
    options.forEach(option => {
        //add a click event to the option element'
        option.addEventListener('click', () => {
            //change selcted inner text to click option inner text
            selected.innerText = option.innerText;
            //Add the clicked slelect styles to the select elemenst
            select.classList.remove('select-clicked');
            //Add the rotate styles to the caret eleemnt
            caret.classList.remove('caret-rotate');
            //Add the open styles to the menu ekement
            menu.classList.remove('menu-open');
            //Remove active class rom al the option eleemnts
            options.forEach(option => {
                option.classList.remove('active');
            });
            //Add active class tp cicked option elelemnt
            option.classList.add('active');
        });
    });
});