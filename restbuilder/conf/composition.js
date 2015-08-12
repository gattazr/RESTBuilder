{
	"name": "RESTBuilder",
	"root": {
		"name": "RESTBuilder",
		"components": [
			{
				"name" : "RESTBuilder-database",
				"factory" : "restbuilder.database_factory",
				"isolate": "rest-api-isolate"
			}
			,{
				"name" : "RESTBuilder-records",
				"factory" : "restbuilder.records_factory",
				"isolate": "rest-api-isolate"
			}
		]
	}
}
