const express = require('express');
const jwt = require('jsonwebtoken')

const app = express();


app.get('/api',(req,res)=>{
    res.json({message: 'Welcome to the API'})
})

// There is a concept called middleware, which is present inside the post request, the first request goes to the middle wear, if everything is ok in the middle wear, send next(), so that it will go to the next part , then only the function gets executed

app.post('/api/posts',verifyToken,(req,res)=>{

    jwt.verify(req.token, 'secreatkey',(err,authData)=>{
        if(err){
            res.sendStatus(403);
        }else{
            res.json({message:"Post Created!!",authData})
        }

    })


})


app.post('/api/login',(req,res)=>{
    // Mock user
    const user = {
        id : 1,
        username:'brad',
        email:'brad@gmail.com'
    }
    // Set the timer as well
    jwt.sign({user},'secreatkey',{expiresIn:'30s'},(err,token)=>{
        res.json({
            token
        })

    })
})

//  Format of token
// Authorization: Bearer <access_token>



// verify Token
function verifyToken(req,res,next){

    // GET auth Header Value
    console.log("req.headers  : ",req.headers)
    const bearerHeader = req.headers['authorization'];

    // if bearer undefined
    if(typeof bearerHeader !== 'undefined'){
        const bearer = bearerHeader.split(' ');

        const bearerToken = bearer[1];

        req.token = bearerToken;

        console.log("req.token",req.token)

        next();

    }else{
        // Forbidden
        res.sendStatus(403)
    }

}


app.listen(5000,()=>{
    console.log("Server started on the port 5000")
})