# Stock_Market_Trading_App  

Short description:  
An app that helps you understand the fluctuation in stock market shares through the uses of APIs and links you relevant news about that company that has come out in the past 48 hours.  

Long description:  
1. Takes the name of a company you specified (by var "STOCK") and using Alpha Vantage API it returns the stock market values for the last two days.  
2. Obtains the current date and the date of the previous two days.  
3. Using News API it returns the most three important articles in the past two days (48 hours) about that specified company.  
4. Using SMTP Port sends a mail to a specified email address in which states the name of the company, the title of the article, % increase/decrease in share values, a short brief of the article and an actual link to that specific article for all three of them.  

---

## CONFIGURATION  

### SMTP Port  
Please follow the "CONFIGURATION - SMTP Port" presented in "Birthday_Congratulation_Autosender" for configuring the SMTP Port.  
Link: [https://github.com/Drakkarok/Birthday_Congratulation_Autosender/blob/main/README.md](url)  
After following the linked document please replace "email_to_send_from" and "password_for_email" with your own email and app password.  

### Alpha Vantage API - key  
You will need an Alpha Vantage account (free version) in order to get your "stock_price_api_key". Simply replace it in the code.  
Link: [https://www.alphavantage.co/](url)  

### News API - key  
You will need a News API account (free version) in order to get your "news_api_key". Simply replace it in the code.
Link: [https://newsapi.org/](url)  

---

Build using: 
- requests;
- datetime;
- smtplib.

Functions:
- N/A.

Classes:
- N/A.

Methods:
- N/A.
