const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const { GraphQLSchema } = require('graphql');
const schema = require('./schema/schema');

const app = express();

app.use(
    '/graphql',
    graphqlHTTP({
        schema: schema,
        graphiql: true
    })
);

app.listen(4000, () => {
    console.log('Now listening for requests on port 4000');
});
