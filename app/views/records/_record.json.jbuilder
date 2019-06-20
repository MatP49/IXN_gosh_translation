json.extract! record, :id, :email, :name, :transcript, :created_at, :updated_at
json.url record_url(record, format: :json)
