Rails.application.routes.draw do
  get 'raspberry/pi'
  mount RailsAdmin::Engine => '/admin', as: 'rails_admin'
  get 'records/listen', to: 'records#listen'
  get 'records/result', to: 'records#result'
  resources :records
  devise_for :users
  root to: 'pages#home'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
