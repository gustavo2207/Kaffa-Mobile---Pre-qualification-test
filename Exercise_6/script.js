function timer() {
  display = document.querySelector(".timer");

  fetch("http://worldclockapi.com/api/json/utc/now")
    .then((response) => response.json())
    .then((time) => {
      display.innerText = `
      {
        "currentDateTime": "${time.currentDateTime}"
      }`;
    });
}
timer();
