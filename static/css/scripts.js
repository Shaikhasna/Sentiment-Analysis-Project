document.addEventListener("DOMContentLoaded", () => {
    const body = document.querySelector("body");

    // Function to create random objects
    function createRandomObject() {
        const div = document.createElement("div");
        div.classList.add("moving-object");
        div.style.top = `${Math.random() * 100}%`;
        div.style.left = `${Math.random() * 100}%`;
        div.style.animationDuration = `${Math.random() * 5 + 3}s`; // Random speed
        div.style.animationDelay = `${Math.random() * 3}s`; // Random delay
        body.appendChild(div);
    }

    // Create a random number of objects
    for (let i = 0; i < 5; i++) {
        createRandomObject();
    }
});
