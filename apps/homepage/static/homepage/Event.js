function myFunction() {
  document.getElementById("myDIV").style.display = "block";
  setTimeout(doThis, 3000);

}

function doThis() {
  window.open("/AboutMe", "_self", "");
  document.getElementById("myDIV").style.display = "none";
}