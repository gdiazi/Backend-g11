import express from "express";

const servidor = express();


servidor.get('/saludar',(req,res) => {
    console.log("entraron a mi API!!");
    res.json({
        message: "Hola bienvenido a mi API",
    });
} );


servidor.get("/saludar/:nombre",(req, res)=>{
    console.log(req.params);

    const {nombre} = req.params;
    res.json({
        message: `Hola ${nombre}`,
    })
})

servidor.listen(3000, ()=> {
    console.log('Servidor corriendo en el puerto 3000');
});