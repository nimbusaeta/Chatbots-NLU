import boto3
client = boto3.client("lex-models")

response = client.put_intent(
	name="EnableDevice",
	description="",
	slots=[
		{
			"name": "device",
			"slotConstraint": "Required",
			"slotType": "device",
			"slotTypeVersion": "$LATEST",
			"valueElicitationPrompt": {
				"messages": [
					{
						"contentType": "PlainText",
						"content": "What do you want me to {enable}?"
					}, {
						"contentType": "PlainText",
						"content": "What should I {enable}?"
					}
				],
				"maxAttempts": 3,
				"responseCard": "string"
			},
			"priority": 3,
			"sampleUtterances": [
				"a {device}",
				"the {device}"
			],
			"responseCard": "string"
		}, {
			"name": "enable",
			"slotConstraint": "Required",
			"slotType": "enable",
			"slotTypeVersion": "$LATEST",
			"valueElicitationPrompt": {
				"messages": [
					{
						"contentType": "PlainText",
						"content": "What should I do with the {device}?"
					}
				],
				"maxAttempts": 3,
				"responseCard": "string"
			},
			"priority": 3,
			"sampleUtterances": [
				"{enable} it"
			],
			"responseCard": "string"
		},
	],
	sampleUtterances=[
		"{enable} the {device}",
		"{enable} a {device}",
		"{enable} something",
		"{device}",
		"{enable}"
	],
	confirmationPrompt={
		"messages": [
			{
				"contentType": "PlainText",
				"content": "So you want me to {enable} the {device}?"
			}
		],
		"maxAttempts": 3,
		"responseCard": "string"
	},
	rejectionStatement={
		"messages": [
			{
				"contentType": "PlainText",
				"content": "Ok, I won't {enable} anything"
			}
		],
		"responseCard": "string"
	},
	conclusionStatement={
		"messages": [
			{
				"contentType": "PlainText",
				"content": "Ok, I will {enable} the {device}!"
			}
		]
	}
# parentIntentSignature="0001",
# checksum = ""
)
