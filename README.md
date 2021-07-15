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

