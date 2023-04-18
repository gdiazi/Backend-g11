import { channel } from "diagnostics_channel";
import express, { json } from "express";

const servidor = express();


servidor.use(express.json());

const productos = [
    {
        nombre: 'Martillo',
        precio: 7.50,
        disponible: true,
    },
    {
        nombre: "Cincel",
        precio: 18.0,
        disponible: true,
    },
    {
        nombre: "Cinta aislante",
        precio: 3.8,
        disponible: false
    }
]

const PORT = 3000;


servidor
    .route("/productos")
    .get((req, res) => {
        res.status(200).json({
            content: productos,
        })
    })


    .post((req, res) => {
        console.log(req.body);

        // if (JSON.stringify(req.body) === "{}"){

        if (Object.keys(req.body).length === 0) {

            res.status(400).json({
                message: "Información incorrecta",

            });

        }

        productos.push(req.body)


        res.status(201).json({
            message: "Producto agregado exitosamente",
            content: req.body,
        })
    })


servidor.route('/producto/:id')

    .get((req, res) => {
        const { id } = req.params;

        const resultado = productos[id];


        if (resultado) {
            res.status(200).json({
                content: resultado,
            });

        } else {
            res.status(404).json({
                message: "El producto no existe",
            })
        }

        // const id = req.params.id; 


    })

    .put((req, res) => {
        const { id } = req.params;
        const body = req.body;

        const resultado = productos[id];

        if (!resultado) {
            res.status(404).json({
                content: "El producto no existe",
            })

        }

        productos[id] = body;

        res.status(201).json({
            message: "Producto actualizado exitosamente",
            content: productos[id],

        });


    })


    .patch((req, res) => {
        
        const id = Number(req.params.id);
        const { nombre } = req.body;

        // Buscamos el producto por su ID en el arreglo de productos
        const resultado = productos.find(p => p.id === id);

        // Si el producto no existe, retornamos un mensaje de error con un código de estado 404
        if (!resultado) {
            return res.status(404).json({ error: 'Producto no encontrado' });
        }

        // Actualizamos el nombre del producto
        productos.nombre = nombre;

        // Retornamos un mensaje de éxito con el producto actualizado y un código de estado 200
        res.json({ mensaje: 'Nombre del producto actualizado correctamente', resultado });

        //hacer la actializacion parcial por ejemplo solo quiero cambiar el nombre o si solo quiero cambiar el nombre o precio
    })


    .delete((req, res) => {
        const { id } = req.params;
        const resultado = productos[id];

        if (!resultado) {
            res.status(404).json({
                content: "El producto no existe",
            })
        }

        productos.splice(id, 1);

        res.status(200).json({
            message: "Producto eliminado exisoasamente",
        });


    });


servidor.route('/buscar-productos').get((req, res) => {
    console.log(req.query)

    let resultado = [];

    if (req.query.nombre) {
        resultado = [
            ...resultado,
            ...productos.filter((producto) => {

                return producto.nombre == req.query.nombre;
            }),
        ];
    }


    if (req.query.patron) {
        resultado = [
            ...resultado,
            ...productos.filter((producto) => {
                return new RegExp(`(${req.query.patron})\w*`).exec(producto.nombre);
            }),
        ];
    }

    if (req.query.disponible) {
        resultado = [
            ...resultado,
            ...productos.filter((producto) => {
                return String(producto.disponible) === req.query.disponible;
            }),
        ];
    }

    res.status(200).json({
        content: resultado,
    })
});

servidor.listen(PORT, () => {
    console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
})