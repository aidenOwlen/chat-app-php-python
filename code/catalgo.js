
//Default code : ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//1) Link keyboard to stuff: Z Q D S Go azerty
document.onkeydown = function(e) {
    e = e || window.event;
    switch(e.which || e.keyCode)  {
        case 68:

	        alert("Right")
	        Right()
	        break;

        case 90: 
	        alert("UP")
	        Up();
          	break;

        case 81:
	        alert("LEFT")
	        Left();
          	break;
        case 83:
	        alert("DOWN")
	        Down();


        default: return; 
    }
    
    e.preventDefault(); 
};


//FUNCTIONS ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Those functions : <button onmousedown="Left()orUp().." onmouseup = "Release()">  

function Up() {
	var xhtml = new XMLHttpRequest;
	xhtml.onreadystatechange = function() {
		if ( this.readyState == 4 & this.status == 200){
			document.getElementById("Ur up button").style.backgroundColor = "yellow" // looks good ?
			// Change other buttons to ur default blue color 
		}
	}
	xhtml.open("GET",'https://www.pequea.net/testo.php?q=U',true)
	xhtml.send()
}

function Down() {
	var xhtml = new XMLHttpRequest;
	xhtml.onreadystatechange = function() {
		if ( this.readyState == 4 & this.status == 200){
			document.getElementById("Ur down button").style.backgroundColor = "yellow" // I guess kayji maa lzre9 wdakchi lmftouh
			//change other buttons to default color 

		}
	}
	xhtml.open("GET",'https://www.pequea.net/testo.php?q=D',true)
	xhtml.send()
}

function Right() {
	var xhtml = new XMLHttpRequest;
	xhtml.onreadystatechange = function() {
		if ( this.readyState == 4 & this.status == 200){
			document.getElementById("Ur right button").style.backgroundColor = "yellow" // blacky likes yellow
			//change other buttons to default color 

		}
	}
	xhtml.open("GET",'https://www.pequea.net/testo.php?q=R',true)
	xhtml.send()
}

function Left() {
	var xhtml = new XMLHttpRequest;
	xhtml.onreadystatechange = function() {
		if ( this.readyState == 4 & this.status == 200){
			document.getElementById("Ur left button").style.backgroundColor = "yellow" // weren't you yellow the first day ?
			//change other buttons to default color 

		}
	}
	xhtml.open("GET",'https://www.pequea.net/testo.php?q=L',true)
	xhtml.send()
}

function Release() { // Stop moving.
	var xhtml = new XMLHttpRequest;
	xhtml.onreadystatechange = function() {
		if ( this.readyState == 4 & this.status == 200){
			
			//change all buttons to default color ; no more yellow 

		}
	}
	xhtml.open("GET",'https://www.pequea.net/testo.php?q=Z',true)
	xhtml.send()
}

function RotateLeft() {
	var xhtml = new XMLHttpRequest;
	xhtml.open("GET",'https://www.pequea.net/testo.php?q=7',true)
	xhtml.send()
}

function RotateRight() {
	var xhtml = new XMLHttpRequest;
	xhtml.open("GET",'https://www.pequea.net/testo.php?q=8',true)
	xhtml.send()
}


function ledOn() {
	var xhtml = new XMLHttpRequest;
	xhtml.open("GET",'https://www.pequea.net/testo.php?q=H',true)
	xhtml.send()
}

function ledOff() {
	var xhtml = new XMLHttpRequest;
	xhtml.open("GET",'https://www.pequea.net/testo.php?q=J',true)
	xhtml.send()
}

function speak() { // Not yet made, will make php write in a msgTTS.txt , and esp read it.
	var msg = "Your msg for TTS blackytner"
	var xhtml = new XMLHttpRequest;
	xhtml.open("GET",'https://www.pequea.net/testo.php?action=speak&msg='+msg,true)
	xhtml.send()
}


