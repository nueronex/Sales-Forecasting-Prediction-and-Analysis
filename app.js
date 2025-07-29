const express = require("express");
const bodyParser = require("body-parser");
const { spawn } = require("child_process");
const connectDB = require("./db");
const UserInput = require("./UserInput");

const app = express();
const PORT = 8080;

connectDB();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));
app.set("view engine", "ejs");

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

app.post("/predict", (req, res) => {
  const { product, category, quantity, price, rating, delivery_time } = req.body;

  const py = spawn("python", ["predict.py"]);
  const input = {
    quantity,
    price,
    rating,
    delivery_time,
  };

  py.stdin.write(JSON.stringify(input));
  py.stdin.end();

  let result = "";
  py.stdout.on("data", (data) => {
    result += data.toString();
  });

  py.stderr.on("data", (data) => {
    console.error("stderr:", data.toString());
  });

  py.on("close", async (code) => {
    if (code === 0) {
      try {
        // Save to MongoDB
        await UserInput.create({
          product,
          category,
          quantity,
          price,
          rating,
          delivery_time,
          prediction: parseFloat(result),
        });

          await newInput.save();

        res.send(<h1>Predicted Revenue: ₹${result}</h1><a href="/">Go Back</a>);
      } catch (err) {
        console.error("MongoDB save error:", err);
        res.send("Failed to save to DB");
      }
    } else {
      res.send("Prediction failed");
    }
  });
});

app.listen(PORT, () => {
  console.log(Server started on http://localhost:${PORT});
});
