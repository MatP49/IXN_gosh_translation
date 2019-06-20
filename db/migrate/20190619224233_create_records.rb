class CreateRecords < ActiveRecord::Migration[5.2]
  def change
    create_table :records do |t|
      t.string :email
      t.string :name
      t.text :transcript

      t.timestamps
    end
  end
end
