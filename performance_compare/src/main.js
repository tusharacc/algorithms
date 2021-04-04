const fs = require('fs');
const {readCsvToJson} = require('./csvparse')
var Chart = require('chart.js');

const sortAlgoAvailable = [];

const programsAvailable = ['PYTHON','C','C++','RUST']

const folders = fs.readdirSync('../');

console.log("Folders", folders);

folders.forEach((data) =>{
	if (data.includes('sort')){
		sortAlgoAvailable.push(data.toUpperCase())
	}
})

console.log("Sort Folders", sortAlgoAvailable);

let checkBoxes = document.getElementById('sort-available')

sortAlgoAvailable.forEach((data)=>{
	createInputTag('checkbox','sort-algo',data,checkBoxes);
})

let radiobuttons = document.getElementById('choose-program')

programsAvailable.forEach((data)=>{
	let el = createInputTag('radio','programs',data,radiobuttons);
	el.addEventListener('change',(event)=>{
		console.log("The event is", event);
		let checkboxSel = document.querySelectorAll('input[type="checkbox"]');
		let noneChecked = true;
		let checkedValue = []
		checkboxSel.forEach((control) =>{
			if (control.checked){
				noneChecked = false;
				checkedValue.push(control.value)
			}
		})

		if (noneChecked){
			showMessage("Please check sort algorithms");
		}

		console.log("The checked value is", checkedValue);
		checkedValue.forEach((data) =>{
			readCsvToJson(data.toLowerCase(),'python')
			.then((data) =>{
				//console.log("The response from readCsvToJson", data);
				let countOfItems = [];
				let timeInMillis = [];
				let reducedArray = data.map(x => [x['number_of_items'],x['time_taken']] );
				reducedArray.sort(function(a, b) {
				  return a[0] - b[0];
				});
				countOfItems = reducedArray.map(x => x[0]);
				timeInMillis = reducedArray.map(x => x[1]);
				createChart(countOfItems,timeInMillis);
			})
			.catch((err) =>{
				console.error("Error", err)
			})	
		})
		
	})
})

function showMessage(message){
	console.log("The message received is", message)
	let el = document.getElementById('message-box');
	el.innerText = message;
	setTimeout((el)=>{
		el.innerText = '';
	},5000,el)
}

function createInputTag(type,name,value,parent){
	let container = document.createElement('div');
	container.classList = "control";

	let input = document.createElement("input");
	input.type = type;
	input.name = name;
	input.value = value;
	input.id = value;

	let label = document.createElement('label')
	label.htmlFor = value;
	label.appendChild(document.createTextNode(value));

	container.appendChild(input);
	container.appendChild(label);
	parent.appendChild(container);
	return input;

}

function createChart(countOfItems, timeInMillis){

	console.log("The time in millis", timeInMillis)
	var ctx = document.getElementById('myChart');
	var myChart = new Chart(ctx, {
	    type: 'line',
	    data: {
	        labels: countOfItems,
	        datasets: [{
	            label: 'Time taken for Sorting',
	            data: timeInMillis,
	            fill: false,
			    borderColor: 'rgb(75, 192, 192)',
			    tension: 0.1,
	        	borderWidth: 1
	        }]
	    },
	    options: {
	        scales: {
	            y: {
	                beginAtZero: true
	            }
	        }
	    }
	});

}