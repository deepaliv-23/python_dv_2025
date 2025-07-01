const grandparent = document.querySelector(".grandparent");
// const parent = document.querySelector(".parent");
// const child = document.querySelector(".child");

// addEventListener (event,function,capture="true")
// Capturing Events


child.addEventListener("click",()=>{
    console.log("Capture !!!!!!  Child !!");
},true);


parent.addEventListener("click",()=>{
    console.log("Capture !!!!!!  parent !!");
},true);


grandparent.addEventListener("click",()=>{
    console.log("Capture !!!!!!  grandparent !!");
},true);


document.body.addEventListener("click",()=>{
    console.log("Capture !!!!!!  body !!");
},true);