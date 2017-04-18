# DecisionTrees
A python ID3 decision trees implementation

## Usage
Structure of the directory is like:
- buildTree.py
- testdata.txt

To run the program, use the following command under the directory:

`% python buildTree.py`

## Input
The input file is changed into csv format for program to read:

```
Size,Occupied,Price,Music,Location,VIP,FavoriteBeer,Enjoy
Large,High,Expensive,Loud,Talpiot,No,No,No
Large,High,Expensive,Loud,City-Center,Yes,No,Yes
Large,Moderate,Normal,Quiet,City-Center,No,Yes,Yes
Medium,Moderate,Expensive,Quiet,German-Colony,No,No,No
Large,Moderate,Expensive,Quiet,German-Colony,Yes,Yes,Yes
Small,Moderate,Normal,Quiet,Ein-Karem,No,No,Yes
Large,Low,Normal,Quiet,Ein-Karem,No,No,No
Small,Moderate,Cheap,Loud,Mahane-Yehuda,No,No,Yes
Medium,High,Expensive,Loud,City-Center,Yes,Yes,Yes
Medium,Low,Cheap,Quiet,City-Center,No,No,No
Large,Moderate,Cheap,Loud,Talpiot,No,Yes,No
Large,Low,Cheap,Quiet,Talpiot,Yes,Yes,No
Medium,Moderate,Expensive,Quiet,Mahane-Yehuda,No,Yes,Yes
Medium,High,Normal,Loud,Mahane-Yehuda,Yes,Yes,Yes
Large,Moderate,Normal,Loud,Ein-Karem,No,Yes,Yes
Small,High,Normal,Quiet,German-Colony,No,No,No
1Large,High,Cheap,Loud,City-Center,No,Yes,Yes
Small,Low,Normal,Quiet,City-Center,No,No,No
Medium,Low,Expensive,Loud,Mahane-Yehuda,No,No,No
Medium,Moderate,Normal,Quiet,Talpiot,No,No,Yes
Medium,Low,Normal,Quiet,City-Center,No,No,Yes
```

In addition, a variable is defined to store attributes and their categories in order with a dictionary. This is used to output the final decision tree in order for each level:

```
attrResult = {'Size': ['Large','Medium','Small'],
             'Occupied': ['High', 'Moderate', 'Low'],
             'Price': ['Expensive', 'Normal', 'Cheap'],
             'Music': ['Loud', 'Quiet'],
             'Location': ['Talpiot', 'City-Center', 'Mahane-Yehuda',
'Ein-Karem', 'German-Colony'],
             'VIP': ['Yes', 'No'],
             'FavoriteBeer': ['Yes', 'No']}
```
             
We also define the prediction in dictionary in our program:

```
prediction = {'Size': 'Large',
             'Occupied': 'Moderate',
             'Price': 'Cheap',
             'Music': 'Loud',
             'Location': 'City-Center',
             'VIP': 'No',
             'FavoriteBeer': 'No'}
```

## Output

The output decision tree and prediction is shown as follows:

```
Occupied
Location, Location, Size
No, Yes, Yes, Tie, No, Size, Yes, Yes, Yes, Size, No, Price, No
No, Yes, Tie, Yes, No, Tie, No, Yes, No
Yes
```
