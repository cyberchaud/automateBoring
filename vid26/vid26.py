# .findall returns a list of matches
# this is different than .search which returns an object

# shorthand codes for common classes
# \d - any number
# \D - any non-number
# \w - any alphanumeric
# \W - any non-alphanumeric
# \s - any space, tab or newline
# \S - any not-space, not-tab, not-newline

# adding a plus after is 'one or more'
# \d+ find one or more digits

# to create a new character class [] are used
# vowelRegex = re.compile(r'[aeiouAEIOU]')

import re

def PrintGroup(x):
    try:
        print(mo.group())
    except AttributeError:
        print('Value not found')

phoneNumbRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumbRegex.search('My phone number is 415-555-1234.  Call me tomorrow')
PrintGroup(mo)

phoneNumbRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumbRegex.search('My phone number is 555-1234.  Call me tomorrow')
PrintGroup(mo)



resume = '''
Malik Rabb

Seattle, WA • 123-456-7891
mrabb@email.com
SUMMARY

Data Scientist with strong math background and 3+ years of experience using predictive modeling, data processing, and data mining algorithms to solve challenging business problems. Involved in Python open source community and passionate about deep reinforcement learning.
EDUCATION
Coral Springs University
Current - Current

Bachelor of Science in Mathematics
EXPERIENCE
River Tech, Data Scientist
Current - Current

    Built fuzzy matching algorithm using k-nearest neighbors to identify non-exact matching duplicates
    Designed and developed real time recommendation engine to rank sales leads for upsell opportunities
    Refined personalization algorithms for 1M+ customers on web and mobile
    Transformed raw data into MySQL with custom-made ETL application to prepare unruly data for machine learning

Retail Ocean, Data Scientist
Current - Current

    Leveraged 200M+ tweets to develop sentiment analysis model that helped improve sales and marketing strategies
    Used Python and Spark to scrape, clean, and analyze large datasets
    Helped build tools for detecting botnets with machine learning and data mining
456-123-7891
SKILLS

    2nd place at Coral Springs Big Data Hackathon (out of 150+ participants)
    Java, Python, C++, Hadoop ecosystem, and MySQL
    Data cleansing, modeling, and mining
    Machine learning
'''


print(phoneNumbRegex.findall(resume))
#PrintGroup(mo)

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food'))
consonantsRegex = re.compile(r'[^aeiouAEIOU ]')
print(consonantsRegex.findall('Robocop eats baby food'))