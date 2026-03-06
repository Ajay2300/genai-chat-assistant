function sendMessage(){

let input = document.getElementById("user-input");
let message = input.value;

if(message.trim() === "") return;

let messages = document.getElementById("messages");

messages.innerHTML += "<p><b>You:</b> "+message+"</p>";

fetch("/chat",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({message:message})
})
.then(res=>res.json())
.then(data=>{
messages.innerHTML += "<p><b>Assistant:</b> "+data.reply+"</p>";
});

input.value="";
}