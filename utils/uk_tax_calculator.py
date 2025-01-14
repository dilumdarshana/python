def calculate_take_home(gross_annual):
    # Constants for 2023/24 tax year
    PERSONAL_ALLOWANCE = 12570
    BASIC_RATE_LIMIT = 50270
    HIGHER_RATE_LIMIT = 125140
    
    # Tax rates
    BASIC_RATE = 0.20
    HIGHER_RATE = 0.40
    ADDITIONAL_RATE = 0.45
    
    # NI thresholds and rates
    NI_PRIMARY_THRESHOLD = 12570
    NI_UPPER_LIMIT = 50270
    NI_BASIC_RATE = 0.12
    NI_HIGHER_RATE = 0.02
    
    # Calculate Income Tax
    tax = 0
    taxable_income = max(0, gross_annual - PERSONAL_ALLOWANCE)
    
    if gross_annual > HIGHER_RATE_LIMIT:
        # Additional rate
        additional_rate_income = gross_annual - HIGHER_RATE_LIMIT
        tax += additional_rate_income * ADDITIONAL_RATE
        taxable_income -= additional_rate_income
        
        # Higher rate
        higher_rate_income = HIGHER_RATE_LIMIT - BASIC_RATE_LIMIT
        tax += higher_rate_income * HIGHER_RATE
        taxable_income -= higher_rate_income
        
        # Basic rate
        tax += taxable_income * BASIC_RATE
        
    elif gross_annual > BASIC_RATE_LIMIT:
        # Higher rate portion
        higher_rate_income = taxable_income - (BASIC_RATE_LIMIT - PERSONAL_ALLOWANCE)
        tax += higher_rate_income * HIGHER_RATE
        taxable_income -= higher_rate_income
        
        # Basic rate portion
        tax += taxable_income * BASIC_RATE
        
    else:
        # Only basic rate
        tax += taxable_income * BASIC_RATE
    
    # Calculate National Insurance
    ni = 0
    if gross_annual > NI_PRIMARY_THRESHOLD:
        if gross_annual <= NI_UPPER_LIMIT:
            ni = (gross_annual - NI_PRIMARY_THRESHOLD) * NI_BASIC_RATE
        else:
            ni = (NI_UPPER_LIMIT - NI_PRIMARY_THRESHOLD) * NI_BASIC_RATE
            ni += (gross_annual - NI_UPPER_LIMIT) * NI_HIGHER_RATE
    
    # Calculate take-home pay
    take_home = gross_annual - tax - ni
    
    return {
        'gross_annual': gross_annual,
        'tax': tax,
        'national_insurance': ni,
        'take_home_annual': take_home,
        'take_home_monthly': take_home / 12
    }

# Example usage
salary = 60000
result = calculate_take_home(salary)
print(f"Gross Annual: £{result['gross_annual']:,.2f}")
print(f"Tax: £{result['tax']:,.2f}")
print(f"NI: £{result['national_insurance']:,.2f}")
print(f"Take-home (Annual): £{result['take_home_annual']:,.2f}")
print(f"Take-home (Monthly): £{result['take_home_monthly']:,.2f}")
