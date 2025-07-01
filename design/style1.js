const a=document.getElementById ("valueA");

const b=document.querySelector ("#valueB"); 
console.log("A", a);
console.log("B", b);

var valueA, valueB, add; 
a.addEventListener("keyup", (e)=>{ 
    console.log(e.target.value); 
    valueA-Number(e.target.value);
})

b.addEventListener("keydown", (e)=>{ 
    console.log(e.target.value); 
    valueB-Number(e.target.value);
})

console.log(valueA); 
console.log(valueB); 