//Tick Tac Toe Game

//Accessing dialog boxes
const gameBox = document.querySelector(".game")
const startup = document.querySelector(".startup");

//Accessing all 9 buttons in the game
const r1c1 = document.getElementById("r1c1");
const r1c2 = document.getElementById("r1c2");
const r1c3 = document.getElementById("r1c3");
const r2c1 = document.getElementById("r2c1");
const r2c2 = document.getElementById("r2c2");
const r2c3 = document.getElementById("r2c3");
const r3c1 = document.getElementById("r3c1");
const r3c2 = document.getElementById("r3c2");
const r3c3 = document.getElementById("r3c3");

function setsize(){
    var x = 445;
    var y = 500;
    if(window.innerWidth != x || window.innerHeight != y){
        window.resizeTo(x,y);
        var Width = x - innerWidth;
        var Height = y - innerHeight;
        window.resizeTo(x + Width, y + Height);
    };
};

function ShowGame(){    // Hidding menu and showing game page
    startup.style.display = "none";
    gameBox.style.display = "block";
};
function Reset(){       // Hidding game and showing menu page and reseting all.
    gameBox.style.display = "none";
    startup.style.display = "block";
    eel.PyReset();
};
function game_p1(){
    ShowGame();
    eel.PyStartGame(1);
};
function game_p2(){
    ShowGame();
    eel.PyStartGame(2);
};

eel.expose(updateGrid)
function updateGrid(outList){
    console.log(outList);

    r1c1.className=outList[0];
    r1c2.className=outList[1];
    r1c3.className=outList[2];
    r2c1.className=outList[3];
    r2c2.className=outList[4];
    r2c3.className=outList[5];
    r3c1.className=outList[6];
    r3c2.className=outList[7];
    r3c3.className=outList[8];
};

async function move(x,y){ 
    await eel.PyMove(x,y)()
        turn = 2
};

eel.expose(js_alert)
function js_alert(msg){
    alert(msg);
};

eel.expose(js_rslt)
function js_rslt(Case,whose){
    var who;
    if(whose == "o"){who = "one"}
    else{who="two"};
    Case = Number(Case);
    if(Case == 1){r1c1.className="res "+who;r1c2.className="res "+who;r1c3.className="res "+who;}
    else if(Case==2){r2c1.className="res "+who;r2c2.className="res "+who;r2c3.className="res "+who;}
    else if(Case==3){r3c1.className="res "+who;r3c2.className="res "+who;r3c3.className="res "+who;}
    else if(Case==4){r1c1.className="res "+who;r2c1.className="res "+who;r3c1.className="res "+who;}
    else if(Case==5){r1c2.className="res "+who;r2c2.className="res "+who;r3c2.className="res "+who;}
    else if(Case==6){r1c3.className="res "+who;r2c3.className="res "+who;r3c3.className="res "+who;}
    else if(Case==7){r1c1.className="res "+who;r2c2.className="res "+who;r3c3.className="res "+who;}
    else{r1c3.className="res "+who;r2c2.className="res "+who;r3c1.className="res "+who;}
};