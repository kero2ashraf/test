import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="A Little Message For You 💗",
    page_icon="💗",
    layout="centered",
    initial_sidebar_state="collapsed",
)

html = r"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width,
             initial-scale=1.0,
             maximum-scale=1.0,
             user-scalable=no"
>

<title>A Little Message For You 💗</title>

<style>

* {
    box-sizing: border-box;
}

html,
body {
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 100%;
    overflow: hidden;
}

body {
    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        Arial,
        sans-serif;

    background:
        radial-gradient(
            circle at 20% 20%,
            rgba(255,255,255,0.8),
            transparent 30%
        ),

        radial-gradient(
            circle at 80% 10%,
            rgba(255,180,220,0.6),
            transparent 30%
        ),

        linear-gradient(
            135deg,
            #ffd6e8 0%,
            #e8d8ff 50%,
            #cfe9ff 100%
        );

    min-height: 100vh;

    color: #542844;
}


/* BACKGROUND */

.glow {
    position: fixed;
    width: 300px;
    height: 300px;
    border-radius: 50%;
    filter: blur(70px);
    opacity: 0.45;
    pointer-events: none;
}

.glow-one {
    background: #ff8fbd;
    top: -100px;
    left: -100px;
}

.glow-two {
    background: #9e8cff;
    bottom: -100px;
    right: -100px;
}


/* MAIN */

.page {
    min-height: 100vh;

    display: flex;
    justify-content: center;
    align-items: center;

    padding: 20px;
}


/* CARD */

.card {
    width: min(92vw, 600px);

    padding: 40px 28px;

    text-align: center;

    border-radius: 32px;

    background:
        rgba(255,255,255,0.74);

    border:
        1px solid rgba(255,255,255,0.75);

    backdrop-filter:
        blur(20px);

    -webkit-backdrop-filter:
        blur(20px);

    box-shadow:
        0 25px 70px
        rgba(80,40,80,0.20);

    position: relative;

    z-index: 2;
}


/* HEART */

.top-heart {
    font-size: 60px;

    display: inline-block;

    animation:
        heartbeat 1.5s
        ease-in-out
        infinite;
}

@keyframes heartbeat {

    0%,
    100% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.18);
    }
}


/* TITLE */

h1 {
    margin:
        12px 0 10px;

    font-size:
        clamp(32px, 8vw, 46px);

    line-height: 1.1;

    color: #742c5b;
}


/* INTRO */

.subtitle {

    max-width: 470px;

    margin:
        0 auto 20px;

    font-size: 17px;

    line-height: 1.6;

    color: #704d66;
}


/* MESSAGE */

.message {

    margin:
        20px auto 25px;

    max-width: 510px;

    font-size:
        clamp(19px, 5vw, 27px);

    font-weight: 800;

    line-height: 1.5;

    color: #542844;
}

.message span {

    display: block;

    margin:
        7px 0;
}

.highlight {

    color: #d92c76;
}


/* BUTTON AREA */

.button-area {

    width: 100%;

    height: 145px;

    position: relative;
}


/* BUTTON */

button {

    border: none;

    border-radius: 999px;

    padding:
        15px 30px;

    font-size: 18px;

    font-weight: 800;

    cursor: pointer;

    touch-action: manipulation;

    box-shadow:
        0 10px 25px
        rgba(80,30,70,0.18);
}


/* YES */

#yes-button {

    position: absolute;

    left: 17%;

    top: 30px;

    background:
        linear-gradient(
            135deg,
            #ff4f9a,
            #ff7ab6
        );

    color: white;

    z-index: 5;

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease;
}

#yes-button:hover {

    box-shadow:
        0 15px 35px
        rgba(255,79,154,0.35);
}


/* NO */

#no-button {

    position: fixed;

    left: 55%;

    top: 65%;

    background: white;

    color: #7c5670;

    z-index: 9999;

    transition:
        left 0.15s ease,
        top 0.15s ease;
}


/* MESSAGE BELOW BUTTON */

#tease-message {

    min-height: 28px;

    margin-top: 5px;

    font-size: 14px;

    font-weight: 700;

    color: #9a4877;
}


/* NOTE */

.note {

    margin-top: 12px;

    font-size: 12px;

    color: #7c6475;

    opacity: 0.75;
}


/* SUCCESS */

#success-screen {

    display: none;

    animation:
        successAppear
        0.7s
        ease
        forwards;
}

@keyframes successAppear {

    from {

        opacity: 0;

        transform:
            scale(0.8)
            translateY(20px);
    }

    to {

        opacity: 1;

        transform:
            scale(1)
            translateY(0);
    }
}


.success-heart {

    font-size: 85px;

    display: inline-block;

    animation:
        heartbeat 1s
        ease-in-out
        infinite;
}


.success-title {

    margin:
        10px 0;

    font-size:
        clamp(38px, 9vw, 55px);

    color: #d92c76;
}


.success-text {

    max-width: 470px;

    margin:
        10px auto 20px;

    font-size: 18px;

    line-height: 1.7;

    color: #604255;
}


.signature {

    font-size: 17px;

    font-weight: 800;

    color: #8b3b69;
}


/* FLOATING HEARTS */

.floating-heart {

    position: fixed;

    bottom: -50px;

    pointer-events: none;

    z-index: 1;

    opacity: 0.7;

    animation:
        floatUp
        linear
        forwards;
}

@keyframes floatUp {

    from {

        transform:
            translateY(0)
            rotate(0deg);

        opacity: 0;
    }

    15% {
        opacity: 0.75;
    }

    to {

        transform:
            translateY(-115vh)
            rotate(360deg);

        opacity: 0;
    }
}


/* CONFETTI */

.confetti {

    position: fixed;

    top: -50px;

    z-index: 99999;

    pointer-events: none;

    animation:
        confettiFall
        3s
        linear
        forwards;
}

@keyframes confettiFall {

    to {

        transform:
            translate3d(
                var(--move-x),
                110vh,
                0
            )
            rotate(720deg);

        opacity: 0;
    }
}


/* MOBILE */

@media (max-width: 600px) {

    .card {

        padding:
            30px 18px;
    }

    h1 {

        font-size: 33px;
    }

    .subtitle {

        font-size: 15px;
    }

    .message {

        font-size: 20px;

        line-height: 1.45;
    }

    #yes-button {

        left: 9%;

        padding:
            14px 25px;
    }

    #no-button {

        left: 55%;

        top: 65%;
    }
}

</style>

</head>


<body>


<div class="glow glow-one"></div>

<div class="glow glow-two"></div>


<div class="page">

<div class="card">


<!-- QUESTION SCREEN -->

<div id="question-screen">


    <div class="top-heart">
        💗
    </div>


    <h1>

        Hey, Beautiful! 💕

    </h1>


    <div class="subtitle">

        I made this little website
        just for you.

        <br>

        Because I want you
        to smile today. 🥰

    </div>


    <!-- YOUR MESSAGE -->

    <div class="message">

        <span>
            You are my best friend. 💕
        </span>

        <span>
            I want you to be happy. 😊
        </span>

        <span>
            I will always be with you. 🤍
        </span>

        <span>
            God will bless you
            in everything. 🙏✨
        </span>

        <span class="highlight">
            And you will be a
            beautiful engineer ever! 👩‍💻💗
        </span>

    </div>


    <!-- BUTTONS -->

    <div class="button-area">

        <button id="yes-button">

            YES 💖

        </button>

    </div>


    <div id="tease-message">

        There is only one correct
        answer... 👀

    </div>


    <div class="note">

        P.S. Try clicking NO
        if you're brave. 😈

    </div>


</div>


<!-- SUCCESS SCREEN -->

<div id="success-screen">


    <div class="success-heart">

        💖

    </div>


    <div class="success-title">

        YAAAAY! 🥳

    </div>


    <div class="success-text">

        I knew you would say yes! 😂💕

        <br><br>

        You are my best friend,
        and I will always be with you. 🤍

        <br><br>

        I want you to always be happy.

        <br>

        May God bless you in everything
        and guide you toward your dreams. 🙏✨

        <br><br>

        And I know you will become
        a beautiful and amazing engineer! 👩‍💻💗

    </div>


    <div class="signature">

        — From Kero 💗

    </div>


</div>


</div>

</div>


<!-- NO BUTTON -->

<button id="no-button">

    NO 😈

</button>


<script>


const noButton =
    document.getElementById(
        "no-button"
    );

const yesButton =
    document.getElementById(
        "yes-button"
    );

const message =
    document.getElementById(
        "tease-message"
    );

const questionScreen =
    document.getElementById(
        "question-screen"
    );

const successScreen =
    document.getElementById(
        "success-screen"
    );


let attempts = 0;


const messages = [

    "Nice try 😂",

    "Nope! The button escaped! 🏃‍♀️💨",

    "You really thought you could click it? 😭",

    "The NO button is scared of you! 😌",

    "Why are you chasing NO? 🥺",

    "Just press YES alreadyyy 🥹💕",

    "NO is getting further away! 😂",

    "I can do this all day 😈",

    "Okay... YES is waiting 💗",

    "Give up and choose YES! 😂💕"

];


/* MOVE NO */

function moveNoButton() {

    attempts++;


    const buttonWidth =
        noButton.offsetWidth;

    const buttonHeight =
        noButton.offsetHeight;


    const padding = 15;


    const maxX =
        window.innerWidth
        - buttonWidth
        - padding;


    const maxY =
        window.innerHeight
        - buttonHeight
        - padding;


    const randomX =
        padding
        +
        Math.random()
        *
        Math.max(
            1,
            maxX - padding
        );


    const randomY =
        padding
        +
        Math.random()
        *
        Math.max(
            1,
            maxY - padding
        );


    noButton.style.left =
        randomX + "px";


    noButton.style.top =
        randomY + "px";


    message.textContent =
        messages[
            (attempts - 1)
            %
            messages.length
        ];


    const scale =
        Math.min(
            1.35,
            1 + attempts * 0.045
        );


    yesButton.style.transform =
        "scale(" + scale + ")";
}


/* DESKTOP */

noButton.addEventListener(
    "mouseenter",
    function() {

        moveNoButton();

    }
);


/* MOBILE */

noButton.addEventListener(
    "touchstart",
    function(event) {

        event.preventDefault();

        moveNoButton();

    },
    {
        passive: false
    }
);


/* CLICK */

noButton.addEventListener(
    "click",
    function(event) {

        event.preventDefault();

        moveNoButton();

    }
);


/* YES */

yesButton.addEventListener(
    "click",
    function() {

        questionScreen.style.display =
            "none";

        noButton.remove();

        successScreen.style.display =
            "block";

        createConfetti();

        createExtraHearts();

    }
);


/* CONFETTI */

function createConfetti() {

    const items = [

        "💗",
        "💖",
        "💕",
        "✨",
        "🌸",
        "🎀",
        "🥰",
        "💐"

    ];


    for (
        let i = 0;
        i < 100;
        i++
    ) {

        const confetti =
            document.createElement(
                "div"
            );


        confetti.className =
            "confetti";


        confetti.textContent =
            items[
                Math.floor(
                    Math.random()
                    *
                    items.length
                )
            ];


        confetti.style.left =
            Math.random()
            *
            100
            +
            "vw";


        confetti.style.fontSize =
            (
                14
                +
                Math.random()
                *
                18
            )
            +
            "px";


        confetti.style.setProperty(
            "--move-x",
            (
                Math.random()
                *
                300
                -
                150
            )
            +
            "px"
        );


        confetti.style.animationDelay =
            Math.random()
            *
            0.8
            +
            "s";


        document.body.appendChild(
            confetti
        );


        setTimeout(
            function() {

                confetti.remove();

            },
            4000
        );

    }

}


/* FLOATING HEARTS */

function createFloatingHeart() {

    const heart =
        document.createElement(
            "div"
        );


    heart.className =
        "floating-heart";


    const hearts = [

        "♡",
        "♥",
        "💗",
        "💕",
        "✨"

    ];


    heart.textContent =
        hearts[
            Math.floor(
                Math.random()
                *
                hearts.length
            )
        ];


    heart.style.left =
        Math.random()
        *
        100
        +
        "vw";


    heart.style.fontSize =
        (
            15
            +
            Math.random()
            *
            25
        )
        +
        "px";


    heart.style.animationDuration =
        (
            7
            +
            Math.random()
            *
            7
        )
        +
        "s";


    document.body.appendChild(
        heart
    );


    setTimeout(
        function() {

            heart.remove();

        },
        15000
    );

}


setInterval(
    createFloatingHeart,
    700
);


/* EXTRA HEARTS */

function createExtraHearts() {

    for (
        let i = 0;
        i < 25;
        i++
    ) {

        setTimeout(
            createFloatingHeart,
            i * 100
        );

    }

}

</script>


</body>

</html>
"""


components.html(
    html,
    height=850,
    scrolling=False
)
