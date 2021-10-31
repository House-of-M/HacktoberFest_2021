
const express = require("express");
const mongoose= require("mongoose");
const _= require("lodash"); 

const date = require(__dirname + "/date.js");

const app = express();

app.set('view engine', 'ejs');

app.use(express.urlencoded({extended: true}));
app.use(express.static("public"));

mongoose.connect("mongodb://localhost:27017/todo-list",{useNewUrlParser:true});


//  const items = ["Buy Food", "Cook Food", "Eat Food"];
// const workItems = [];

const itemsSchema= mongoose.Schema({
  name:{
    required:`it needs a name`,
    type:String
  }});
  const listItemsSchema= mongoose.Schema({
    name:{
      required:`it needs a name`,
      type:String
    },
    items:[itemsSchema]});  

const Items= mongoose.model("items",itemsSchema);
const Lists= mongoose.model("lists",listItemsSchema);
const defaultItems=[{name:"Buy Food"}, {name:"Cook Food"}, {name:"Eat Food"}];



app.get("/", function(req, res) {
 Items.find( (err,items)=>{
      if (err) console.log(err);
      if(items){ 
        res.render("list", {listTitle: "today", newListItems: items});
      }else{
        Items.insertMany(defaultItems,(err)=>{
          if(err)console.log(err);else{ console.log(`that was a success boi`);res.redirect("/");}
        });
      } 
  });
});



app.post("/:listName", function(req, res){
  const listName= req.params.listName;
  console.log(listName);
  const newItem = req.body.newItem;
  console.log(newItem);

    const item=new Items({name:newItem});
  
    Lists.updateOne({name:listName},{$addToSet:{items:item}}, (err,list)=>{
      if (err) console.log(err);
      else{if(list) 
        res.redirect(`/${listName}`);
      }
});

    // Items.create(item,(err)=>{
    //   if(err)console.log(err);else{    res.redirect("/");}});
  
});


app.post("/delete", function(req, res){
  const removeItemId=req.body.checkbox.toString().trim();
  Items.findByIdAndDelete(removeItemId,(err,item)=>{
    if(err)console.log(err);else{
      console.log(item);
      res.redirect("/");
    }
  })
});
app.post("/delete/:listName", function(req, res){
  const listName=_.toLower(req.params.listName).trim();
  console.log(listName);
  const removeItemId=req.body.checkbox.toString().trim();
  console.log(removeItemId);
  
    Lists.updateOne({name:listName},{$pull:{items:{_id:removeItemId}}}, (err,list)=>{
      if (err) console.log(err);
      else{if(list) 
        res.redirect(`/${listName}`);
      }
    });
  // const removeItemId=req.body.checkbox.toString().trim();
  // Items.findByIdAndDelete(removeItemId,(err,item)=>{
  //   if(err)console.log(err);else{
  //     console.log(item);
  // res.redirect("/");
  //     }
  //   });
  });
app.get("/:listName", function(req,res){
  const listName= _.toLower(req.params.listName).trim();
  // console.log(listName);
  const List= new Lists({
    name:listName,
    items:defaultItems});

  Lists.findOne({name:listName}, (err,list)=>{
      if (err) console.log(err);
      if(list){ 
        res.render("list", {listTitle: list.name, newListItems: list.items});
      }else{
        List.save();
        res.redirect(`/${listName}`);
      }
});
 
});

app.get("/about", function(req, res){
  res.render("about");
});

app.listen(3000, function() {
  console.log("Server started on port 3000");
});
