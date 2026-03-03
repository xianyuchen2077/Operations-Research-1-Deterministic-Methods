* Signature: 0x8f82c1143941e9ab
NAME Computer_Purchase_Optimization
ROWS
 N  OBJ
 G  nonnegative_purchase_number_from_Vendor_1
 G  min_purchase_quantity_from_Vendor_1
 L  max_purchase_quantity_from_Vendor_1
 G  nonnegative_purchase_number_from_Vendor_2
 G  min_purchase_quantity_from_Vendor_2
 L  max_purchase_quantity_from_Vendor_2
 G  nonnegative_purchase_number_from_Vendor_3
 G  min_purchase_quantity_from_Vendor_3
 L  max_purchase_quantity_from_Vendor_3
 E  total_number_of_computers_planned_to_purchase
COLUMNS
    MARKER    'MARKER'                 'INTORG'
    whether_purchase_from_Vendor_1  OBJ       5000
    whether_purchase_from_Vendor_1  min_purchase_quantity_from_Vendor_1  -200
    whether_purchase_from_Vendor_1  max_purchase_quantity_from_Vendor_1  -500
    whether_purchase_from_Vendor_2  OBJ       4000
    whether_purchase_from_Vendor_2  min_purchase_quantity_from_Vendor_2  -200
    whether_purchase_from_Vendor_2  max_purchase_quantity_from_Vendor_2  -900
    whether_purchase_from_Vendor_3  OBJ       6000
    whether_purchase_from_Vendor_3  min_purchase_quantity_from_Vendor_3  -200
    whether_purchase_from_Vendor_3  max_purchase_quantity_from_Vendor_3  -400
    MARKER    'MARKER'                 'INTEND'
    Number_purchased_from_Vendor_1  nonnegative_purchase_number_from_Vendor_1  1
    Number_purchased_from_Vendor_1  min_purchase_quantity_from_Vendor_1  1
    Number_purchased_from_Vendor_1  max_purchase_quantity_from_Vendor_1  1
    Number_purchased_from_Vendor_1  total_number_of_computers_planned_to_purchase  1
    Number_purchased_from_Vendor_2  nonnegative_purchase_number_from_Vendor_2  1
    Number_purchased_from_Vendor_2  min_purchase_quantity_from_Vendor_2  1
    Number_purchased_from_Vendor_2  max_purchase_quantity_from_Vendor_2  1
    Number_purchased_from_Vendor_2  total_number_of_computers_planned_to_purchase  1
    Number_purchased_from_Vendor_3  nonnegative_purchase_number_from_Vendor_3  1
    Number_purchased_from_Vendor_3  min_purchase_quantity_from_Vendor_3  1
    Number_purchased_from_Vendor_3  max_purchase_quantity_from_Vendor_3  1
    Number_purchased_from_Vendor_3  total_number_of_computers_planned_to_purchase  1
RHS
    RHS1      total_number_of_computers_planned_to_purchase  1100
BOUNDS
 BV BND1      whether_purchase_from_Vendor_1
 BV BND1      whether_purchase_from_Vendor_2
 BV BND1      whether_purchase_from_Vendor_3
QUADOBJ
    whether_purchase_from_Vendor_1  Number_purchased_from_Vendor_1  500
    whether_purchase_from_Vendor_2  Number_purchased_from_Vendor_2  350
    whether_purchase_from_Vendor_3  Number_purchased_from_Vendor_3  250
ENDATA
