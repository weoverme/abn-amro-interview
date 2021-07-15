# ABN Amro Interview

## Assumptions:
1.	To use the provided Specifications to get necessary fields and their columns.
2.	Input file will always be tab delimited.
3.	Input.txt to be provided on a consistent daily basis.

## Solution
1. Provide a script that may produce a report. This will be run from the command line/terminal.
2. Provide a daily transaction summary report to the required user that based on the below <br>
&nbsp;&nbsp;&nbsp;&nbsp;a.	Client Information<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i.	Client Type<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ii.	Client Number<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iii.	Account Number<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iv.	Subaccount Number<br>
&nbsp;&nbsp;&nbsp;&nbsp;b.	Product Information<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i.	Exchange Code<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ii.	Product Group<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iii.	Symbol<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iv.	Expiry Date<br>
&nbsp;&nbsp;&nbsp;&nbsp;c.	Total Transaction Amount<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i.	Quantity Long<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ii.	Quantity Short<br>

### How to run

1. Ensure Python 3.x is running
    python --version

2. Change directory to where the parser is.<br>i.e. abn-amro-interview/build/lib/src

3. Run the parser <br>python parser.py path_of_input path_of_output delimiter
<br>Ex. python parser.py Input.txt Output.txt ,

You may place the Input.txt into /res directory.


## What actually happened:
1. I read the requirements and produced "Impact Analysis", which consists of assumptions and my projected design and solution.
2. Created a PyCharm project and git init with several files and directories.
3. I identified different fields from the "System A File Specification.pdf" and converted it into a mapping within parser.py. My initial idea was to use it as an enum, but using a dict like a JSON would work better. This included all the required fields as in the requirements document, but somehow, the transaction date and price and buysell code were important in that thought process. In hindsight, this made things a lot more complicated that it should have been.
4. The program was designed to have two main classes - Transaction and Parser. Transaction takes in a line of input and transforms it into an object, and Parser will use the Transaction objects to group and perform functions upon. This was to repeating code everywhere.
5. The class Transaction has getters for each field in the mapping, developed using TDD, to convert the line of input into an object form. Additionally, it had simple calculation functions to obtain single values using the Transaction objects. Unfortunately, due to the shortage of time, I was not able to put in extensive and complete testing.
6. The class Parser's main objective is to use the Transaction objects to group per client_information (client type, number, acc no., subacc no.) and per product_information (exchange code, product group, symbol, expiry date) to obtain the total number of transactions.
8. I realised in my sleep that I was overcomplicating the requirements and reduced the complexity, back to only that which was mentioned. This procese removed transaction date, price, buysell code, and the movement code. It was at this point in the dev process, I dropped using TDD in order to meet time requirements (aim was to submit by noon). 
9. After removing the fields in #8, I was able to produce the remaining code for the parser to group transactions by client information and product information with better flow. However, I was unable to finish coding the tests for these.
10. I tested the program by running in the terminal and confirmed that when there were not enough args, it would show an error and show the right way to do it, as well as the correct order of args. Unfortunately, it cannot prevent user error, where the output and input paths may be switched around.
11. After confirming that it was working as expected, I added in an extra arg for delimiter, so that the user may define what their delimiter would be in the output file. 
12. I cleaned the code by removing any debug print statements, unnecessary comments and code blocks, and instead added in logging to track progress and any error messages. During this process, I realised the string format %(string) was the "old way of doing things" and refactored to use f"{}" instead.
13. After confirming I had done all I could do within the time available to me, the project went through the build process.
14. 
