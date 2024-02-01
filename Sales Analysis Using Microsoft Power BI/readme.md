# 2016 TO 2019 SALES ANALYSIS USING POWER BI

<p align = "center">
<img src = ".\img\2016 to 2019 Sales Analysis.drawio.png"> </img> </p>


## OVERVIEW:
- Superstore data comprises information about the __Order, Shipping, Customer Purchase__ Details in __United States__ with _Profit & Discount_ Earned from <b> <span style="color: orange;"> 2016 To 2019 </span> </b> 
- This Dashboard contains Three pages for each category that Superstore Dataset talks about:
  - Time Based Analysis
  - Regional Analysis
  - Product Analysis
- For Live Dashboard: [CLICK HERE](https://app.powerbi.com/view?r=eyJrIjoiN2VkOGYzZWItNWVlMS00ZjE3LTgwMzktM2QwNzk3NGNiYTJhIiwidCI6Ijk3ZTRiZDI4LTExNzMtNGIwYy04Yjg4LWE2NTE4ZmJiMWRkOCJ9)


### Time Based Analysis:
<br>
<p align = "center">
<img src = ".\img\Time series analysis.png"> </img> </p>

- This Page Explains charts about __Sales, Profit & Quality of sales__ on SuperStore Dataset.
- A Slicer [__Order Date__] is added in this page to control the Time Span of the Dataset
- A Card is added to display __Sum of Profit__ over that particular span of time frame

### Regional Analysis
<br>
<p align = "center">
<img src = ".\img\Regional Analysis.png"> </img> </p>

- Focusing on geography, this page illustrates how sales are distributed across different regions. It employs charts to help us to understand regional variations in sales performance, facilitating targeted decision-making.
- This Page Explains <span style="color: orange;"> Cards, Pie Chart, Stacked Column chart & Clustered Bar Chart</span>  about 
  - __Max of Sales by Product,__ 
  - __Max of Sales by Shiping Mode ,__ 
  - __Max sales by segments &__
  - __Max of sales by regions__ on SuperStore Dataset.
- As Segments Contains __Corporate, Consumer, Home Office.__
- AS Shipping mode contains 
  - Standard
  - First Class
  - Second Class
  - Same Day

### Product Analysis
<br>
<p align = "center">
<img src = ".\img\Product Analysis.png"> </img> </p>

- This Page Centered around products or product categories, this page offers insights into the sales performance of Each Category and Subcategories in Different regions with Sales, Profit, Discount. Users can analyze product trends, identify top-selling items, and make informed decisions based on product-specific data.
- This Page Explains <span style="color: orange;"> Cards,Pie chart, Treemap & Slicer </span> about 
  - __Max of Sales by Category,__ 
  - __Sum of sales__,
  - __Sum of discount__,
  - __Sum of profit__,
  - __Count of returned__,
  - __Sum of profit by sub-category__,
- Total number of Product Category 3 and Sub-Category 17

### INSIGHTS GATHARED:

<br>
<p align = "center">
<img src = ".\img\insights.png"> </img> </p>

- The Profit margin was very low as 11.09% for 88.91% of total sales
- Customer Count was increasing Steadly of 2.5% per year.

<p align = "center">
<img src = ".\img\insights1.png"> </img> </p>

- Max Sales of all times is $118k in Nov 2019 with Profit of $9.8k and Sales rate has down trended to $84k in Dec 2019 with profit of $8.4k.
- Max of Sales on Each regional:

  |            | Corporate | Consumer | Home Office |
  |------------| ----------|----------|-------------|
  |**Center**     | **32.32%**    |18.27%    | 7.04%|
  |**West**        | 9.39%    |**25.86%**    | 8.38%|
  |**East**       | 16.81%    |19.39%    | **20.69%**|
  |**South**       | 14.78%    |16.16%    | **41.82%**|

- Max of Sales by Shipping Mode:

  |            | Standard Class | First Class | Second Class | Same Day |
    |------------| ----------|----------|-------------|----------|
    |**Center**     | **32.78%**    |7.14%    | 10.2% |4.6%|
    |**West**        | 9.52%    |**26.22%**    | 15.34%|5.24%|
    |**East**       | 19.67%   |**20.98%**    | 8.74%|8.7%|
    |**South**       | **42.4%**   |5.69%    | 16.39|14.98%|

### ACTION REQUIRED:

- Campaigns on Each Regional should be cutomised based on 
  - Most selling Segments on each regions
    - **Center** - Corporate
    - **West** - Consumer
    - **South & East** -  Home Office
  - Most Used Shipping Mode:
    - **Center & South** - Standard Class
    - **West & East** -  First Class