const express = require("express");
const app = express();

app.get("/api", (req, res) => {
  res.send("Hello backend engineer, your api is working fine! ~DevHubBox");
});

const PORT = 5000;
app.listen(PORT, "0.0.0.0", () => {
  console.log(`Server running on port ${PORT}`);
});
