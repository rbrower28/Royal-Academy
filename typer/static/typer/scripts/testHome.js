
let page = document.querySelector("html");

let h = window.innerHeight;

console.log(h);
console.log(page.offsetHeight);

// page.offsetHeight = h;

page.setAttribute("height", h);

// console.log(page.offsetHeight);
