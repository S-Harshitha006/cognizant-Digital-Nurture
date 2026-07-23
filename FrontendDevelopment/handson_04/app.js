import { courses } from "./data.js";

let courseList = [...courses];

const grid = document.querySelector(".course-grid");
const totalCredits = document.querySelector("#total-credits");
const search = document.querySelector("#search-courses");
const sortBtn = document.querySelector("#sort-btn");
const selected = document.querySelector("#selected-course");

const loadingCourses = document.querySelector("#loading-courses");

const loadingPosts = document.querySelector("#loading-posts");
const notificationList = document.querySelector("#notification-list");
const errorMessage = document.querySelector("#error-message");
const retryBtn = document.querySelector("#retry-btn");


/* =========================================
   ES6 Practice
========================================= */

courseList.forEach(({ name, credits }) => {
    console.log(`${name} (${credits} credits)`);
});

const formatted = courseList.map(
    ({ code, name, credits }) =>
        `${code} — ${name} (${credits} credits)`
);

console.log(formatted);

const filtered = courseList.filter(course => course.credits >= 4);

console.log(filtered.length);

const total = courseList.reduce(
    (sum, course) => sum + course.credits,
    0
);

console.log(total);


/* =========================================
   Promise Example
========================================= */

function fetchUser(id){

    return fetch(
        `https://jsonplaceholder.typicode.com/users/${id}`
    )
    .then(response=>response.json())
    .then(user=>console.log(user.name));

}

fetchUser(1);


/* =========================================
   Async Await
========================================= */

async function fetchUserAsync(id){

    try{

        const response =
        await fetch(
            `https://jsonplaceholder.typicode.com/users/${id}`
        );

        const user = await response.json();

        console.log(user.name);

    }

    catch(error){

        console.error(error);

    }

}

fetchUserAsync(2);


/* =========================================
   Promise.all
========================================= */

Promise.all([

fetch("https://jsonplaceholder.typicode.com/users/1").then(r=>r.json()),

fetch("https://jsonplaceholder.typicode.com/users/2").then(r=>r.json())

])

.then(users=>{

console.log(users[0].name);

console.log(users[1].name);

});


/* =========================================
   Simulated Delay
========================================= */

function fetchAllCourses(){

return new Promise(resolve=>{

setTimeout(()=>{

resolve(courseList);

},1000);

});

}


/* =========================================
   Render Courses
========================================= */

function render(data){

grid.innerHTML="";

data.forEach(course=>{

const article=document.createElement("article");

article.className="course-card";

article.dataset.id=course.id;

article.innerHTML=`

<h3>${course.name}</h3>

<p>${course.code}</p>

<p>Credits : ${course.credits}</p>

<p>Grade : ${course.grade}</p>

`;

grid.appendChild(article);

});

totalCredits.textContent=
`Total Credits : ${
data.reduce((sum,c)=>sum+c.credits,0)
}`;

}


/* =========================================
   Loading Courses
========================================= */

loadingCourses.style.display="block";

fetchAllCourses()

.then(data=>{

loadingCourses.style.display="none";

render(data);

});


/* =========================================
   Search
========================================= */

search.addEventListener("input",()=>{

const value=search.value.toLowerCase();

const result=courseList.filter(course=>

course.name.toLowerCase().includes(value)

);

render(result);

});


/* =========================================
   Sort
========================================= */

sortBtn.addEventListener("click",()=>{

courseList.sort(

(a,b)=>b.credits-a.credits

);

render(courseList);

});


/* =========================================
   Event Delegation
========================================= */

grid.addEventListener("click",(event)=>{

const card=event.target.closest(".course-card");

if(!card) return;

const id=Number(card.dataset.id);

const course=

courseList.find(c=>c.id===id);

selected.textContent=

`Selected Course : ${course.name} | Grade : ${course.grade}`;

});


/* =========================================
   Fetch API
========================================= */

async function apiFetch(url){

const response=await fetch(url);

if(!response.ok){

throw new Error("Unable to fetch data.");

}

return await response.json();

}


/* =========================================
   Notifications
========================================= */

async function loadNotifications(){

loadingPosts.style.display="block";

notificationList.innerHTML="";

errorMessage.textContent="";

retryBtn.style.display="none";

try{

const posts=await apiFetch(

"https://jsonplaceholder.typicode.com/posts?_limit=6"

);

loadingPosts.style.display="none";

posts.forEach(post=>{

const div=document.createElement("div");

div.className="notification-card";

div.innerHTML=`

<h3>${post.title}</h3>

<p>${post.body}</p>

`;

notificationList.appendChild(div);

});

}

catch(error){

loadingPosts.style.display="none";

errorMessage.textContent=error.message;

retryBtn.style.display="inline-block";

}

}

loadNotifications();


/* =========================================
   Retry
========================================= */

retryBtn.addEventListener("click",()=>{

loadNotifications();

});


/* =========================================
   Simulated Error
========================================= */

async function simulate404(){

try{

await apiFetch(

"https://jsonplaceholder.typicode.com/nonexistent"

);

}

catch(error){

console.log(error.message);

}

}

simulate404();


/* =========================================
   Axios Interceptor
========================================= */

axios.interceptors.request.use(config=>{

console.log(

"API call started :",

config.url

);

return config;

});


/* =========================================
   Axios Example
========================================= */

async function axiosExample(){

try{

const response=

await axios.get(

"https://jsonplaceholder.typicode.com/posts",

{

params:{userId:1},

timeout:5000

}

);

console.log(response.data);

}

catch(error){

console.log(error);

}

}

axiosExample();


/* =========================================
Fetch vs Axios

1. Fetch requires response.ok check.
   Axios throws automatically.

2. Fetch requires response.json().
   Axios parses JSON automatically.

3. Axios supports interceptors,
   timeout and request cancellation.

========================================= */