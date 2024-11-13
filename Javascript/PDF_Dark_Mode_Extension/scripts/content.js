let cover = document.createElement("div");
let newStyle = ` 
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
`;
cover.setAttribute("style", newStyle);
cover.setAttribute("id", "darkModeOverlay");
document.body.appendChild(cover);

// Listen for messages from the background script
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "toggle") {
        const overlay = document.getElementById('darkModeOverlay');
        overlay.style.display = overlay.style.display === 'none' ? 'block' : 'none';
    }
});