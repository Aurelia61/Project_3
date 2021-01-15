// alert("It's working");
    

document.addEventListener("DOMContentLoaded", (event) => {
    let icon_moves = [["48%", "0%"], ["18%", "18%"], ["35%", "35%"], ["68%", "38%"],
    ["86%", "36%"], ["92%", "12%"], ["72%", "6%"]],
        icons = [],
        position = 0;
    for (let i = 1; i < 8; i++) {
        icons.push($("#moved-" + i));
    }

    function oneTurn() {
        for (let i = 0; i < icons.length; i++) {
            let currentElement = icons[i].attr("id").split("-")[1] - 1;
            currentElement += position;
            if (currentElement >= icon_moves.length) {
                currentElement -= icon_moves.length;
            }
            icons[i].animate({
                left: icon_moves[currentElement][0],
                marginTop: icon_moves[currentElement][1],
            }, 1500, "swing");
        }
        position++;
        if (position === icons.length) {
            position = 0;
        }
    }
    setInterval(function () {
        oneTurn();
    }, 2500)
})