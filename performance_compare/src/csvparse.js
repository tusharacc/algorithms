const csv = require('papaparse');
const path = require('path');
const fs = require('fs')




function readCsvToJson(...folders){
	let csvFile = path.join('..',...folders,'performance.csv');
	const file = fs.createReadStream(csvFile);
	return new Promise((resolve,reject) => {
		var csvData=[];
		csv.parse(file,{
		  header: true,
		  step: function(result) {
		    csvData.push(result.data)
		  },
		  complete: (results, file) =>{
		  	resolve(csvData);
		  } ,
		  error: (err,file) => {
		  	reject(err)
		  }
		});
	});
}


/*readCsvToJson('mergesort','python')
.then((data) =>{
	console.log("The response from readCsvToJson", data)
})
.catch((err) =>{
	console.error("Error", err)
})*/

module.exports = {
	readCsvToJson,
}
