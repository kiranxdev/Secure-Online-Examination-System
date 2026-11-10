from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# =========================================================
# QUESTIONS
# =========================================================

questions = [
    {
        "q": "Which language is mainly used for web page structure?",
        "options": ["Python", "HTML", "Java", "C"],
        "answer": "B"
    },
    {
        "q": "Which keyword is used to define a function in Python?",
        "options": ["function", "define", "def", "fun"],
        "answer": "C"
    },
    {
        "q": "Which of these is a programming language?",
        "options": ["Python", "HTML", "CSS", "HTTP"],
        "answer": "A"
    },
    {
        "q": "Which symbol is used for comments in Python?",
        "options": ["//", "/*", "#", "<!--"],
        "answer": "C"
    },
    {
        "q": "Which language is developed by Sun Microsystems?",
        "options": ["Python", "Java", "C", "PHP"],
        "answer": "B"
    },
    {
        "q": "Which data type stores True or False?",
        "options": ["String", "Integer", "Boolean", "Float"],
        "answer": "C"
    },
    {
        "q": "Which of these is an operating system?",
        "options": ["Windows", "Python", "HTML", "MySQL"],
        "answer": "A"
    },
    {
        "q": "Which language is used for styling web pages?",
        "options": ["Java", "Python", "C", "CSS"],
        "answer": "D"
    },
    {
        "q": "Which database language is used to retrieve data?",
        "options": ["HTML", "SQL", "CSS", "XML"],
        "answer": "B"
    },
    {
        "q": "Which keyword is used to create a class in Python?",
        "options": ["object", "class", "define", "struct"],
        "answer": "B"
    }
]


# =========================================================
# LOGIN PAGE
# =========================================================

LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Secure Online Examination</title>

<style>
body {
    font-family: Arial;
    background: #eef2f7;
    text-align: center;
    padding-top: 80px;
}

.box {
    background: white;
    width: 350px;
    margin: auto;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.15);
}

input {
    width: 90%;
    padding: 12px;
    margin: 10px;
    border-radius: 8px;
    border: 1px solid #aaa;
    box-sizing: border-box;
}

button {
    padding: 12px 30px;
    background: #1976d2;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
}

.error {
    color: red;
}
</style>
</head>

<body>

<div class="box">

<h2>🔐 Secure Online Examination</h2>

<form method="POST">

<input
    type="text"
    name="username"
    placeholder="Username"
    required
>

<input
    type="password"
    name="password"
    placeholder="Password"
    required
>

<button type="submit">Login</button>

</form>

{% if error %}
<p class="error">{{ error }}</p>
{% endif %}

</div>

</body>
</html>
"""


# =========================================================
# DASHBOARD
# =========================================================

DASHBOARD = """
<!DOCTYPE html>
<html>
<head>

<title>Dashboard</title>

<style>
body {
    font-family: Arial;
    background: #eef2f7;
    text-align: center;
    padding-top: 70px;
}

.box {
    background: white;
    width: 450px;
    margin: auto;
    padding: 35px;
    border-radius: 15px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.15);
}

button {
    padding: 14px 35px;
    background: #1976d2;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 16px;
}
</style>

</head>

<body>

<div class="box">

<h1>📝 Secure Online Examination</h1>

<h3>Subject: CSE</h3>

<p>📚 Questions: 10</p>
<p>🎯 Marks: 10</p>
<p>⏱️ Time: 10 Minutes</p>

<br>

<a href="/exam">
<button>Start Exam</button>
</a>

</div>

</body>
</html>
"""


# =========================================================
# EXAM PAGE
# =========================================================

EXAM_PAGE = """
<!DOCTYPE html>
<html>

<head>

<title>Secure Online Examination</title>

<style>

body {
    font-family: Arial, sans-serif;
    background: #f1f3f6;
    margin: 0;
    padding: 20px;
}

.header {
    background: #1976d2;
    color: white;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    position: sticky;
    top: 0;
    z-index: 100;
}

#timer {
    font-size: 25px;
    font-weight: bold;
}

#warningBox {
    background: #fff3cd;
    color: #856404;
    border: 2px solid #ffc107;
    padding: 15px;
    margin: 15px auto;
    max-width: 700px;
    border-radius: 10px;
    text-align: center;
    font-weight: bold;
}

#cameraBox {
    position: fixed;
    right: 15px;
    bottom: 15px;
    background: #111;
    padding: 8px;
    border-radius: 12px;
    z-index: 200;
    width: 300px;
}

#cameraCanvas {
    width: 300px;
    height: 225px;
    border-radius: 8px;
    display: block;
    background: black;
}

#cameraStatus {
    color: white;
    text-align: center;
    font-size: 13px;
    padding: 7px;
    font-weight: bold;
}

#aiInfo {
    color: #00ff66;
    background: #000;
    text-align: center;
    font-size: 11px;
    padding: 6px;
    min-height: 16px;
}

.question {
    background: white;
    padding: 20px;
    margin: 20px auto;
    max-width: 800px;
    border-radius: 12px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.1);
}

.option {
    margin: 12px 0;
}

.submitBtn {
    display: block;
    margin: 30px auto;
    padding: 15px 40px;
    background: #198754;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 18px;
}

</style>

</head>

<body>

<div class="header">

<h2>🔐 Secure Online Examination</h2>

<div>
⏱️ Time Remaining:
<span id="timer">10:00</span>
</div>

</div>


<div id="warningBox">

⚠️ Security Monitoring Active

<br><br>

Warnings:
<span id="warningCount">0</span>/3

</div>


<!-- ============================================= -->
<!-- CAMERA -->
<!-- ============================================= -->

<div id="cameraBox">

<canvas
    id="cameraCanvas"
    width="640"
    height="480">
</canvas>

<div id="cameraStatus">
🟡 Starting Camera...
</div>

<div id="aiInfo">
AI: Starting...
</div>

</div>


<!-- Hidden video used by AI -->

<video
    id="cameraVideo"
    autoplay
    muted
    playsinline
    style="display:none;">
</video>


<form
    id="examForm"
    method="POST"
    action="/submit"
>


{% for item in questions %}

{% set qnum = loop.index %}

<div class="question">

<h3>
{{ qnum }}. {{ item.q }}
</h3>

{% for option in item.options %}

<div class="option">

<label>

<input
    type="radio"
    name="q{{ qnum }}"
    value="{{ ['A','B','C','D'][loop.index0] }}"
>

{{ ['A','B','C','D'][loop.index0] }}.
{{ option }}

</label>

</div>

{% endfor %}

</div>

{% endfor %}


<button
    class="submitBtn"
    type="submit">
Submit Exam
</button>

</form>


<!-- ================================================= -->
<!-- AI LIBRARIES -->
<!-- ================================================= -->

<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@4.20.0/dist/tf.min.js"></script>

<script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/coco-ssd"></script>


<script>

// =====================================================
// VARIABLES
// =====================================================

let warningCount = 0;

const MAX_WARNINGS = 3;

let examFinished = false;

let lastWarningTime = 0;

const WARNING_COOLDOWN = 4000;

let model = null;

let aiReady = false;

let phoneDetected = false;

let personMissing = false;

let multiplePersonWarning = false;


// =====================================================
// ELEMENTS
// =====================================================

const video =
    document.getElementById("cameraVideo");

const canvas =
    document.getElementById("cameraCanvas");

const ctx =
    canvas.getContext("2d");

const cameraStatus =
    document.getElementById("cameraStatus");

const aiInfo =
    document.getElementById("aiInfo");

const warningBox =
    document.getElementById("warningBox");

const warningCountText =
    document.getElementById("warningCount");


// =====================================================
// WARNING SOUND
// =====================================================

function warningSound() {

    try {

        const AudioContext =
            window.AudioContext ||
            window.webkitAudioContext;

        const audioContext =
            new AudioContext();

        const oscillator =
            audioContext.createOscillator();

        const gain =
            audioContext.createGain();

        oscillator.connect(gain);

        gain.connect(
            audioContext.destination
        );

        oscillator.frequency.value = 900;

        gain.gain.value = 0.3;

        oscillator.start();

        setTimeout(function() {

            oscillator.stop();

        }, 500);

    }

    catch(error) {

        console.log(error);

    }
}


// =====================================================
// WARNING FUNCTION
// =====================================================

function giveWarning(message) {

    if (examFinished) {
        return;
    }

    const now = Date.now();

    if (
        now - lastWarningTime <
        WARNING_COOLDOWN
    ) {
        return;
    }

    lastWarningTime = now;

    warningCount++;

    warningCountText.innerText =
        warningCount;

    warningBox.innerHTML =
        "⚠️ WARNING " +
        warningCount +
        "/" +
        MAX_WARNINGS +
        "<br><br>" +
        message;

    warningSound();


    if (
        warningCount >= MAX_WARNINGS
    ) {

        examFinished = true;

        alert(
            "❌ EXAM TERMINATED\\n\\n" +
            "3 security warnings detected."
        );

        document
            .getElementById("examForm")
            .submit();
    }
}


// =====================================================
// CAMERA
// =====================================================

async function startCamera() {

    try {

        if (
            !navigator.mediaDevices ||
            !navigator.mediaDevices.getUserMedia
        ) {

            cameraStatus.innerText =
                "🔴 Camera not supported";

            giveWarning(
                "📷 Camera is not supported."
            );

            return;
        }


        cameraStatus.innerText =
            "🟡 Requesting camera...";


        const stream =
            await navigator.mediaDevices.getUserMedia({

                video: {
                    width: {
                        ideal: 640
                    },
                    height: {
                        ideal: 480
                    },
                    facingMode: "user"
                },

                audio: false

            });


        video.srcObject = stream;


        await video.play();


        cameraStatus.innerText =
            "🟢 Camera ON";


        aiInfo.innerText =
            "AI: Loading mobile detector...";


        startAI();

    }

    catch(error) {

        console.error(
            "Camera Error:",
            error
        );

        cameraStatus.innerText =
            "🔴 Camera OFF";

        aiInfo.innerText =
            "AI: Camera unavailable";

        giveWarning(
            "📷 Camera access is required."
        );

    }
}


startCamera();


// =====================================================
// AI MODEL
// =====================================================

async function startAI() {

    try {

        aiInfo.innerText =
            "AI: Starting TensorFlow...";


        await tf.ready();


        console.log(
            "TensorFlow ready"
        );


        aiInfo.innerText =
            "AI: Loading COCO-SSD mobile detector...";


        model =
            await cocoSsd.load();


        aiReady = true;


        cameraStatus.innerText =
            "🟢 CAMERA + AI ON";


        aiInfo.innerText =
            "AI: READY - Mobile monitoring ON";


        console.log(
            "AI MODEL LOADED"
        );


        detectObjects();

    }

    catch(error) {

        console.error(
            "AI MODEL ERROR:",
            error
        );


        aiReady = false;


        cameraStatus.innerText =
            "🔴 AI FAILED";


        aiInfo.innerText =
            "AI: FAILED - Check Internet";


        alert(
            "AI model failed to load.\\n\\n" +
            "Please check Internet and refresh the exam."
        );

    }
}


// =====================================================
// BOX DRAWING
// =====================================================

function drawPrediction(
    prediction
) {

    const box =
        prediction.bbox;

    const x = box[0];

    const y = box[1];

    const width = box[2];

    const height = box[3];


    ctx.lineWidth = 4;

    ctx.strokeStyle =
        prediction.class === "cell phone"
        ? "#ff0000"
        : "#00ff00";

    ctx.strokeRect(
        x,
        y,
        width,
        height
    );


    ctx.font =
        "bold 18px Arial";

    ctx.fillStyle =
        prediction.class === "cell phone"
        ? "#ff0000"
        : "#00ff00";


    const percentage =
        Math.round(
            prediction.score * 100
        );


    ctx.fillText(

        prediction.class +
        " " +
        percentage +
        "%",

        x,
        Math.max(
            20,
            y - 5
        )

    );
}


// =====================================================
// PHONE INSIDE PERSON CHECK
// =====================================================

function phoneInsidePerson(
    phone,
    person
) {

    const px =
        phone.bbox[0];

    const py =
        phone.bbox[1];

    const pw =
        phone.bbox[2];

    const ph =
        phone.bbox[3];


    const personX =
        person.bbox[0];

    const personY =
        person.bbox[1];

    const personW =
        person.bbox[2];

    const personH =
        person.bbox[3];


    const phoneCenterX =
        px + pw / 2;

    const phoneCenterY =
        py + ph / 2;


    return (

        phoneCenterX >= personX &&

        phoneCenterX <=
            personX + personW &&

        phoneCenterY >= personY &&

        phoneCenterY <=
            personY + personH

    );
}


// =====================================================
// AI OBJECT DETECTION
// =====================================================

async function detectObjects() {

    if (examFinished) {
        return;
    }


    if (
        !aiReady ||
        !model
    ) {

        setTimeout(
            detectObjects,
            1000
        );

        return;
    }


    if (
        video.readyState < 2
    ) {

        setTimeout(
            detectObjects,
            1000
        );

        return;
    }


    try {

        // =============================================
        // RUN AI
        // =============================================

        const predictions =
            await model.detect(
                video,
                20
            );


        // =============================================
        // DRAW CAMERA
        // =============================================

        ctx.clearRect(
            0,
            0,
            canvas.width,
            canvas.height
        );


        ctx.drawImage(
            video,
            0,
            0,
            canvas.width,
            canvas.height
        );


        // =============================================
        // DRAW ALL AI BOXES
        // =============================================

        predictions.forEach(
            function(item) {

                if (
                    item.score >= 0.10
                ) {

                    drawPrediction(
                        item
                    );

                }

            }
        );


        // =============================================
        // MOBILE DETECTION
        // =============================================

        const phones =
            predictions.filter(
                function(item) {

                    return (

                        item.class ===
                        "cell phone"

                        &&

                        item.score >=
                        0.10

                    );

                }
            );


        // =============================================
        // PERSON DETECTION
        // =============================================

        const persons =
            predictions.filter(
                function(item) {

                    return (

                        item.class ===
                        "person"

                        &&

                        item.score >=
                        0.30

                    );

                }
            );


        // =============================================
        // AI STATUS
        // =============================================

        if (
            predictions.length === 0
        ) {

            aiInfo.innerText =
                "AI: READY - No object detected";

        }

        else {

            const names =
                predictions
                .filter(
                    function(item) {

                        return (
                            item.score >= 0.10
                        );

                    }
                )
                .map(
                    function(item) {

                        return (

                            item.class +
                            " " +
                            Math.round(
                                item.score * 100
                            ) +
                            "%"

                        );

                    }
                )
                .join(" | ");


            aiInfo.innerText =
                "AI: " + names;

        }


        // =============================================
        // 📱 PHONE WARNING
        // =============================================

        if (
            phones.length > 0
        ) {

            let phoneInHand =
                false;


            // Check if phone is inside person box

            for (
                let i = 0;
                i < phones.length;
                i++
            ) {

                for (
                    let j = 0;
                    j < persons.length;
                    j++
                ) {

                    if (
                        phoneInsidePerson(
                            phones[i],
                            persons[j]
                        )
                    ) {

                        phoneInHand =
                            true;

                    }

                }

            }


            if (
                phoneInHand
            ) {

                aiInfo.innerText =
                    "🚨 AI: PHONE IN PERSON AREA";


                if (
                    !phoneDetected
                ) {

                    phoneDetected = true;


                    giveWarning(

                        "📱 MOBILE PHONE DETECTED!<br><br>" +

                        "Phone detected near the person. " +

                        "Please keep the mobile phone away."

                    );

                }

            }

            else {

                // Even if not inside person,
                // a clearly visible phone is still suspicious.

                if (
                    !phoneDetected
                ) {

                    phoneDetected = true;


                    giveWarning(

                        "📱 MOBILE PHONE DETECTED!<br><br>" +

                        "Please keep the mobile phone away."

                    );

                }

            }

        }

        else {

            phoneDetected =
                false;

        }


        // =============================================
        // 👤 PERSON MISSING
        // =============================================

        if (
            persons.length === 0
        ) {

            if (
                !personMissing
            ) {

                personMissing =
                    true;


                giveWarning(

                    "👤 PERSON NOT DETECTED!<br><br>" +

                    "Please stay in front of the camera."

                );

            }

        }

        else {

            personMissing =
                false;

        }


        // =============================================
        // 👥 MULTIPLE PERSON
        // =============================================

        if (
            persons.length > 1
        ) {

            if (
                !multiplePersonWarning
            ) {

                multiplePersonWarning =
                    true;


                giveWarning(

                    "👥 MULTIPLE PERSONS DETECTED!<br><br>" +

                    "Only one person is allowed."

                );

            }

        }

        else {

            multiplePersonWarning =
                false;

        }

    }

    catch(error) {

        console.error(
            "AI Detection Error:",
            error
        );


        aiInfo.innerText =
            "AI: Detection error";

    }


    // Run again

    setTimeout(
        detectObjects,
        700
    );
}


// =====================================================
// CAMERA OFF DETECTION
// =====================================================

setInterval(
    function() {

        if (
            examFinished
        ) {
            return;
        }


        if (
            !video.srcObject
        ) {

            giveWarning(
                "📷 Camera is not available."
            );

            return;
        }


        const tracks =
            video.srcObject
                .getVideoTracks();


        if (
            tracks.length === 0||
            tracks[0].readyState !== "live"
        ) {

            giveWarning(
                "📷 Camera was turned OFF."
            );

        }

    },
    4000
);


// =====================================================
// TAB SWITCH
// =====================================================

document.addEventListener(
    "visibilitychange",
    function() {

        if (
            examFinished
        ) {
            return;
        }


        if (
            document.hidden
        ) {

            giveWarning(
                "🔄 You switched to another tab."
            );

        }

    }
);


// =====================================================
// WINDOW FOCUS
// =====================================================

window.addEventListener(
    "blur",
    function() {

        if (
            examFinished
        ) {
            return;
        }


        if (
            !document.hidden
        ) {

            giveWarning(
                "🪟 Exam window lost focus."
            );

        }

    }
);


// =====================================================
// BACK BUTTON
// =====================================================

history.pushState(
    null,
    "",
    location.href
);


window.onpopstate =
function() {

    history.pushState(
        null,
        "",
        location.href
    );


    giveWarning(
        "◀️ Back navigation detected."
    );

};


// =====================================================
// TIMER
// =====================================================

let timeLeft = 600;


const timer =
    document.getElementById(
        "timer"
    );


const countdown =
    setInterval(
        function() {

            if (
                examFinished
            ) {

                clearInterval(
                    countdown
                );

                return;
            }


            const minutes =
                Math.floor(
                    timeLeft / 60
                );


            const seconds =
                timeLeft % 60;


            timer.innerText =

                String(minutes)
                    .padStart(2, "0")

                +

                ":" +

                String(seconds)
                    .padStart(2, "0");


            if (
                timeLeft <= 0
            ) {

                clearInterval(
                    countdown
                );


                examFinished =
                    true;


                alert(
                    "⏰ Time is over!"
                );


                document
                    .getElementById(
                        "examForm"
                    )
                    .submit();


                return;
            }


            timeLeft--;

        },
        1000
    );


// =====================================================
// PAGE EXIT WARNING
// =====================================================

window.addEventListener(
    "beforeunload",
    function(event) {

        if (
            !examFinished
        ) {

            event.preventDefault();

            event.returnValue = "";

        }

    }
);

</script>

</body>
</html>
"""


# =========================================================
# RESULT PAGE
# =========================================================

RESULT_PAGE = """
<!DOCTYPE html>
<html>

<head>

<title>Exam Result</title>

<style>

body {
    font-family: Arial;
    background: #eef2f7;
    text-align: center;
    padding-top: 80px;
}

.box {
    background: white;
    width: 400px;
    margin: auto;
    padding: 35px;
    border-radius: 15px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.15);
}

button {
    padding: 12px 30px;
    background: #1976d2;
    color: white;
    border: none;
    border-radius: 8px;
}

</style>

</head>

<body>

<div class="box">

<h1>📊 Exam Result</h1>

<h2>Score: {{ score }}/10</h2>

<p>✅ Correct: {{ score }}</p>

<p>❌ Wrong: {{ wrong }}</p>

<p>⚪ Unanswered: {{ unanswered }}</p>

<br>

<a href="/logout">
<button>Logout</button>
</a>

</div>

</body>

</html>
"""


# =========================================================
# ROUTES
# =========================================================

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get(
            "username"
        )

        password = request.form.get(
            "password"
        )


        if (
            username == "student"
            and password == "1234"
        ):

            return redirect(
                "/dashboard"
            )


        return render_template_string(
            LOGIN_PAGE,
            error="❌ Invalid username or password"
        )


    return render_template_string(
        LOGIN_PAGE
    )


@app.route("/dashboard")
def dashboard():

    return render_template_string(
        DASHBOARD
    )


@app.route("/exam")
def exam():

    return render_template_string(
        EXAM_PAGE,
        questions=questions
    )


@app.route(
    "/submit",
    methods=["POST"]
)
def submit():

    score = 0

    unanswered = 0


    for i, item in enumerate(
        questions,
        start=1
    ):

        user_answer = request.form.get(
            f"q{i}"
        )


        if not user_answer:

            unanswered += 1

        elif (
            user_answer ==
            item["answer"]
        ):

            score += 1


    wrong = (
        len(questions)
        - score
        - unanswered
    )


    return render_template_string(
        RESULT_PAGE,
        score=score,
        wrong=wrong,
        unanswered=unanswered
    )


@app.route("/logout")
def logout():

    return redirect("/")


# =========================================================
# START SERVER
# =========================================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5050,
        debug=True
    )