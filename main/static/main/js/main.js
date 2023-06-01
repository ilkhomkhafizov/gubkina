const tech_radio = document.getElementById('id_major_choice_0');
const eco_radio = document.getElementById('id_major_choice_1');
const eco_box = document.querySelector('.eco_box');
const tech_box = document.querySelector('.tech_box');
const two_programs = document.querySelector('.two_programs');
const faculty_types = document.querySelectorAll(".faculty_type");


function toggle_visible() {
    if(tech_radio.checked) {
        eco_box.style.display = "none";
        tech_box.style.display = "block";
        two_programs.style.justifyContent = "space-between";
    }else if(eco_radio.checked) {
        tech_box.style.display = "none";
        eco_box.style.display = "block";
        two_programs.style.justifyContent = "flex-end";
    }
}

faculty_types.forEach((faculty) => {
    faculty.addEventListener('click', toggle_visible)
})
