function timer() {
  timezoneUtc = document.querySelector(".zone-utc");
  currentDateTimeUtc = document.querySelector(".date-utc");
  timezoneLocal = document.querySelector(".zone-local");
  currentDateTimeLocal = document.querySelector(".date-local");

  fetch("http://worldclockapi.com/api/json/utc/now")
    .then((response) => response.json())
    .then((time) => {
      timezoneUtc.innerText = `${time.timeZoneName}`;
      currentDateTimeUtc.innerText = `${time.currentDateTime}`
        .replace("T", " ")
        .replace("Z", ".");
    });

  fetch("http://worldclockapi.com/api/json/est/now")
    .then((response) => response.json())
    .then((time) => {
      timezoneLocal.innerText = `${time.timeZoneName}`;
      currentDateTimeLocal.innerText = `${time.currentDateTime}`
        .replace("T", " ")
        .replace("Z", ".")
        .replace("-04:00", "");
    });
}
setInterval(timer(), 1000);
