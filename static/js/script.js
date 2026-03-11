const messages = document.getElementById("messages");
const form = document.querySelector("form");
const input = document.querySelector("input");


/* AUTO SCROLL */

function scrollBottom(){
messages.scrollTop = messages.scrollHeight;
}

scrollBottom();


/* TYPING EFFECT */

form.addEventListener("submit",function(){

const text = input.value;

const userRow = document.createElement("div");
userRow.className="message-row user-row";

userRow.innerHTML = `
<div class="avatar user-avatar">U</div>
<div class="message">${text}</div>
`;

messages.appendChild(userRow);


const typing = document.createElement("div");
typing.className="message-row";
typing.id="typing";

typing.innerHTML=`
<div class="avatar bot-avatar">AI</div>
<div class="message">AI is typing...</div>
`;

messages.appendChild(typing);

scrollBottom();

});
const toggleBtn = document.getElementById("themeToggle");

/* load saved theme */

if(localStorage.getItem("theme") === "light"){
document.body.classList.add("light-mode");
toggleBtn.innerText="☀ Light";
}

/* toggle theme */

toggleBtn.addEventListener("click", () => {

document.body.classList.toggle("light-mode");

if(document.body.classList.contains("light-mode")){
localStorage.setItem("theme","light");
toggleBtn.innerText="☀ Light";
}else{
localStorage.setItem("theme","dark");
toggleBtn.innerText="🌙 Dark";
}

});
// Sidebar toggle
const menuToggle = document.getElementById("menu-toggle");
const sidebar = document.getElementById("sidebar");

menuToggle.addEventListener("click", function () {
    sidebar.classList.toggle("collapsed");
});

