const express = require('express');
const app = express();
const port = 5000;

app.get('/test', (req, res) => {
    res.send("Hola, soy el servicio c,que va desde servidor c!");
});

app.listen(port, () => {
    console.log(`Servicio c corriendo en http://localhost:${port}`);
});
