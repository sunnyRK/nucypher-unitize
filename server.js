const { createServer } = require('http');
const next = require('next');
const app = next({
    dev: process.env.NODE_ENV !== 'production'
});

const routes = require("./routes");
const handler = routes.getRequestHandler(app);

app.prepare().then(() => {
    createServer(handler).listen(3000,(err) => {
        if(err) throw err;
        console.log(`Ready on localhost 3000`);
        // `Ready on localhost ${process.env.PORT}`
    });

    // createServer(handler).listen(process.env.PORT || 3000,(err) => {
    //     if(err) throw err;
    //     console.log(`Ready on localhost ${process.env.PORT}`);
    //     // `Ready on localhost ${process.env.PORT}`
    // });
});