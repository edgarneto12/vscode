const hours = document.getElementById('hours');
const minutes = document.getElementById('minutes');
const seconds = document.getElementById('seconds');

console.log("ping");

const relogio = setInterval(function time(){
    let dateToday = new Date();
    let hr = dateToday.getHours();
    let min = dateToday.getMinutes();
    let sec = dateToday.getSeconds();

    if(hr < 10) hr = "0" + hr;
    if(min < 10) min = "0" + min;
    if(sec < 10) sec = "0" + sec;

    
    if(hr < 18){document.body.style.backgroundImage = "url('wallpaper.jpg')";
    }else{
        document.body.style.backgroundImage = "url('wallpapernight.jpg')";
    }

    hours.textContent = hr;
    minutes.textContent = min;
    seconds.textContent = sec;
})