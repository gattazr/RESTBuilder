{
	"name": "CohorteAPI",
	"root": {
		"name": "CohorteAPI",
		"components": [
			{
				"name" : "cohorte-api-database",
				"factory" : "cohorteapi.database_factory",
				"isolate": "api"
			}
			,{
				"name" : "cohorte-api-records",
				"factory" : "cohorteapi.records_factory",
				"isolate": "api"
			}
		]
	}
}
