from walkthrough import app, db
from flask import render_template, request, flash, redirect, url_for
from walkthrough.models import Company, Location
from walkthrough.forms import *

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

        # Delete Company logic
        deleted_company = request.form.get('deleted_company')
        d_company_obj = Company.query.filter_by(name=deleted_company).first()
        if d_company_obj:
            d_company_obj.delete_company()
            flash(f"{d_company_obj.name} was deleted", category="danger")
    companies = Company.query.all()
    return render_template('companies.html', form=cc_form, companies=companies, del_form=dc_form)



#LOCATION PAGE
# @app.route('<company_name>/locations')
@app.route('/locations')
def locations_page():
    # include way to specify which company/site the page is for
    #       use something similar to @app.route('/<company_name>/locations')
    #       https://exploreflask.com/en/latest/views.html
    # TEMPORARY: displaying ALL locations for styling purposes; will display locations only related to company later
    cl_form = CreateLocationForm()
    dl_form = DeleteLocationForm()

    if request.method == "POST":
        # Create Location logic
        if cl_form.validate_on_submit():
            location_to_create = Location()
            db.session.add(location_to_create)
            db.session.commit()
            flash(f"Location added sucessfully!", category="success")
            return redirect(url_for('locations_page'))
        
        if cl_form.errors != {}:
            for err_mg in cl_form.errors.values():
                flash(f"Something went wrong when attempting to create location: {err_mg}", category='danger')

    return render_template('locations.html', form=cl_form)

