import boto3
client = boto3.client('lex-models')

response = client.put_slot_type(
	name='enable',
	description='',
	enumerationValues=[
		{
			"value": "enable",
			"synonyms": [
				"enable"
			]
		},
		{
			"value": "turn on",
			"synonyms": [
				"turn on"
			]
		},
		{
			"value": "switch on",
			"synonyms": [
				"switch on"
			]
		}
	]
# checksum='1',
# valueSelectionStrategy='ORIGINAL_VALUE'|'TOP_RESOLUTION'
)

response = client.put_slot_type(
	name='device',
	description='',
	enumerationValues=[
		{
			"value": "alarm",
			"synonyms": [
				"alarm"
			]
		},
		{
			"value": "TV",
			"synonyms": [
				"TV"
			]
		}
	]
# checksum='1',
# valueSelectionStrategy='ORIGINAL_VALUE'|'TOP_RESOLUTION'
)