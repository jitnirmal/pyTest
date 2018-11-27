Julia is an event planner who assembles extravagant packages for weddings with guests ranging from 2 to 2000 people. Each guest gets a wedding favor as a souvenir of the event. Each item's price per unit is highly variable, so Julia keeps a list of the favor quantities and their associated prices per unit from previous quotes.

To price a new event, Julia consults her database of past quotes. Her method for determining favor pricing is as follows:

If the quantity needed for the new event is exactly the same as the quantity for a previous event, the unit price remains the same.
If she has a price for a larger quantity and a price for a smaller quantity, she will linearly interpolate the price of the quantity she needs from the unit prices for the closest smaller and larger quantities.
If the database only has 1 quantity, she assumes that the associated price is the per unit cost for the favor.
If the quantities for which she has quotes are all smaller or all larger than the amount she needs, then she linearly extrapolates the unit price from the 2 points closest to the quantity of favors she needs.
Sometimes, price quotes lapse. When this happens, Julia overwrites the old unit price with either a 0 or a negative number. The quantities associated with zero or negative unit prices must be disregarded.
 

For example, assume the price breaks occur for quantity = [25, 50, 100] units at price = [5.0, 4.0, 3.0]. A diagram follows with pricing for 75 and 150 units. In the graph, price versus quantity for given values are in blue. Our target numbers of guests and the linear extrapolation are plotted in red.

 



Function Description 
Complete the function interpolate in the editor below. The function must return the expected price per unit as a floating point number rounded to two decimals.

interpolate has the following parameter(s):
    n: an integer denoting the number of guests
    quantity[quantity[0],...quantity[m-1]]: an array of integers in increasing order
    price[price[0],...price[m-1]]: an array of floating point numbers where price[i] is the unit price when quantity[i] units were purchased.

 

Note: The interpolate function's array parameters may be vectors, where necessitated by the language.

 

Constraints

2 ≤ n ≤ 2000
1 ≤ m ≤ 100
|quantity| = |price| = m
quantity[i] < quantity[j], where 0 ≤ i < j < m
 

Input Format For Custom Testing
Sample Case 0
Sample Input 0

25
5
10
2.46
25
2.58
50
2.0
100
2.25
500
3.0
 

Sample Output 0

2.58
 

Explanation 0

The following arguments are passed to your interpolate function:

n = 25

quantity = { 10, 25, 50, 100, 500 }

price = { 2.46, 2.58, 2.0, 2.25, 3.0 }

 

The quantity 25 is in the database, so interpolate returns the unit price associated with that quantity.

 