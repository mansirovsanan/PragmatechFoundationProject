// Modal və ya sidebar (ikisindən birini seçin) - clickleyende yeni bir card (və ya sidebar) açılsın və x vuranda baglansın (css -lə istəyinizə görə bəzəyin)

function openNav() {
    document.getElementById("mysidebar").style.width = "300px";
    document.getElementById("main").style.marginLeft = "300px";
  }

function closeNav() {
    document.getElementById("mysidebar").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
}
  