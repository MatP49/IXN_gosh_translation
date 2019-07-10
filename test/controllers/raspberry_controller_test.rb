require 'test_helper'

class RaspberryControllerTest < ActionDispatch::IntegrationTest
  test "should get pi" do
    get raspberry_pi_url
    assert_response :success
  end

end
