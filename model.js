const mongoose = require('mongoose');

const booksSchema = new mongoose.Schema({
    title: {
        type: String,
        required: true
    },
    topic: {
        type: String,
        required: true
    },
    audience: {
        type: String,
        required: true
    },
    chapters: {
        type: Number,
        required: true
    },
    subsections: {
        type: Number,
        required: true
    }
});

module.exports = booksSchema;
