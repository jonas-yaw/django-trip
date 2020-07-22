let menu = document.getElementById('menu-div')
let cancel_menu = document.getElementById('cancel-menu-div')
let dropdown = document.getElementById('dropdown-content')

menu.onclick = () => {
    if (cancel_menu.style.visibility == "hidden") {
        cancel_menu.style.visibility = "visible"
        dropdown.style.display = "block"
        menu.style.visibility = "hidden"
    } else {
        cancel_menu.style.visibility = "hidden"
        dropdown.style.display = "none"
        menu.style.visibility = "visible"
    }
}