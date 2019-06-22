class AddLanguageToRecords < ActiveRecord::Migration[5.2]
  def change
    add_column :records, :language, :string
  end
end
