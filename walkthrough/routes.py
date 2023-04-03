from walkthrough import app, db
from flask import render_template, request, flash, redirect, url_for
from walkthrough.models import Company, Location
from walkthrough.forms import CreateCompanyForm, DeleteCompanyForm

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/companies', methods=['GET', 'POST'])
def companies_page():
    # Main functionality will be viewing/creating companies
    # Will need functions to create/delete companies (include in models.py)
    # Will need a form to get the information for creating, along with a form to validate deletion
    cc_form = CreateCompanyForm()
    dc_form = DeleteCompanyForm()
    if request.method == "POST":
        # Create Company logic
        if cc_form.validate_on_submit():
            company_to_create = Company(name=cc_form.company_name.data)
            db.session.add(company_to_create)
            db.session.commit()
            flash(f"Company added sucessfully!", category="success")
            return redirect(url_for('companies_page'))
        
        if cc_form.errors != {}:
            for err_mg in cc_form.errors.values():
                flash(f"Something went wrong when attempting to create company: {err_mg}", category='danger')
    companies = Company.query.all()
    # if request.method == "GET":
    #     companies = Company.query.all()
    #     return companies
    return render_template('companies.html', form=cc_form, companies=companies)



#SITE PAGE
def sites_page():
    # include way to specify which company/site the page is for
    pass

