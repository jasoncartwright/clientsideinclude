document.addEventListener("DOMContentLoaded", (event) => {
    document.querySelectorAll("*[data-include]").forEach((element) => {
        const url = element.getAttribute("data-include");
        const updateInterval = element.getAttribute("data-update");
        const stopWhen = element.getAttribute("data-stop-when");
        let intervalId;
        let stopped = false;
        
        const loadContent = () => {
            fetch(url).then((response) => {
                response.text().then((text) => {
                    element.innerHTML = text;
                    if (stopWhen !== null && text.trim() === stopWhen) {
                        stopped = true;
                        if (intervalId !== undefined) {
                            clearInterval(intervalId);
                        }
                    }
                });
            });
        };
        
        // Load content initially
        loadContent();
        
        // Set up auto-update if data-update attribute is present
        if (updateInterval) {
            const intervalSeconds = parseInt(updateInterval, 10);
            if (!isNaN(intervalSeconds) && intervalSeconds > 0 && !stopped) {
                intervalId = setInterval(loadContent, intervalSeconds * 1000);
            }
        }
    });
});