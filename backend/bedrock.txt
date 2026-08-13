import express from "express";
import {
  BedrockRuntimeClient,
  ConverseCommand,
} from "@aws-sdk/client-bedrock-runtime";

const app = express();

app.use(express.json());

const bedrock = new BedrockRuntimeClient({
  region: "us-east-1",
});

app.post("/ai", async (req, res) => {
  try {
    const { prompt } = req.body;

    const command = new ConverseCommand({
      modelId: "amazon.nova-micro-v1:0",
      messages: [
        {
          role: "user",
          content: [
            {
              text: prompt,
            },
          ],
        },
      ],
    });

    const response = await bedrock.send(command);
    console.log(
      "Response from Bedrock:",
      response.output.message.content[0].text,
    );
    res.json({
      answer: response.output.message.content[0].text,
    });
  } catch (error) {
    console.error(error);

    res.status(500).json({
      error: error.message,
    });
  }
});

app.listen(3000, () => {
  console.log("Server is running on http://localhost:3000");
});
