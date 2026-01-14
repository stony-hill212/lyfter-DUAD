employee_info={
    "name": "David",
    "email": "dzelayasegura@gmail",
    "access_level": 5,
    "age": 27
}
deleted_item=employee_info.pop("access_level")
deleted_item2=employee_info.pop("age")
print(employee_info)
print(f"Deleted items: {deleted_item, deleted_item2}")