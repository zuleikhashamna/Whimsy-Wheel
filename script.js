const taskInput = document.getElementById("taskInput");
const taskList = document.getElementById("taskList");

function addTask(){

    if(taskInput.value.trim()===""){
        alert("Please enter a task!");
        return;
    }

    const li=document.createElement("li");

    const span=document.createElement("span");
    span.textContent=taskInput.value;

    span.onclick=function(){
        span.classList.toggle("completed");
    };

    const del=document.createElement("button");
    del.textContent="🗑";
    del.className="delete";

    del.onclick=function(){
        li.remove();
    };

    li.appendChild(span);
    li.appendChild(del);

    taskList.appendChild(li);

    taskInput.value="";
}