const express = require("express");
const ejs = require("ejs");
const path = require("path");

const app = express();

app.use(express.json());

app.set("view engine", "ejs");

app.use(express.static(path.join(__dirname, "/public")));

const PORT = process.env.PORT || 3000;

app.get("/", (req, res, next) => {
  res.render("index");
});

app.get("/search", (req, res, next) => {
  const query = req.query;

  const question = query.question;

  //TF - IDF algo

  //list of top 5 results

  setTimeout(() => {
    const array = [
      {
        title: "storj coin",
        url: "http://storj.io",
        description: "lorem ipsum dolor sit amet",
      },
      {
        title: "storj coin",
        url: "http://storj.io",
        description: "lorem ipsum dolor sit amet",
      },
      {
        title: "storj coin",
        url: "http://storj.io",
        description: "lorem ipsum dolor sit amet",
      },
      {
        title: "storj coin",
        url: "http://storj.io",
        description: "lorem ipsum dolor sit amet",
      },
      {
        title: "storj coin",
        url: "http://storj.io",
        description: "lorem ipsum dolor sit amet",
      },
    ];
    res.json(array);
  }, 1000);
});

app.listen(PORT, () => {
  console.log("Server is running on port " + PORT);
});
