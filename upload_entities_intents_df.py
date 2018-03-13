import json
import requests
from time import sleep

# Upload entity types out of a list
def dialogflow_client_put_entity_types(all_entity_types):
	for entity_type in all_entity_types:
		entity_type_json = json.dumps(entity_type)
		res = requests.put(
			'https://api.api.ai/v1/entities?v=20170712',
			headers = {"Authorization": "bearer 2cb9423f7501441d987806f014384779",
			"Content-Type": "application/json; charset=utf-8"},
			data = entity_type_json)
		print(res.status_code)
		if not res.status_code == 200:
			print(entity_type_json)
		sleep(1)

# Upload intents out of a list
def dialogflow_client_put_intents(all_intents):
	for intent in all_intents:
		intent_json = json.dumps(intent)
		res = requests.post(
			'https://api.api.ai/v1/intents?v=20170712',
			headers={"Authorization": "bearer 2cb9423f7501441d987806f014384779",
			"Content-Type": "application/json; charset=utf-8" },
			data=intent_json)
		if not res.status_code == 200:
			print(intent_json)
		print(res.status_code)
		sleep(1)

# Data
entity_types = [
	{
		"name": "enable",
		"entries": [
			{
				"synonyms": [],
				"value": "enable"
			}, {
				"synonyms": [],
				"value": "switch on"
			}, {
				"synonyms": [],
				"value": "activate"
			}
		]
	}, {
		"name": "device",
		"entries": [
			{
				"synonyms": [],
				"value": "alarm"
			}, {
				"synonyms": [],
				"value": "TV"
			}, {
				"synonyms": [],
				"value": "lights"
			}
		]
	}
]

intents = [
	{
		"name": "EnableDevice",
		"auto": True,
		"templates": [
			"@enable @device",
			"@device",
			"@enable the @device",
			"@enable the @device, please"
		],
		"userSays": [],
		"contexts": [],
		"responses": [
			{
				"messages": [
					{
						"type": 0,
						"speech": [
							"Ok, I will $enable the $device!",
							"Ok, I will turn on the $device!"
						],
						"lang": "en"
					}
				],
				"affectedContexts": [],
				"speech": [],
				"action": "EnableDevice",
				"parameters": [
					{
						"prompts": [
							"what should I $enable?"
						],
						"name": "device",
						"required": True,
						"dataType": "@device",
						"value": "$device"
					},
					{
						"name": "enable",
						"required": False,
						"dataType": "@enable",
						"value": "$enable"
					}
				],
				"resetContexts": True
			}
		],
		"priority": 500000
	}
]

# Upload entities and intents
dialogflow_client_put_entity_types(entity_types)
dialogflow_client_put_intents(intents)