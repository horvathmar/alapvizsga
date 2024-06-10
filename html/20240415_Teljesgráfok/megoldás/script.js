function dont() {
    console.log("teszt");

    let volt = false;
    document.getElementsByName("valasz").forEach(element => {
        if (element.checked == true) volt = true;
    });

    if (!volt)
    {
        document.getElementById("eredmeny").innerText = "Hiányos válasz!";
    }
    else if (document.getElementById("helyes").checked)
    {
        document.getElementById("eredmeny").innerText = "Jó válasz!";
    }
    else {
        document.getElementById("eredmeny").innerText = "Rossz válasz!";
    }
    
    
}

document.getElementById("gomb").addEventListener("click", dont);