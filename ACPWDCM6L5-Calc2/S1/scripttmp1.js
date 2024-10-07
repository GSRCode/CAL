
function printOutput(num){
    document.getElementById("output-value").innerText=num;
}

function getOutput(){
	return document.getElementById("output-value").innerText;
}

function getHistory(){
	return document.getElementById("history-value").innerText;
}
function printHistory(num){
	document.getElementById("history-value").innerText=num;
}



var operator = document.getElementsByClassName("operator");
for(var i =0;i<operator.length;i++){
	operator[i].addEventListener('click',function(){

		if(this.id=="clear"){
			printHistory("");
			printOutput("");
		}
        else if(this.id=="backspace"){
			var output=getOutput();
			if(output){//if output has a value
				output= output.substring(0,output.length-1);
				printOutput(output);
			}
		}
        else {

			var output=getOutput();
			var history=getHistory();

            if(this.id=="="){
                var opt = history + output
                var result=eval(opt);
                printOutput(result);
                printHistory("");
            }
            else{
                history=output+this.id;
                printHistory(history);
                printOutput("");
            }
       
        }


    });
}



var number = document.getElementsByClassName("number");
for(var i =0;i<number.length;i++){
	number[i].addEventListener('click',function(){

        let output = getOutput()
        if(output != NaN){
            output = output + this.id
            printOutput(output);
        }
        
    });
}