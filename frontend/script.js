const ticketForm = document.getElementById("ticketForm");

ticketForm.addEventListener("submit", async function (event) {
  event.preventDefault();

  const query = document.getElementById("ticketInput").value;

  const response = await fetch("http://127.0.0.1:5000/analyse", {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({
      ticket: query,
    }),
  });

  const result = await response.json();
  console.log(result);
});
