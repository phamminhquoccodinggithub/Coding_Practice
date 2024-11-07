var cover = document.createElement("div"); 
let css = ` 
    position: fixed; 
    pointer-events: none; 
    top: 0; 
    left: 0; 
    width: 100vw; 
    height: 100vh; 
    background-color: white;
    mix-blend-mode: exclusion;
    z-index: 1; 
    display: none;
` 
cover.setAttribute("style", css); 
cover.setAttribute("id", "darkModeOverlay");
document.body.appendChild(cover);

// Listen for messages from the background script
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "toggle") {
        const overlay = document.getElementById('darkModeOverlay');
        if (overlay.style.display === 'none') {
            overlay.style.display = 'block';
        } else {
            overlay.style.display = 'none';
        }
    }
});