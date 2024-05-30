function toggleDiv() {
    var div = document.getElementById("extend");
    if (div.style.display === "none" && window.innerWidth <= 996) {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}

function delDropdownOnResize() {
    const width = window.innerWidth;
    var div = document.getElementById("extend");

    if (width > 996 && div.style.display === "block") {
        div.style.display = "none";
    }
}


function main() {
    window.addEventListener('resize', delDropdownOnResize);
}

main();