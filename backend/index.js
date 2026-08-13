import express from "express";
import cookieParser from "cookie-parser";
import jwt from "jsonwebtoken";
import cors from "cors";

const app = express();
app.use(cookieParser());
app.use(cors());

app.use(express.json());

app.post("/message", (req, res) => {
  const { question } = req.body;
  setTimeout(() => {
    res.json({
      response: `hoo good qn ${question}`,
    });
  }, 2000);
});

app.listen(3000, () => {
  console.log("http://localhost:3000");
});
