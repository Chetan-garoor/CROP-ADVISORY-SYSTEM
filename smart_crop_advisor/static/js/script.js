// ----------------------------------------------------
// SCREEN SWITCHING
// ----------------------------------------------------
function showScreen(screenId) {
    document.querySelectorAll('.screen-wrapper').forEach(screen => {
        screen.classList.remove('active');
    });

    const activeScreen = document.getElementById(screenId);
    if (activeScreen) activeScreen.classList.add('active');

    document.querySelectorAll('.nav-links .nav-item').forEach(item => {
        item.classList.remove('active');
        if (item.getAttribute('data-screen') === screenId) {
            item.classList.add('active');
        }
    });

    document.querySelector('.web-content').scrollTo(0, 0);
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.nav-links .nav-item').forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const screenId = item.getAttribute('data-screen');
            showScreen(screenId);
        });
    });

    document.querySelectorAll('.fert-btn').forEach(button => {
        button.addEventListener('click', (e) => {
            document.querySelectorAll('.fert-btn').forEach(btn => btn.classList.remove('active'));
            e.target.classList.add('active');
            document.getElementById('fertilizer-type').value = e.target.getAttribute('data-value');
        });
    });

    document.querySelector('.fert-btn[data-value="Organic"]').classList.add('active');

    document.querySelector('.image-upload').addEventListener('click', () => {
        document.getElementById('disease-image-upload').click();
    });
});



// ----------------------------------------------------
// 🌾 REAL CROP RECOMMENDATION (Connected to Flask API)
// ----------------------------------------------------
async function getRecommendation() {

    const data = {
        N: parseFloat(document.getElementById('n-input').value),
        P: parseFloat(document.getElementById('p-input').value),
        K: parseFloat(document.getElementById('k-input').value),
        pH: parseFloat(document.getElementById('ph-input').value),
        temp: parseFloat(document.getElementById('temp-input').value),
        humidity: parseFloat(document.getElementById('humidity-input').value),
        rainfall: parseFloat(document.getElementById('rainfall-input').value)
    };

    console.log("📤 Sending to backend:", data);

    try {
        const response = await fetch("/api/recommend-crop", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        console.log("📥 Backend Response:", result);

        if (result.error) {
            alert("Error from backend: " + result.error);
            return;
        }

        // ⭐ Update UI with REAL prediction
        document.getElementById('recommended-crop').textContent = result.recommended_crop;
        document.getElementById('recommendation-confidence').textContent =
            `Confidence: ${result.confidence}%`;

        document.getElementById('recommendation-result').style.display = 'block';

    } catch (err) {
        console.error("❌ Frontend Error:", err);
        alert("Cannot connect to backend. Check Flask server.");
    }
}



// ----------------------------------------------------
// 📈 Yield Prediction (NOT YET LINKED TO MODEL)
// ----------------------------------------------------
async function predictYield() {
    alert("Yield Prediction model not integrated yet.");
}



// ----------------------------------------------------
// 🌿 Disease Detection (NOT YET LINKED TO MODEL)
// ----------------------------------------------------
async function detectDisease() {
    const file = document.getElementById('disease-image-upload').files[0];
    if (!file) {
        alert("Please upload an image");
        return;
    }

    alert("Disease detection model not integrated yet.");
}
