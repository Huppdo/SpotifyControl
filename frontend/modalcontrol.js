var modal = document.getElementById('songInput');
window.onclick = function(event) {
    if (event.target == modal) {
        closeModal()
    }
}

function closeModal(){
    modal.style.display = "none";
    document.getElementById("trackTitle").innerText = "";
    document.getElementById("trackTitle").value = "";
}

function showModal() {
    modal.style.display = "inline-block";
}
