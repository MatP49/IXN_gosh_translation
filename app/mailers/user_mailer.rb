class UserMailer < ApplicationMailer
default from: 'testbabelucl@gmail.com'

  def email_to_send(user)
  	user = "PATIENT"
  	@email = ""
    file_email = File.open("email.txt", "r")
    file_email.each do |x|
      @email += x
    end
    file_email.close
    @email_final = @email.delete!("\n")
    mail(to: @email_final, subject: 'Welcome to My Awesome Site')
  end

end