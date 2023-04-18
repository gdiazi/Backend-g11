
import express from "express";
import cors from "cors";

const servidor = express();
const PORT = 3000;


servidor.use(cors());
servidor.use(express.json());

servidor.listen(PORT, () =>{
    console.log(`Servidor corriendp en el puerto ${PORT}`);
});
