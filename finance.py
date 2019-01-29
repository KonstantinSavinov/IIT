def get_federal_income_tax_deduction(employee_salary, employee_marriage_status):
    if employee_marriage_status == "NO" or "no" or "No" or "None" or "N" or "n" or False:
        if (employee_salary >= 0) and (employee_salary <= 9525):
            tax = (.1 * employee_salary)
        elif (employee_salary >= 9526) and (employee_salary <= 38700):
            tax = (.1 * 9525) + (.12 * (employee_salary - 9525))
        elif (employee_salary >= 38701) and (employee_salary <= 82500):
            tax = (.1 * 9525) + (.12 * (38700 - 9525)) + (.22 * (employee_salary - 38700))
        elif (employee_salary >= 82501) and (employee_salary <= 157500):
            tax = (.1 * 9525) + (.12 * (38700 - 9525)) + (.22 * (82500 - 38700)) + (
                    .24 * (employee_salary - 82500))
        elif (employee_salary >= 157501) and (employee_salary <= 200000):
            tax = (.1 * 9525) + (.12 * (38700 - 9525)) + (.22 * (82500 - 38700)) + (.24 * (157500 - 82500)) + (
                    .32 * (employee_salary - 157500))
        elif (employee_salary >= 200001) and (employee_salary <= 500000):
            tax = (.1 * 9525) + (.12 * (38700 - 9525)) + (.22 * (82500 - 38700)) + (.24 * (157500 - 82500)) + (
                    .32 * (200000 - 157500)) + (.35 * (employee_salary - 200000))
        elif employee_salary >= 500001:
            tax = (.1 * 9525) + (.12 * (38700 - 9525)) + (.22 * (82500 - 38700)) + (.24 * (157500 - 82500)) + (
                    .32 * (200000 - 157500)) + (.35 * (500000 - 200000)) + (.37 * (employee_salary - 500000))
        else:
            pass
    if employee_marriage_status == "YES" or "yes" or "Yes" or "Y" or "y" or True:
        if (employee_salary >= 0) and (employee_salary <= 19050):
            tax = (.1 * employee_salary)
        elif (employee_salary >= 19050) and (employee_salary <= 77400):
            tax = (.1 * 19050) + (.12 * (employee_salary - 19050))
        elif (employee_salary >= 77401) and (employee_salary <= 165000):
            tax = (.1 * 19050) + (.12 * (77400 - 19050)) + (.22 * (employee_salary - 77400))
        elif (employee_salary >= 165001) and (employee_salary <= 315000):
            tax = (.1 * 19050) + (.12 * (77400 - 19050)) + (.22 * (165000 - 77400)) + (
                    .24 * (employee_salary - 165000))
        elif (employee_salary >= 315001) and (employee_salary <= 400000):
            tax = (.1 * 19050) + (.12 * (77400 - 19050)) + (.22 * (165000 - 77400)) + (.24 * (315000 - 165000)) + (
                    .32 * (employee_salary - 315000))
        elif (employee_salary >= 400001) and (employee_salary <= 600000):
            tax = (.1 * 19050) + (.12 * (77400 - 19050)) + (.22 * (165000 - 77400)) + (.24 * (315000 - 165000)) + (
                    .32 * (400000 - 315000)) + (.35 * (employee_salary - 400000))
        elif employee_salary >= 600001:
            tax = (.1 * 19050) + (.12 * (77400 - 19050)) + (.22 * (165000 - 77400)) + (.24 * (315000 - 165000)) + (
                    .32 * (400000 - 315000)) + (.35 * (600000 - 400000)) + (.37 * (employee_salary - 600000))
        else:
            pass
    tax = "%.2f" % round(tax, 2)
    return tax


def get_medicare_deduction(employee_salary):
    medicare_deduction = employee_salary * .0145
    medicare_deduction = "%.2f" % round(medicare_deduction, 2)
    return medicare_deduction


def get_state_income_tax_deduction(employee_state, employee_salary):
    if employee_state == " ":
        employee_state_income_tax = employee_salary * 0.0

    # Fixed rate states 8 states

    elif employee_state == "Colorado" or "COLORADO" or "colorado" or "CO" or "co":
        employee_state_income_tax = employee_salary * .0463

    elif employee_state == "Illinois" or "ILLINOIS" or "illinois" or "IL" or "il":
        employee_state_income_tax = employee_salary * .0495

    elif employee_state == "Indiana" or "INDIANA" or "indiana" or "IN" or "in":
        employee_state_income_tax = employee_salary * .0323

    elif employee_state == "Massachusetts" or "MASSACHUSETTS" or "massachusetts" or "MA" or "ma":
        employee_state_income_tax = employee_salary * .051

    elif employee_state == "Michigan" or "MICHIGAN" or "michigan" or "MI" or "mi":
        employee_state_income_tax = employee_salary * .0425

    elif employee_state == "North Carolina" or "NORTH CAROLINA" or "north carolina" or "NC" or "nc":
        employee_state_income_tax = employee_salary * .05499

    elif employee_state == "Pennsylvania" or "PENNSYLVANIA" or "pennsylvania" or "PA" or "pa":
        employee_state_income_tax = employee_salary * .0307

    elif employee_state == "Utah" or "UTAH" or "utah" or "UT" or "ut":
        employee_state_income_tax = employee_salary * .05

    # no state income tax 7 states

    elif employee_state == "Alaska" or "ALASKA" or "alaska" or "AK" or "ak":
        employee_state_income_tax = employee_salary * 0.0

    elif employee_state == "Washington" or "WASHINGTON" or "washington" or "WA" or "wa":
        employee_state_income_tax = employee_salary * 0.0

    elif employee_state == "Nevada" or "NEVADA" or "nevada" or "NV" or "nv":
        employee_state_income_tax = employee_salary * 0.0

    elif employee_state == "Wyoming" or "WYOMING" or "wyoming" or "WY" or "wy":
        employee_state_income_tax = employee_salary * 0.0

    elif employee_state == "South Dakota" or "SOUTH DAKOTA" or "south dakota" or "SD" or "sd":
        employee_state_income_tax = employee_salary * 0.0

    elif employee_state == "Texas" or "TEXAS" or "texas" or "TX" or "tx":
        employee_state_income_tax = employee_salary * 0.0

    elif employee_state == "Florida" or "FLORIDA" or "florida" or "FL" or "fl":
        employee_state_income_tax = employee_salary * 0.0

    # states with adjustable income tax rates

    elif employee_state == "Alabama" or "ALABAMA" or "alabama" or "AL" or "al":
        employee_state_income_tax = employee_salary * .05

    elif employee_state == "Arizona" or "ARIZONA" or "arizona" or "AZ" or "az":
        employee_state_income_tax = employee_salary * .0454

    elif employee_state == "Arkansas" or "ARKANSAS" or "arkansas" or "AR" or "ar":
        employee_state_income_tax = employee_salary * .069

    elif employee_state == "California" or "CALIFORNIA" or "california" or "CA" or "ca":
        employee_state_income_tax = employee_salary * .123

    elif employee_state == "Connecticut" or "CONNECTICUT" or "connecticut" or "CT" or "ct":
        employee_state_income_tax = employee_salary * .0699

    elif employee_state == "Delaware" or "DELAWARE" or "delaware" or "DE" or "de":
        employee_state_income_tax = employee_salary * .066

    elif employee_state == "Georgia" or "GEORGIA" or "georgia" or "GA" or "ga":
        employee_state_income_tax = employee_salary * .06

    elif employee_state == "Hawaii" or "HAWAII" or "hawaii" or "HI" or "hi":
        employee_state_income_tax = employee_salary * .11

    elif employee_state == "Idaho" or "IDAHO" or "idaho" or "ID" or "id":
        employee_state_income_tax = employee_salary * .074

    elif employee_state == "Iowa" or "IOWA" or "iowa" or "IA" or "ia":
        employee_state_income_tax = employee_salary * .0898

    elif employee_state == "Kansas" or "KANSAS" or "kansas" or "KS" or "ks":
        employee_state_income_tax = employee_salary * .057

    elif employee_state == "Kentucky" or "KENTUCKY" or "kentucky" or "KY" or "ky":
        employee_state_income_tax = employee_salary * .06

    elif employee_state == "Louisiana" or "LOUISIANA" or "louisiana" or "LA" or "la":
        employee_state_income_tax = employee_salary * .06

    elif employee_state == "Main" or "MAIN" or "main" or "ME" or "me":
        employee_state_income_tax = employee_salary * .0715

    elif employee_state == "Maryland" or "MARYLAND" or "maryland" or "MD" or "md":
        employee_state_income_tax = employee_salary * .0575

    elif employee_state == "Minnesota" or "MINNESOTA" or "minnesota" or "MN" or "mn":
        employee_state_income_tax = employee_salary * .0985

    elif employee_state == "Mississippi" or "MISSISSIPPI" or "mississippi" or "MS" or "ms":
        employee_state_income_tax = employee_salary * .05

    elif employee_state == "Missouri" or "MISSOURI" or "missouri" or "MO" or "mo":
        employee_state_income_tax = employee_salary * .059

    elif employee_state == "Montana" or "MONTANA" or "montana" or "MT" or "mt":
        employee_state_income_tax = employee_salary * .069

    elif employee_state == "Nebraska" or "NEBRASKA" or "nebraska" or "NE" or "ne":
        employee_state_income_tax = employee_salary * .0684

    elif employee_state == "New Jersey" or "NEW JERSEY" or "new jersey" or "NJ" or "nj":
        employee_state_income_tax = employee_salary * .0897

    elif employee_state == "New Mexico" or "NEW MEXICO" or "new mexico" or "NM" or "nm":
        employee_state_income_tax = employee_salary * .049

    elif employee_state == "New York" or "NEW YORK" or "new york" or "NY" or "ny":
        employee_state_income_tax = employee_salary * .0882

    elif employee_state == "North Dakota" or "NORTH DAKOTA" or "north dakota" or "ND" or "nd":
        employee_state_income_tax = employee_salary * .029

    elif employee_state == "Ohio" or "OHIO" or "ohio" or "OH" or "oh":
        employee_state_income_tax = employee_salary * .04997

    elif employee_state == "Oklahoma" or "OKLAHOMA" or "oklahoma" or "OK" or "ok":
        employee_state_income_tax = employee_salary * .05

    elif employee_state == "Oregon" or "OREGON" or "oregon" or "OR" or "or":
        employee_state_income_tax = employee_salary * .099

    elif employee_state == "Rhode Island" or "RHODE ISLAND" or "rhode island" or "RI" or "ri":
        employee_state_income_tax = employee_salary * .0599

    elif employee_state == "South Carolina" or "SOUTH CAROLINA" or "south carolina" or "SC" or "sc":
        employee_state_income_tax = employee_salary * .07

    elif employee_state == "Vermont" or "VERMONT" or "vermont" or "VT" or "vt":
        employee_state_income_tax = employee_salary * .0895

    elif employee_state == "Virginia" or "VIRGINIA" or "virginia" or "VA" or "va":
        employee_state_income_tax = employee_salary * .0575

    elif employee_state == "West Virginia" or "WEST VIRGINIA" or "west virginia" or "WV" or "wv":
        employee_state_income_tax = employee_salary * .065

    elif employee_state == "Wisconsin" or "WISCONSIN" or "wisconsin" or "WI" or "wi":
        employee_state_income_tax = employee_salary * .0765

    elif employee_state == "Washington DC" or "WASHINGTON DC" or "washington dc" or "DC" or "dc":
        employee_state_income_tax = employee_salary * .0895

    # if a state is incorrectly spelt
    else:
        employee_state_income_tax = employee_salary * 0.0

    employee_salary = "%.2f" % round(employee_salary, 2)
    employee_state_income_tax = "%.2f" % round(employee_state_income_tax, 2)
    return employee_state_income_tax


def get_social_security_deduction(employee_salary):
    if employee_salary <= 128400:
        social_security_deduction = employee_salary * .062
    elif employee_salary > 128400:
        social_security_deduction = 128400 * .062
    social_security_deduction = "%.2f" % round(social_security_deduction, 2)
    return social_security_deduction

def total_salary_deduction(employee_salary, employee_marriage_status, employee_state):
    final_employee_salary = employee_salary - float(get_medicare_deduction(employee_salary)) - float(get_federal_income_tax_deduction(employee_salary, employee_marriage_status)) - float(get_state_income_tax_deduction(employee_state, employee_salary)) - float(get_social_security_deduction(employee_salary))
    return str(final_employee_salary)