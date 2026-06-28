let chart;

function predictFish(){

let fileInput = document.getElementById("imageInput").files[0];

let formData = new FormData();
formData.append("image", fileInput);

fetch("/predict",{
method:"POST",
body:formData
})
.then(res => res.json())
.then(data => {

document.getElementById("result").innerHTML =
"Predicted Fish: " + data.prediction +
" (" + data.confidence + "% confidence)";

let d = data.details;

let html = `

<div class="details">

<h3>General Information</h3>

<p><b>Scientific Name:</b> ${d.scientific}</p>
<p><b>Category:</b> ${d.category}</p>
<p><b>Habitat:</b> ${d.habitat}</p>
<p><b>Taste:</b> ${d.taste}</p>
<p><b>Average Price:</b> ${d.price}</p>
<p><b>Available In:</b> ${d.availability}</p>

<h3>Nutritional Value (per 100g)</h3>

<table class="nutrition-table">

<tr><td>Protein</td><td>${d.protein}</td></tr>
<tr><td>Fat</td><td>${d.fat}</td></tr>
<tr><td>Calories</td><td>${d.calories}</td></tr>
<tr><td>Omega-3</td><td>${d.omega3}</td></tr>

</table>

<h3>Health Benefits</h3>
<ul>${d.benefits.map(b=>"<li>"+b+"</li>").join("")}</ul>

<h3>Disadvantages</h3>
<ul>${d.disadvantages.map(b=>"<li>"+b+"</li>").join("")}</ul>

<h3>Who Should Eat</h3>
<ul>${d.who_should_eat.map(b=>"<li>"+b+"</li>").join("")}</ul>

<h3>Who Should Avoid</h3>
<ul>${d.who_should_avoid.map(b=>"<li>"+b+"</li>").join("")}</ul>

<h3>Best Cooking Methods</h3>
<ul>${d.best_cooking_methods.map(b=>"<li>"+b+"</li>").join("")}</ul>

</div>

`;

document.getElementById("fishDetails").innerHTML = html;


createChart(d);

});

let reader = new FileReader();

reader.onload = function(e){

document.getElementById("preview").src = e.target.result;

};

reader.readAsDataURL(fileInput);

}



function createChart(d){

let protein = parseFloat(d.protein);
let fat = parseFloat(d.fat);
let calories = parseFloat(d.calories);

if(chart) chart.destroy();

chart = new Chart(

document.getElementById("nutritionChart"),

{

type:'pie',

data:{

labels:["Protein (g)","Fat (g)","Calories"],

datasets:[{

data:[protein,fat,calories],

backgroundColor:[

"#38bdf8",
"#22c55e",
"#f97316"

],

borderWidth:1

}]

},

options:{

responsive:true,

plugins:{
legend:{
position:'bottom',
labels:{
color:'white',
font:{
size:14
}
}
}
}

}

}

);

}