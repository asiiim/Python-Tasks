# Method to request date
def request_date():
    day = int(input("Day: "))

    # Check if day value exceeds more than 31
    while day >= 32:
        print("Please enter correct day value.")
        day = int(input("Day: "))
    
    mth = int(input("Month: "))

    # Check if day value exceeds more than 12
    while mth >= 13:
        print("Please enter correct month value.")
        mth = int(input("Month: "))
    yr = int(input("Year: "))
    return day, mth, yr

# Main method
def calc_capital_gains_tax():
    # Request stock purchase & sale date
    print("\nEnter stock purchase date")
    stk_prc_day, stk_prc_mth, stk_prc_yr = request_date()

    print("\nEnter stock sale date")
    stk_sal_day, stk_sal_mth, stk_sal_yr = request_date()

    # Store stock hold duration in months
    stk_hold_mth = 0.0

    # Check if purchase date is older than sale date
    yr_diff = stk_sal_yr - stk_prc_yr
    mth_diff = stk_sal_mth - stk_prc_mth
    day_diff = stk_sal_day - stk_prc_day

    if yr_diff > 0.0:
        stk_hold_mth += yr_diff * 12
        stk_hold_mth += mth_diff
        stk_hold_mth += day_diff / 30
    elif yr_diff == 0.0:
        if mth_diff > 0.0:
            stk_hold_mth += mth_diff
        elif mth_diff == 0.0:
            if day_diff >= 0.0:
                stk_hold_mth += day_diff / 30
            else:
                print("\nError: Sold day seems older than the purchased one.")
                print("Please try again.")
                return calc_capital_gains_tax()
        else:
            print("\nError: Sold month seems older than the purchased one.")
            print("Please try again.")
            return calc_capital_gains_tax()
    else:
        print("\nError: Sold year seems older than the purchased one.\n")
        print("Please try again.")
        return calc_capital_gains_tax()

    # Request number of shares
    print("------------------------------------------")
    share_qty = float(input("Enter number of shares: "))

    # Request purchase price per unit
    prc_rate = float(input("Purchase price per unit: "))

    # Request sale price per unit
    sal_rate = float(input("Sale Price per unit: "))

    # Request income tax rate in percentage
    inc_tax_rate = float(input("Income tax rate %: "))

    # This is the string variable that records the result regarding capital gains and tax information.
    result = ""

    # Compute total purchase & sale value with capital gains/losses
    total_prc_val = prc_rate * share_qty
    total_sale_val = sal_rate * share_qty
    capital_gains = total_sale_val - total_prc_val

    result += "\nTotal purchase value = $" + str("{:,}".format(total_prc_val))
    result += "\nTotal sale value = $" + str("{:,}".format(total_sale_val))
    result += "\nCapital gains = $" + str("{:,}".format(capital_gains))

    if capital_gains > 0.0:
        if stk_hold_mth >= 12.0:
            taxable_capital_gains = capital_gains * 0.5
            tax_due = round(taxable_capital_gains * (inc_tax_rate / 100), 2)
            
            result += "\nThe stock was held for 12 months or more.\nClient is *eligible* for a 50% discount on capital gains tax."
            result += "\n------------------------------------------"
            result += "\nTaxable capital gains = $" + str("{:,}".format(taxable_capital_gains))
            result += "\nIncome tax rate = $" + str("{:,}".format(taxable_capital_gains))
            result += "\nTax due = $" + str("{:,}".format(tax_due))
        else:
            taxable_capital_gains = capital_gains
            tax_due = round(taxable_capital_gains * (inc_tax_rate / 100), 2)
            
            result += "\nThe stock was held for less than 12 months.\nClient is *not eligible* for a 50% discount on capital gains tax."
            result += "\n------------------------------------------"
            result += "\nTaxable capital gains = $" + str("{:,}".format(taxable_capital_gains))
            result += "\nTax due = $" + str("{:,}".format(tax_due))
    else:
        result += "\nClient had a capital loss. No taxes are applicable."

    result += "\n------------------------------------------"
    result += "\nThank You !\n"
    return result

# Execute the main method
result = calc_capital_gains_tax()
print(result)
