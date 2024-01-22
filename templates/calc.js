// All declaeration

let sideBar = document.querySelector("aside");
let historyBar = document.getElementById("history");
let linkTag = document.getElementById("theme");
let lightBtn = document.getElementById("light");
let darkBtn = document.getElementById("dark");
let inputBar = document.getElementById("inbar");
let questBar = document.getElementById("ques");
let anserBar = document.getElementById("ans");
let operations = ['+','-','x','/','√','\\','^'];
let operator = '';

// JS functions

function setsize() {    // Resize the screen size
    var y = 600;
    var x;
  
    if(sideBar.style.width != "0px"){x = 510;}
    else{x = 310;};
  
    if(window.innerWidth != x || window.innerHeight != y){
        window.resizeTo(x, y);
        var InnerWidth = x - window.innerWidth;
        var InnerHeight = y - window.innerHeight;
        window.resizeTo(x + InnerWidth, y + InnerHeight);
    };
};

function showaside(){   // Show side bar & other options
    if(sideBar.style.width != "0px"){
        sideBar.style.width = "0px";
        while(sideBar.style.width > "0px"){
            var currentTime = new Date().getTime();
            while(currentTime + 1000 >= new Date().getTime()){};
        };
        historyBar.innerHTML = '';
    }
    else{
        sideBar.style.width = "200px";
        loadHistory();
    };
    setsize();
};

function write_in_bar(key){    // Writing in calculator bar
    inputBar.value += key;
};

function backSpace(){
    if(inputBar.value != ''){inputBar.value = inputBar.value.slice(0,-1);}
    else if(questBar.innerHTML != ''){
        inputBar.value = questBar.innerHTML.slice(0,-1);
        operator = '';
        questBar.innerHTML = '';
    }
}


// Async Functions

async function loadtheme(){
    var theme = document.getElementById("theme");
    if(await eel.LoadTheme()() == "light"){
        theme.href="css/light.css";
        darkBtn.checked=false;lightBtn.checked=true;
    }
    else{
        theme.href="css/dark.css";
        darkBtn.checked=true;lightBtn.checked=false;
    };
};
async function changetheme(theme){
    await eel.py_changetheme(theme)();
    loadtheme();
};
async function calculate(){
    eel.py_takeValues(questBar.innerHTML.slice(0,-1), questBar.innerHTML[questBar.innerHTML.length -1], inputBar.value)
    var result = await eel.py_calculate()();
    console.log(result);
    anserBar.innerHTML = result;
    questBar.innerHTML += inputBar.value;
    inputBar.value = '';
};
async function add_operator(oper){    // Adding operator & ending the number
    if(inputBar.value != '' || anserBar.innerHTML != ''){
        if(inputBar.value == '' && anserBar.innerHTML != ''){
            inputBar.value = anserBar.innerHTML;
            questBar.innerHTML = '';
        }
        if(inputBar.value != '' && questBar.innerHTML != ''){
            calculate();
        }
        if(operator != '' && inputBar.value == ''){
            inputBar.value = questBar.innerHTML.slice(0,-1);
        }
        inputBar.value += oper;
        questBar.innerHTML = inputBar.value;
        inputBar.value = '';
        anserBar.innerHTML = '';
        operator = oper;
    }
};
async function loadHistory(){
    var history = await eel.py_loadHistory()();
    for(var i=0; i<=history.length; i++){
        if(history[i] != undefined){
            console.log(history[i]);
            var node = document.createElement("p");
            node.appendChild(document.createTextNode(history[i]));
            historyBar.appendChild(node);
        }
    }
}
async function clearHis(){
    await eel.py_clearHis()();
    historyBar.innerHTML = '';
}

// eel-expose functions

// Function calling on start up

sideBar.style.width="0px";
setsize();
loadtheme();