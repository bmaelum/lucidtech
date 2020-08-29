from las import Client

client = Client()
document = client.create_document('invoice.pdf')
prediction = client.create_prediction(document_id=document.id, model_name='invoice')

print(prediction)