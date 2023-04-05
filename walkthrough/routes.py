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
        # Inlcude getting all records (query all locations, and for each location query all sites, etc)
        # May need functions to check all associated records
        deleted_company = request.form.get('deleted_company') # value = company.id
        d_company_obj = Company.query.filter_by(id=deleted_company).first()
        db.session.delete(d_company_obj)
        db.session.commit()
    companies = Company.query.all()
    return render_template('companies.html', form=cc_form, companies=companies, del_form=dc_form)



#LOCATIONS PAGE
@app.route('/<company_name>/locations', methods=['GET', 'POST'])
def locations_page(company_name):
    company = Company.query.filter_by(name=company_name).first()
    cl_form = CreateLocationForm()
    dl_form = DeleteLocationForm()

    if request.method == "POST":
        # Create Location logic
        if cl_form.validate_on_submit():
            location_to_create = Location(city=cl_form.city.data, state=cl_form.state.data, company_id=company.id)
            db.session.add(location_to_create)
            db.session.commit()
            flash(f"Location added sucessfully!", category="success")
            return redirect(url_for('locations_page', company_name=company.name))
        
        if cl_form.errors != {}:
            for err_mg in cl_form.errors.values():
                flash(f"Something went wrong when attempting to create location: {err_mg}", category='danger')

        # Delete Location logic
        deleted_location = request.form.get('deleted_location') # value = location.id
        d_location_obj = Location.query.filter_by(id=deleted_location).first()
        db.session.delete(d_location_obj)
        db.session.commit()


    company_locations = Location.query.filter_by(company_id=company.id)

    return render_template('locations.html', form=cl_form, d_form=dl_form, locations=company_locations)


# SITES PAGE
@app.route('/sites')
def sites_page():
    return render_template('home.html')