# devops_python_task
Here is the Coding test from NBC . Please complete this by EOD Monday. Let me know if you have questions. 

 
This is an API with the last 30 days by hour of bitcoin prices.

https://api.coinranking.com/v1/public/coin/1/history/30d

From that, output a JSON file, or display on a browser or endpoint values in this format:

 

[

{

    "date": "{date}",

    “price”: ”{value}",

    "direction": "{up/down/same}",

    "change": "{amount}",

    "dayOfWeek": "{name}”,

    "highSinceStart": "{true/false}”,

    “lowSinceStart": "{true/false}”

 

}

]

 

- date in format "2019-03-17T00:00:00"

- one entry per day at "00:00:00" hours

- results ordered by oldest date first.

- "direction" is direction of price change since previous day in the list, first day can be “na” ({up/down/same})

- "change" is the price difference between current and previous day. “na” for first

- "day of week" is name of the day (Saturday, Tuesday, etc)

- "high since start” / “low since start” is if this is the highest/lowest price since the oldest date in the list.

 

Example:

Day1 :

    price:100

    Highest:true

    Lowest:true

Day2:

    price:90

    Highest:false

    Lowest:true

Day3:

    price:101

    Highest:true

    Lowest:false

Etc…

 

- code should be written in python and hosted in github
