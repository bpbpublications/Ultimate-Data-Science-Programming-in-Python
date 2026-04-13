import polars as mypl
# Polars DataFrame creation with 8-bit signed integers
mydf_int8 = mypl.DataFrame({
    'int8_column': [11, 12, 13],
})
# Polars DataFrame creation with 16-bit signed integers
mydf_int16 = mypl.DataFrame({
    'int16_column': [1100, 1200, 1300],
})
# Polars DataFrame creation with 32-bit signed integers
mydf_int32 = mypl.DataFrame({
    'int32_column': [11000, 12000, 13000],
})
# Polars DataFrame creation with 64-bit signed integers
mydf_int64 = mypl.DataFrame({
    'int64_column': [110000, 120000, 130000],
})
# Polars DataFrame creation with 8-bit unsigned integers
mydf_uint8 = mypl.DataFrame({
    'int8_column': [11, 12, 13],
})
# Polars DataFrame creation with 16-bit unsigned integers
mydf_uint16 = mypl.DataFrame({
    'int16_column': [1100, 1200, 1300],
})
# Polars DataFrame creation with 32-bit unsigned integers
mydf_uint32 = mypl.DataFrame({
    'int32_column': [11000, 12000, 13000],
})
# Polars DataFrame creation with 64-bit unsigned integers
mydf_uint64 = mypl.DataFrame({
    'int64_column': [110000, 120000, 130000],
})
mydf_f32 = mypl.DataFrame({
    'float32_column': [11.23, 14.56, 17.89],
})
mydf_f64 = mypl.DataFrame({
    'float64_column': [11.23, 14.56, 17.89],
})
# Display the DataFrames
print("8-bit integers:")
print(mydf_int8)
print('-'*50)
print("\n16-bit integers:")
print(mydf_int16)
print('-'*50)
print("\n32-bit integers:")
print(mydf_int32)
print('-'*50)
print("\n64-bit integers:")
print(mydf_int64)
print('-'*50)
print("8-bit unsigned integers:")
print(mydf_int8)
print('-'*50)
print("\n16-bit unsigned integers:")
print(mydf_int16)
print('-'*50)
print("\n32-bit unsigned integers:")
print(mydf_int32)
print('-'*50)
print("\n64-bit unsigned integers:")
print(mydf_int64)
print('-'*50)
print("\n32-bit floating point:")
print(mydf_f32)
print('-'*50)
print("\n64-bit floating point:")
print(mydf_f64)