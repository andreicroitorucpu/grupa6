cnp = "279146358279"


def county_check(cnp):
    counties = ["%.2d" % i for i in range(1,47)]
    counties.append('51')
    counties.append('52')
    inserted_county = cnp[6:8]
    if inserted_county in counties:
        return f"Valid: {inserted_county}"
    else:
        return f"Invalid: {inserted_county}"


print(county_check(cnp))
