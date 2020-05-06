#
# RiverNET Water Quality Documentation

## **Documentation Contents:**

[Class Diagram](#_jadljggx0c2r)

[Important Classes](#_457kqwlupqc2)

User Documentation

###


###


### Class Diagram

![](RackMultipart20200506-4-1h7e5q4_html_7831dcc175c81b55.png)

### Important Classes

**Model, Forms, View**

Data collection in the Rivernet application is implemented via the files model.py, forms.py, and view.py. Each of which is located under the folder polls. In the file, model.py, the database structure is initiated as an object-relational database mapping via the WaterQuality object. Here the single line code means that each Rivernet row of data to be entered will be defined as a single JSON file. The forms.py file object, WaterQuality, defines each data attribute and its object type. From here, forms.py gets implemented by view.py and the HTML documents in the folder &quot;Template.&quot; Once the values are filled by the user, the &#39;OK&#39; button at the bottom defines a POST method which callsviews.py calls a POST method which acting on the WaterQuality data members, creates a JSON dictionary and saves those values by passing them into an instance of model.py&#39;s WaterQuality object .

###


###


###


###


User Documentation

To use app open [https://software-engineering-rivernet.appspot.com/](https://software-engineering-rivernet.appspot.com/)

Note: All fields must be filled out for form collection to work properly.

Field Data Types:

Collection Date: Date Drop Down

Collection Time: HH:MM:SS

Site ID: Drop Down Menu

Collector initials: Text

Jar Number: Drop Down Menu

Parameter: Drop Down Menu

Pval One: Float

Pval Two: Float

Pval Three: Float

Average: Float

Analyst Initials: Text

Enterer Initials: Text

Notes

If field is not desired enter -1.
