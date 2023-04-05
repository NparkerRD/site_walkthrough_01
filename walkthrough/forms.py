from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from walkthrough.models import Company, Location

# Company Forms
class CreateCompanyForm(FlaskForm):
    # Check that company does not already exist in database
    def validate_company(self, company_to_check):
        company = Company.query.filter_by(name=company_to_check.data).first()

        if company:
            raise ValidationError('This company alrady exists. Please try another company')
        
    company_name = StringField(label="Company Name", validators=[Length(min=2,max=50), DataRequired()])
    submit = SubmitField(label="Create Company")

class DeleteCompanyForm(FlaskForm):
    submit = SubmitField(label="Delete Company")

# Location Forms
class CreateLocationForm(FlaskForm):
    def validate_location(self, city_to_check, state_to_check, company_to_check):
        # Check if location with city, state, and company already exists
        # Company can possibly be pulled from url or passed in
        location = Location.query.filter_by(city=city_to_check, state=state_to_check, company_id=company_to_check)
        pass

    city = StringField(label="City", validators=[Length(min=3, max=50), DataRequired()])
    state = StringField(label="State", validators=[Length(min=3, max=50), DataRequired()])
    submit = SubmitField(label="Create Location")
    

class DeleteLocationForm(FlaskForm):
    submit = SubmitField(label="Delete Location")