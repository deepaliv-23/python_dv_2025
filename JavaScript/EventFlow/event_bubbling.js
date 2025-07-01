// 1. Event Bubbling / Event Propogation.
// 2. Event Capturing.
// 3. Event Delegation.



// addEventListener (event,function,capture="false")
//  Event Bubbling / Event Propogation.

//-------------------------------------------------------------------
child.addEventListener("click",()=>{
    console.log("Bubble Child !!");
})


parent.addEventListener("click",()=>{
    console.log("Bubble parent !!");
})


grandparent.addEventListener("click",()=>{
    console.log("Bubble grandparent !!");
})


document.body.addEventListener("click",()=>{
    console.log("Bubble body !!");
})


// ---Event Delegation
grandparent.addEventListener("click",(e)=>{
    console.log(e.target);
})