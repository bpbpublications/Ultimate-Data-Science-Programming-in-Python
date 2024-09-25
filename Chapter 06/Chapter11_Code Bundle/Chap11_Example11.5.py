import polars as mypl
mydf = mypl.DataFrame({"Random_Data": ["Mango", "Pear and Fear", "Bana$na", None, 'ab 12 cd','34 efgh 56']})
print('Case1: Checking of data ')
print(mydf.select(
    mypl.col("Random_Data"),
    mypl.col("Random_Data").str.contains("Man|na").alias("Myregex"),
    mypl.col("Random_Data").str.contains("Bana$", literal=True).alias("Myliteral"),
    mypl.col("Random_Data").str.starts_with("Bana").alias("Mystarts_with"),
    mypl.col("Random_Data").str.ends_with("Fear").alias("Myends_with")))
# The  literal=True  parameter ensures that the search is done as a literal string instead of a regular expression. 
print('-'*50)
print('Case2: Extracting the characters')
print(mydf.select(
    mypl.col("Random_Data").str.extract_all(r"([^\d\s]+)").alias("extracted_chars"),
))