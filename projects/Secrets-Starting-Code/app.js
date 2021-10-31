require('dotenv').config();

const DB_HOST=process.env.DB_HOST;
const DB_PORT=process.env.DB_PORT;
const DB_NAME=process.env.DB_NAME;
const PORT=process.env.PORT; 

const GOOGLE_CLIENT_ID=process.env.GOOGLE_CLIENT_ID;
const GOOGLE_CLIENT_SECRET=process.env.GOOGLE_CLIENT_SECRET; 

const express = require( "express");
const ejs = require( "ejs");
const mongoose = require( "mongoose");
const app = express();
const session = require("express-session");
const passport = require("passport");
const GoogleStrategy = require('passport-google-oauth20').Strategy;
const findOrCreate = require('mongoose-findorcreate');

// const passportLocalMongoose = require("passport-local-mongoose");

const User=require("./models/user");

app.set("view engine", "ejs");

app.use(express.urlencoded({extended:true}));
app.use(express.static(__dirname + "/public"));

app.use(session({
    secret: 'dead always fed',
    resave: false,
    saveUninitialized: true,
}));
mongoose.connect(`mongodb://${DB_HOST}:${DB_PORT}/${DB_NAME}`,{useNewUrlParser:true});
app.use(passport.initialize());
app.use(passport.session());
passport.use(User.createStrategy());
// passport.serializeUser(User.serializeUser());
// passport.deserializeUser(User.deserializeUser());

passport.serializeUser(function(user, done) {
    done(null, user);
  });
  
  passport.deserializeUser(function(id, done) {
        User.findById(id, function(err, user) {
              done(err, user);
            });
          });
        
passport.use(new GoogleStrategy({
    clientID: GOOGLE_CLIENT_ID,
    clientSecret: GOOGLE_CLIENT_SECRET,
    callbackURL: "http://localhost:3000/Auth/google/secret",
      // This option tells the strategy to use the userinfo endpoint instead
      // protection  against the  deprecation of googleplus Api
    userProfileURL: "https://www.googleapis.com/oauth2/v3/userinfo",
  },
  (accessToken, refreshToken, profile, cb)=>{
    console.log(profile)
    //never use findOrCreate 
    //works for login and register
    User.findOne({ googleId: profile.id})
    .then( existingUser=>{
       if(existingUser){
        cb(null, existingUser);
       }else{
         new  User({username: profile.displayName, googleId: profile.id,name:profile.name})
         .save()
         .then(user=>cb(null,user)).catch(console.error);
       }
    }).catch(console.error);
  }
));



 // schema and model are all in their module file

app.route("/").get((req,res)=>{
    res.render("home");
})
app.route("/login")

.get((req,res)=>{
  req.isAuthenticated()?res.redirect("/secrets"):res.render("login");
})
/* using passport.authenticate as a middleware that 
sets the req.user  invoke req.login() */
.post( 
    // passport.authenticate("local",{
    //     successRedirect: "/secrets",
    //     failureRedirect: "/login"
    // }),
    (req,res)=>{
    const user = new User({
        username:req.body.username.trim(),
        password:req.body.password
        });
    req.login(user,(err)=>{//create session 
       if(err){return next(err);}
       passport.authenticate("local")(req,res,()=>{ // authenticate and create session 
        res.redirect("/secrets");
    })
        });
    }
);

/* Oauth google  */
app.get("/auth/google",
  passport.authenticate("google", { scope: ["profile"] }));

  
  app.get("/auth/google/secret", 
  passport.authenticate("google", { failureRedirect: "/login" }),
  function(req, res) {
    // Successful authentication, redirect home.
    res.redirect("/secrets");
  });


app.get("/register",(req,res)=>{
    res.render("register");
});

app.post("/register",(req,res)=>{
    User.register({username:req.body.username},req.body.password)
    .then(user=> passport.authenticate("local")(req,res,()=>{
        res.redirect("/secrets");
    }))
    .catch(err=>{console.error(err);res.redirect("/register")})
})
  const isLoggedIn=(req,res,next)=>{
    if(req.isAuthenticated()){
        return next();
    }
        res.redirect("/login")
}
app.get("/secrets",isLoggedIn,(req,res)=>{
   res.render("secrets");
})
 
app.get("/logout",(req,res)=>{
    req.logout();
    res.redirect('/login');
})
app.listen(PORT,()=>{
    console.log(`successfully connecting to port ${PORT}`);
})