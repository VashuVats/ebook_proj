const express = require('express');
const mongoose = require('mongoose');
const Connection = require('./connection.js');
const booksSchema = require('./model.js');
const dotenv = require('dotenv');

dotenv.config();

const app = express();
app.use(express.json());

const username = process.env.DB_USERNAME;
const password = process.env.DB_PASSWORD;

Connection(username, password);

const Ebooks = mongoose.model("Books", booksSchema);
app.use(bodyParser.json());

/// yaha par clien js see anae vala data ko handel karne ke liye aoo.get banayio

app.post("/api/ebooks", async (req, res) => {
    try {
        const { title, topic, audience, chapters, subsections } = req.body;

        const newText = await Ebooks.create({
            title: title,
            topic: topic,
            audience: audience,
            chapters: chapters,
            subsections: subsections
        });

        res.status(201).json(newText);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
