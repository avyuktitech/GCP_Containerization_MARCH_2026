const express = require('express');
const app = express();

app.use(express.urlencoded({ extended: true }));

// Business Logic
function calculateDiscount(price) {
    if (price > 1000) {
        return price * 0.9; // 10% discount
    }
    return price;
}

// UI + Backend
app.get('/', (req, res) => {
    res.send(`
        <h2>Price Calculator</h2>
        <form method="POST" action="/calculate">
            Enter Price: <input type="text" name="price"/>
            <button type="submit">Calculate</button>
        </form>
    `);
});

app.post('/calculate', (req, res) => {
    const price = parseFloat(req.body.price);
    const finalPrice = calculateDiscount(price);

    res.send(`
        <h3>Final Price: ${finalPrice}</h3>
        <a href="/">Go Back</a>
    `);
});

// Run server
app.listen(3000, () => {
    console.log('App running on port 3000');
});
