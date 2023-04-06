from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired, ValidationError
from walkthrough.models import Company, Location

# Company Forms
class CreateCompanyForm(FlaskForm):
    # Check that company does not already exist in database
    def validate_name(self, name_to_check):
        company = Company.query.filter_by(name=name_to_check.data).first() #access first result/object
        if company:
            raise ValidationError('Company already exists. Please try a different Company')
        
    company_name = StringField(label="Company Name", validators=[Length(min=2,max=50), DataRequired()])
    submit = SubmitField(label="Create Company")

class DeleteCompanyForm(FlaskForm):
    submit = SubmitField(label="Delete Company")

# Location Forms
class CreateLocationForm(FlaskForm):
    def validate_location(self, city_to_check, state_to_check, company_to_check):
        # Check if location with city, state, and company already exists
        # Company can possibly be pulled from url or passed in
        location = Location.query.filter_by(city=city_to_check, state=state_to_check)
        if location:
            pass

    city = StringField(label="City", validators=[Length(min=3, max=50), DataRequired()])
    state = StringField(label="State", validators=[Length(min=3, max=50), DataRequired()])
    submit = SubmitField(label="Create Location")
    

class DeleteLocationForm(FlaskForm):
    submit = SubmitField(label="Delete Location")