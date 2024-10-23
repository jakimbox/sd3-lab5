const express = require('express');
const app = express();
const port = 6000;

app.get('/test', (req, res) => {
    res.send("Hola, soy el servicio g, Desde el servidor G!");
});

app.listen(port, () => {
    console.log(`Servicio g corriendo en http://localhost:${port}`);
});
