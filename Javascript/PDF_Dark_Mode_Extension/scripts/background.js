chrome.action.onClicked.addListener((tab) => {
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    // Check if the tab exists and is a valid tab
    if (tabs[0] && tabs[0].id) {
      // Execute content script first to ensure receiver exists
      chrome.scripting.executeScript({
        target: {tabId: tabs[0].id},
        files: ['scripts/content.js']
      }).then(() => {
        // Send message after content script is injected
        chrome.tabs.sendMessage(tabs[0].id, {action: "toggle"});
      }).catch((err) => {
        console.error('Failed to inject content script:', err);
      });
    }
  });
});