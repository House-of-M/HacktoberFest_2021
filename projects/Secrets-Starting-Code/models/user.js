const mongoose = require( "mongoose");
const passportLocalMongoose = require('passport-local-mongoose');
// const findOrCreate = require('mongoose-findorcreate');

const Schema = mongoose.Schema;
const nameSchema = new Schema({
    familyName:String,
    givenName:String
});
const userSchema=new Schema({
    email:String,
    password:String,
    googleId: String,
    name:nameSchema

});
userSchema.plugin(passportLocalMongoose);
// userSchema.plugin(findOrCreate);
// nameSchema .plugin(passportLocalMongoose);
// nameSchema .plugin(findOrCreate);
module.exports=mongoose.model("User",userSchema);