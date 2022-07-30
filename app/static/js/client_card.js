function show_client(mini_client_card, full_client_card) {
    document.getElementById(full_client_card).style.display = "block";
    document.getElementById(mini_client_card).style.display = "none";
}

function hide_client(mini_client_card, full_client_card) {
    document.getElementById(full_client_card).style.display = "none";
    document.getElementById(mini_client_card).style.display = "block";
}