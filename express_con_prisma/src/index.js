import express from "express";
import * as rutas from "./routes/index.js";
import cors from "cors";


//import { categoriaRouter } from "./routes/categorias.routes.js";
//import { Prisma } from "./prisma.js";
//const Prisma = new prisma.PrismaClient();

const servidor = express();
servidor.use(express.json());

servidor.use(
    cors({
        origin: ["http://127.0.0.1:3001"],
        methods: ["GET", "POST", "PUT", "PATCH", "DELETE"],
        allowedHeaders: ["Content-Type", "Authorization"],
    })
);

const PORT = 3000;

servidor.use(rutas.categoriaRouter);
servidor.use(rutas.productoRouter);

servidor.listen(PORT, () => {
    console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`)
});

// export const eliminarCategoria = async(req, res) =>{
//     const {id} = req.params;


//     const categoriaEliminada = await Prisma.categoria.delete({
//         where: { id: +id },
//     });

//     return res.json({
//         message: "Categoria eliminada existosamente",
//         content: categoriaEliminada,
//     });
// };