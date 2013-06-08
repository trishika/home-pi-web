'use strict';

/* Services */

var app = angular.module('homePiApp.services', ['ngResource']);

var url = "http://localhost:8001/switches";
//var url = "http://rcswitch.apiary.io/switches";

app.value('version', '1.0');

app.service('Switch', function($http) {

	this.query = function() {
		console.log("Returning Switches");
		return $http.get(url).then(function (response) {
			console.log(response);
			return response.data;
		});
	};

	this.turnOn = function(id) {
		console.log(id);
		var request = '{"status": "1"}';
		console.log(request);
		return $http.put(url + "/" + id,request).then(function (response) {
			console.log(response);
			return response.data;
		});
	};

	this.turnOff = function(id) {
		console.log(id);
		var request = '{"status": "0"}';
		console.log(request);
		return $http.put(url + "/" + id,request).then(function (response) {
			console.log(response);
			return response.data;
		});
	};

	this.turnAllSwitchesOn = function() {
		console.log("Turning on all switches");
		var request = '{"status": "1"}';
		console.log(request);
		return $http.put(url,request).then(function (response) {
			console.log(response);
			return response.data;
		});
	};

	this.turnAllSwitchesOff = function() {
		console.log("Turning off all switches");
		var request = '{"status": "0"}';
		console.log(request);
		return $http.put(url,request).then(function (response) {
			console.log(response);
			return response.data;
		});
	};

});

