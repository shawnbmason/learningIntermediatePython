tables = {
  1: ['Jiho', False],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: [],
}
print(tables, "\n")

def assign_table(table_number, name, vip_status = False):
  tables[table_number] = [name, vip_status]
  
assign_table(6, "Yoni", False)
print(tables, "\n")

assign_table(table_number = 3, name = "Martha", vip_status = True)
print(tables, "\n")

assign_table(4, "Karla")
print(tables, "\n")
