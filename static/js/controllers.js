/* Switch Controllers */

function actionSwitch(host, id, action)
{
	$.getJSON(host+"/switches/"+id+"/"+action+"/", function(data) {
		condole.log(data);
	});
}

function turnSwitchOn(host, id)
{
	console.log("Turning switch " + id + " on");
	actionSwitch(host,id,1);
}

function turnSwitchOff(host, id)
{
	console.log("Turning switch " + id + " off");
	actionSwitch(host,id,0);
}


