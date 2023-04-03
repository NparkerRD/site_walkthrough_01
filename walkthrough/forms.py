from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from walkthrough.models import Company

# Company Forms
class CreateCompanyForm(FlaskForm):
    # Check that company does not already exist in database
    def validate_company(self, company_to_check):
        company = Company.query.filter_by(name=company_to_check.data).first()

        if company:
            raise ValidationError(f'It appears this company, {company_to_check.name}, already exists. Please try a different name.')
        
    company_name = StringField(label="Company Name", validators=[Length(min=2,max=50), DataRequired()])
    submit = SubmitField(label="Create Company")

class DeleteCompanyForm(FlaskForm):
    submit = SubmitField(label="Delete Company")

