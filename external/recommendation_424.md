# CSV Injection

CSV injection can occur when there is not validated user input into CSV files. This type of attack is also known has formula injection.
It is important to preform input validation and not allow for a cell to begin with any of the following characters in order to prevent this attack:
* "="
* "+"
* "-"
* "@"
* "0x09" (Tab)
* "0x0D" (Carriage return)


## Manually

To manually test if the system is vulnerable to this type of attack the tester can look for a place where input is asked and add the following command:

```text
 =HYPERLINK(“[URL]“, “Click for Report”)
```

To verify if the attack was successful the tester can open the generated CSV file and check if the hyperlink appears in said file. If it is present, then, the system is vulnerable to this type of attack.