import express from "express";
import cors from "cors";
import jwt from "jsonwebtoken";

const app = express();
app.use(cors());
app.use(express.json());
const port = 3000;

function generateAccessToken() {
  const access_token = jwt.sign(
    {
      name: "demo",
    },
    "my-secret-key",
    {
      expiresIn: "1min",
    },
  );

  return access_token;
}
function generateRefreshToken() {
  const demo_refresh_token = jwt.sign(
    {
      name: "demo",
    },
    "my-secret-key",
    {
      expiresIn: "3min",
    },
  );

  return demo_refresh_token;
}
app.get("/", (req, res) => {
  res.send("wellcome");
});

app.post("/access", (req, res) => {
  const demo_acc_token = generateAccessToken();
  const demo_refresh_token = generateRefreshToken();
  res.json({
    demo_access_token: demo_acc_token,
    demo_refresh_token: demo_refresh_token,
  });
});

app.get("/verify", (req, res) => {
  try {
    const authHeader = req.headers.authorization;

    if (!authHeader) {
      return res.status(401).json({
        result: "No token provided",
      });
    }

    const token = authHeader.split(" ")[1];

    const result = jwt.verify(token, "my-secret-key");

    res.json({
      result: "success",
      user: result,
    });
  } catch (error) {
    res.status(401).json({
      result: "failed or expired",
    });
  }
});

app.listen(port, () => {
  console.log(`running http://localhost:${port}`);
});
