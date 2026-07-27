import { courses } from "./data.js";

let courseList = [...courses];

const grid = document.querySelector(".course-grid");
const totalCredits = document.querySelector("#total-credits");
const search = document.querySelector("#search-courses");
const sortBtn = document.querySelector("#sort-btn");
const selected = document.querySelector("#selected-course");
const resultsCount = document.querySelector("#results-count");

// ES6 Destructuring
courseList.forEach(({ name, credits }) => {
    console.log(`${name} (${credits} credits)`);
});

// map()
const formatted = courseList.map(
    ({ code, name, credits }) =>
        `${code} — ${name} (${credits} credits)`
);

console.log(formatted);

// filter()
const filtered = courseList.filter(
    course => course.credits >= 4
);

console.log(filtered.length);

// reduce()
const total = courseList.reduce(
    (sum, course) => sum + course.credits,
    0
);

console.log(total);

function render(data) {

    grid.innerHTML = "";

    // Accessibility: announce search result count
    resultsCount.textContent = `${data.length} courses found`;

    data.forEach(course => {

        const article = document.createElement("article");

        article.className = "course-card";

        article.dataset.id = course.id;

        // Task 129 - Keyboard Accessibility
        article.tabIndex = 0;

        article.setAttribute("role", "button");

        article.setAttribute(
            "aria-label",
            `${course.name}, ${course.credits} credits`
        );

        article.innerHTML = `
            <h3>${course.name}</h3>

            <p>${course.code}</p>

            <p>Credits : ${course.credits}</p>

            <p>Grade : ${course.grade}</p>
        `;

        grid.appendChild(article);

    });

    totalCredits.textContent =
        `Total Credits : ${
            data.reduce((sum, c) => sum + c.credits, 0)
        }`;

}

render(courseList);

// Search
search.addEventListener("input", () => {

    const value = search.value.toLowerCase();

    const result = courseList.filter(course =>
        course.name.toLowerCase().includes(value)
    );

    render(result);

});

// Sort
sortBtn.addEventListener("click", () => {

    courseList.sort(
        (a, b) => b.credits - a.credits
    );

    render(courseList);

});

// Event Delegation (Mouse Click)
grid.addEventListener("click", (event) => {

    const card = event.target.closest(".course-card");

    if (!card) return;

    const id = Number(card.dataset.id);

    const course = courseList.find(c => c.id === id);

    selected.textContent =
        `Selected : ${course.name} | Grade : ${course.grade}`;

});

// Task 129 - Keyboard Enter Support
grid.addEventListener("keydown", (event) => {

    if (event.key !== "Enter") return;

    const card = event.target.closest(".course-card");

    if (!card) return;

    card.click();

});

// Task 131 - aria-expanded

menuBtn.addEventListener("click",()=>{

const expanded =
menuBtn.getAttribute("aria-expanded")==="true";

menuBtn.setAttribute(
"aria-expanded",
(!expanded).toString()
);

});