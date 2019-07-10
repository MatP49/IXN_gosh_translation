class RecordsController < ApplicationController
  
  before_action :set_record, only: [:show, :edit, :update, :destroy]

  # GET /records
  # GET /records.json
  def index
    @records = Record.all
  end

  def listen
  end

  def result
    @definitions = ""
    file = File.open("definitions.txt", "r")
    file.each do |definition|
      @definitions += definition
    end
    file.close

    @transcript_text = ""
    file_transcript = File.open("transcript.txt", "r")
    file_transcript.each do |x|
      @transcript_text += x
    end
    file_transcript.close

    @email = ""
    file_email = File.open("email.txt", "r")
    file_email.each do |x|
      @email += x

    end
    file_email.close
    @email_final = @email.delete!("\n")

     UserMailer.email_to_send(@email_final).deliver_now

  
    
  end

  # GET /records/1
  # GET /records/1.json
  def show
  end

  # GET /records/new
  def new
    @record = Record.new
  end

  # GET /records/1/edit
  def edit
  end

  # POST /records
  # POST /records.json
  def create

   
    @record = Record.new(record_params)
    @name = @record.name
    @record.transcript = @record.transcript.gsub(@name, 'John Doe')


    file = File.open("transcript.txt", "w")
    file.puts @record.transcript
    file.close

     @language = @record.language


    file = File.open("language.txt", "w")
    file.puts @record.language
    file.close

    @email = @record.email

    file = File.open("email.txt", "w")
    file.puts @record.email
    file.close


    file = File.open("language.txt", "w")
    file.puts @record.language
    file.close



    respond_to do |format|
      if @record.save
        format.html { redirect_to @record, notice: 'Record was successfully created.' }
        format.json { render :show, status: :created, location: @record }
      else
        format.html { render :new }
        format.json { render json: @record.errors, status: :unprocessable_entity }
      end
    end

    
  end

  # PATCH/PUT /records/1
  # PATCH/PUT /records/1.json
  def update
    respond_to do |format|
      if @record.update(record_params)
        format.html { redirect_to @record, notice: 'Record was successfully updated.' }
        format.json { render :show, status: :ok, location: @record }
      else
        format.html { render :edit }
        format.json { render json: @record.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /records/1
  # DELETE /records/1.json
  def destroy
    @record.destroy
    respond_to do |format|
      format.html { redirect_to records_url, notice: 'Record was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_record
      @record = Record.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def record_params
      params.require(:record).permit(:email, :name, :transcript, :language)
    end



end
