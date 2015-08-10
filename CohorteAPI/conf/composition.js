{
	"name": "CohorteAPI",
	"root": {
		"name": "CohorteAPI",
		"components": [
			{
				"name" : "CohorteAPI-database",
				"factory" : "cohorteapi.database_factory",
				"isolate": "CohorteAPI-isolate"
			}
			,{
				"name" : "CohorteAPI-records",
				"factory" : "cohorteapi.records_factory",
				"isolate": "CohorteAPI-isolate"
			}
		]
	}
}
