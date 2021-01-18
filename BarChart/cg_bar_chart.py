# Import method from the provided monthcalc
from monthcalc import twelve_month_apart

# Import turtle for drawing bar chart
import turtle


def get_capital_gains(request_times):

    # Store the capital gains value in the list
    capital_gains_list = []

    for req in range(request_times):

        # Call capital gains tax method
        capital_gains = calc_capital_gains_tax(req + 1)
        capital_gains_list.append(capital_gains)

    return capital_gains_list


def calc_capital_gains_tax(request):

    # Request stock holding data
    print(f"\n=== Enter data for stock holding {request} ===")

    purchase_date = input("Purchase Date (YYYY-MM-DD) : ")
    sale_date = input("Sale Date (YYYY-MM-DD) : ")
    num_of_shares = float(input("Number of Shares : "))
    purchase_rate = float(input("Purchase price per unit : "))
    sale_rate = float(input("Sale price per unit : "))
    client_annual_gross_income = float(
        input("Client's annual gross income : ")
    )
    tax_rate = get_income_tax_rate(client_annual_gross_income)

    # Compute total purchase & sale value with capital gains/losses
    total_purchase_value = purchase_rate * num_of_shares
    total_sale_value = sale_rate * num_of_shares
    capital_gains = total_sale_value - total_purchase_value

    # This is the string variable that records the result regarding capital gains and tax information.
    result = ""
    result += "\nTotal purchase value = $" + str(
        "{:,}".format(total_purchase_value)
    )
    result += "\nTotal sale value = $" + str("{:,}".format(total_sale_value))
    result += "\nCapital gains = $" + str("{:,}".format(capital_gains))

    # Get stock hold duration data
    stock_hold_duration = twelve_month_apart(purchase_date, sale_date)

    if capital_gains > 0.0:
        if stock_hold_duration:
            taxable_capital_gains = capital_gains * 0.5
            tax_due = round(taxable_capital_gains * tax_rate, 2)

            result += "\n\nThe stock was held for 12 months or more.\nClient is *eligible* for a discount on capital gains tax."
            result += "\n\nTaxable capital gains = $" + str(
                "{:,}".format(taxable_capital_gains)
            )
            result += (
                "\nIncome Tax Rate = "
                + str("{:,}".format(tax_rate * 100))
                + "%"
            )
            result += "\nTax due = $" + str("{:,}".format(tax_due))
        else:
            taxable_capital_gains = capital_gains
            tax_due = round(taxable_capital_gains * tax_rate, 2)

            result += "\n\nThe stock was held for less than 12 months.\nClient is *not eligible* for a discount on capital gains tax."
            result += "\n\nTaxable capital gains = $" + str(
                "{:,}".format(taxable_capital_gains)
            )
            result += (
                "\nIncome Tax Rate = "
                + str("{:,}".format(tax_rate * 100))
                + "%"
            )
            result += "\nTax due = $" + str("{:,}".format(tax_due))
    else:
        result += "\nClient had a capital loss. No taxes are applicable."

    print(result)
    return capital_gains


def get_income_tax_rate(annual_gross_income):

    if annual_gross_income in range(18201, 37001):
        return 0.19
    elif annual_gross_income in range(37001, 90001):
        return 0.325
    elif annual_gross_income in range(90001, 180001):
        return 0.37
    elif annual_gross_income >= 180001:
        return 0.45
    else:
        return 0


# --------------------------------------------------------------------------------------
# Bar Chart Section
# --------------------------------------------------------------------------------------


def set_pos(t, x, y):
    """ Set Turtle Position """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.hideturtle()


def draw_dim_indicator(width, factor_value):
    current_position = t.pos()

    # Write down y-axis factor
    t.penup()
    t.left(90)
    t.forward(40)
    t.left(-90)
    t.write("$" + str(factor_value))
    t.goto(current_position)
    t.pendown()

    # Draw dim line and return back to same position
    t.right(90)
    t.color("Grey")
    t.forward(width)
    t.color("Black", "#87CEEB")
    t.right(-90)
    t.penup()
    t.goto(current_position)
    t.pendown()


def draw_axes(left_bottom_x, left_bottom_y, width, height, y_max):

    # For the purpose of y-axis dim indicator
    y_dim_factor = int(y_max / 5)
    y_dim_indicator_list = [y_dim_factor]
    for x in range(4):
        value = y_dim_indicator_list[x] + y_dim_factor
        y_dim_indicator_list.append(value)

    # Set the coordinate to given argument value
    set_pos(t, left_bottom_x, left_bottom_y)
    t.left(90)

    # Draw y-axis
    for x in y_dim_indicator_list:
        t.forward(int(height / 5))
        draw_dim_indicator(width, x)

    # Get back to same position and draw x-axis
    set_pos(t, left_bottom_x, left_bottom_y)
    t.right(90)
    t.forward(width)


def draw_bar(middle_x, bottom_y, width, height):
    set_pos(t, middle_x, bottom_y)
    t.penup()
    t.forward(width / 2)
    t.pendown()
    t.begin_fill()
    t.left(180)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


# Trigger barchart session
def request_barchart_param():

    print("\n=== Indicate the coordinates of the origin point ===")
    left_bottom_x = int(input("X-Coordinate : "))
    left_bottom_y = int(input("Y-Coordinate : "))

    print("\n=== Provide the size for the Bar Chart ===")
    width = int(input("Width (in Pixels): "))
    height = int(input("Height (in Pixels): "))

    print("\n=== Bar chart opens in new window ===")
    print("Thanks for using this app.")

    return left_bottom_x, left_bottom_y, width, height


def draw_bar_chart(data, left_bottom_x, left_bottom_y, width, height):

    # Get data max value and length
    max_value = max(data)
    data_len = len(data)

    # Draw axes for the barchart
    draw_axes(left_bottom_x, left_bottom_y, width, height, max_value)

    # Draw bars in the chart
    """ Get the height ration for the bar """
    height_max_value_ratio = height / max_value

    """ Get the width for the bar """
    bar_width = int(width / (2 * data_len))

    # Middle x-coordinate for the bar
    middle_x_factor = left_bottom_x + bar_width

    """ Compute height for each data list of the argument and draw the bars """
    for value in data:
        if value > 0:
            bar_height = value * height_max_value_ratio
            draw_bar(
                middle_x_factor, left_bottom_y, bar_width, int(bar_height)
            )
        else:
            draw_bar(middle_x_factor, left_bottom_y, bar_width, 0)

        middle_x_factor += 2 * bar_width


# --------------------------------------------------------------------------------------
# Trigger the workflow
# --------------------------------------------------------------------------------------

# Call method request_stock_holding_data and generate bar chart
holding_count = int(input("\nEnter the number of stock holdings: "))
capital_gains_list = get_capital_gains(holding_count)

# Generate barchart
left_bottom_x, left_bottom_y, width, height = request_barchart_param()
s = turtle.Screen()
s.title("Capital Gains Chart")
t = turtle.Turtle()

draw_bar_chart(capital_gains_list, left_bottom_x, left_bottom_y, width, height)

t.speed(1)
t.pensize(2)
t.color("black", "#87CEEB")

turtle.done()
