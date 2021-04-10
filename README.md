# buySellAlerts
Project Requirement Specification(PRD)

Goal: Design a service which will poll stock market and generate alert after a condition is satisfied

Steps:

1. Create a python script to send email

2. Create a python script to get quote of ticker

3. Send an email if current price of ticker is less than 50 day moving average

4. Run above script as cronjob everyday at market open, mid-day and at market close

5. Run above script as lambda function, trigger event is time

6. Make Dockerfile of above script and run it as container

7. Create yaml and run it as kubernetes job

8. Run a database in kubernetes and fetch credential from database

9. Store and retrieve credentia in encrypted manner

10. Finally run above setup on raspbarry pi

11. Make rules pluggable and define rules list


Tech Stack to use: Python, SMTP lib, AWS, Docker, Kubernetes, Redis, financemodellingprep, REST API

Advance techniques:

1. Configurable rules

2. Only companies with market capitalization > 1 Billion, and quaterly revenue > 50 Million and Analyst rating = Buy, if stock dips by 5% send alert as message

3. Send email as well text message

4.If reply email is "buy" with quantity. Buy the stock by integrating with investment platform

5.Run a python server: Expose two REST API: GET /recommendation : return stocks which are buy as per rules
                                            POST /subscribe {email_address} : add email to list of email address
                                            POST /addStock {Ticker Symbol}: add stock for rules
                                            
6. Modernaize infrastructure:           

          Load Balancer: Envoy
          API ingress: Trafik
          DNS: check if we can use route53 or get domain name and map it our load balancer IP
          Logging: Elastic search, kibana, Fluend
          Monitoring: Prometheus, Alert manager with alert going to email or phone
          Security:   
               Network security/policies : Use Istio
               App security/Image scanning: Figure out cloud native tools
          Documentation tools:
          Ensure APIs are versioned
          Databases: PostGres for SQL, Etcd for key-Value
          Caching: Use Redis for caching of data and faster api response
          
 7. Write an operator for your app: 
          Operator will deploy app, databases, logging, monitoring infrastructure, if possible deploy load balancer
          
 8. Integrate a UI: such that charts, stock, subscripton can be done via UI
 9. Enhance charts:1) Get sentimental analysis of stock: 1) sentiment on reddit 2) sentiment on news 3) sentiment on twitter
 10. Co-relate sentiment to stock rise/fall and check if there is buy/sell signal
