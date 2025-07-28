const mongoose = require("mongoose");

const userInputSchema = new mongoose.Schema({
  product: String,
  category: String,
  quantity: Number,
  price: Number,
  rating: Number,
  delivery_time: Number,
  prediction: Number,
  createdAt: { type: Date, default: Date.now }
});

module.exports = mongoose.model("UserInput", userInputSchema);
