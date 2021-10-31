const mongoose = require( "mongoose");

const encrypt = require( "mongoose-encryption");

mongoose.connect("mongodb://localhost:27017/userDB",{useNewUrlParser:true});


const userSchema=new mongoose.Schema({
    email:String,
    password:String
});

const secret ="Thisisourlittlesecret.";

userSchema.plugin(encrypt.migrations, {secret:secret,encryptedFields:['password']});
const User = mongoose.model('User', userSchema);
User.migrateToA(function(err){
    if (err){ throw err; }
    console.log('Migration successful');
});