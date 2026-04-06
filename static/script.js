document
    .getElementById("registrationForm")
    .addEventListener("submit", async function (event) {

        event.preventDefault();

        let full_name =
            document.getElementById("full_name").value;

        let event_name =
            document.getElementById("event_name").value;

        let response =
            await fetch("/register", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    full_name,
                    event_name
                })

            });

        let result = await response.json();

        document.getElementById("message").innerText =
            result.message;

    });